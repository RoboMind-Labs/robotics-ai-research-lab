"""Gradient computation and optimization algorithms.

This module provides numerical gradient computation and various gradient-based
optimization algorithms including gradient descent, momentum, and Nesterov
momentum.

Author: Robotics AI Research Lab
"""

from typing import Callable, Tuple, List
import numpy as np


def numerical_gradient(f: Callable, x: np.ndarray, delta: float = 1e-5) -> np.ndarray:
    """Compute numerical gradient using finite differences.
    
    Uses central difference formula: ∇f[i] ≈ (f(x+δe_i) - f(x-δe_i)) / (2δ)
    
    Args:
        f: Function that takes array x and returns scalar
        x: Point at which to compute gradient
        delta: Finite difference step size
        
    Returns:
        Gradient vector of same shape as x
    """
    x = np.array(x, dtype=float)
    grad = np.zeros_like(x)
    
    for i in range(len(x)):
        x_plus = x.copy()
        x_minus = x.copy()
        x_plus[i] += delta
        x_minus[i] -= delta
        
        grad[i] = (f(x_plus) - f(x_minus)) / (2 * delta)
    
    return grad


class GradientDescentOptimizer:
    """Gradient descent optimization with various momentum variants.
    
    Solves: min f(x) by iteratively moving in negative gradient direction.
    """
    
    def __init__(self, learning_rate: float = 0.01, momentum: float = 0.0,
                nesterov: bool = False, max_iterations: int = 1000,
                tolerance: float = 1e-6):
        """Initialize optimizer.
        
        Args:
            learning_rate: Step size for gradient updates
            momentum: Momentum coefficient (0 = no momentum)
            nesterov: Use Nesterov momentum if True
            max_iterations: Maximum number of iterations
            tolerance: Convergence tolerance
        """
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.nesterov = nesterov
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        
        self.history = []
        self.gradient_history = []
    
    def optimize(self, f: Callable, x0: np.ndarray) -> Tuple[np.ndarray, List[float]]:
        """Run optimization.
        
        Args:
            f: Objective function (returns scalar)
            x0: Initial point
            
        Returns:
            Tuple of (optimal_x, history of objective values)
        """
        x = np.array(x0, dtype=float).flatten()
        v = np.zeros_like(x)  # Velocity for momentum
        
        self.history = []
        self.gradient_history = []
        
        for iteration in range(self.max_iterations):
            # Compute gradient
            grad = numerical_gradient(f, x)
            f_val = f(x)
            
            self.history.append(f_val)
            self.gradient_history.append(grad.copy())
            
            # Check convergence
            if iteration > 0 and abs(self.history[-1] - self.history[-2]) < self.tolerance:
                break
            
            if self.momentum > 0:
                if self.nesterov:
                    # Nesterov momentum
                    v = self.momentum * v - self.learning_rate * grad
                    x = x + self.momentum * v - self.learning_rate * grad
                else:
                    # Standard momentum
                    v = self.momentum * v - self.learning_rate * grad
                    x = x + v
            else:
                # Vanilla gradient descent
                x = x - self.learning_rate * grad
        
        return x, self.history
    
    def optimize_with_constraint(self, f: Callable, x0: np.ndarray,
                                constraint: Callable) -> Tuple[np.ndarray, List[float]]:
        """Run optimization with constraint.
        
        Constraint function should return 0 if satisfied, >0 if violated.
        
        Args:
            f: Objective function
            x0: Initial point
            constraint: Constraint function (0 = satisfied)
            
        Returns:
            Tuple of (optimal_x, history)
        """
        x = np.array(x0, dtype=float).flatten()
        v = np.zeros_like(x)
        
        self.history = []
        
        for iteration in range(self.max_iterations):
            # Compute gradient
            grad = numerical_gradient(f, x)
            f_val = f(x)
            
            self.history.append(f_val)
            
            # Check convergence
            if iteration > 0 and abs(self.history[-1] - self.history[-2]) < self.tolerance:
                break
            
            # Gradient step
            if self.momentum > 0:
                v = self.momentum * v - self.learning_rate * grad
                x_candidate = x + v
            else:
                x_candidate = x - self.learning_rate * grad
            
            # Project to feasible set if constraint violated
            if constraint(x_candidate) > 0:
                # Simple projection: move towards feasible region
                alpha = 0.5
                x_candidate = alpha * x + (1 - alpha) * x_candidate
            
            x = x_candidate
        
        return x, self.history


class AdamOptimizer:
    """Adaptive Moment Estimation (Adam) optimizer.
    
    Combines momentum and adaptive learning rates.
    """
    
    def __init__(self, learning_rate: float = 0.001, beta1: float = 0.9,
                beta2: float = 0.999, epsilon: float = 1e-8,
                max_iterations: int = 1000, tolerance: float = 1e-6):
        """Initialize Adam optimizer.
        
        Args:
            learning_rate: Initial learning rate
            beta1: Exponential decay rate for first moment (mean)
            beta2: Exponential decay rate for second moment (variance)
            epsilon: Small constant for numerical stability
            max_iterations: Maximum iterations
            tolerance: Convergence tolerance
        """
        self.learning_rate = learning_rate
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        
        self.history = []
    
    def optimize(self, f: Callable, x0: np.ndarray) -> Tuple[np.ndarray, List[float]]:
        """Run Adam optimization.
        
        Args:
            f: Objective function
            x0: Initial point
            
        Returns:
            Tuple of (optimal_x, history of objective values)
        """
        x = np.array(x0, dtype=float).flatten()
        m = np.zeros_like(x)  # First moment
        v = np.zeros_like(x)  # Second moment
        
        self.history = []
        
        for t in range(1, self.max_iterations + 1):
            # Compute gradient
            grad = numerical_gradient(f, x)
            f_val = f(x)
            
            self.history.append(f_val)
            
            # Check convergence
            if t > 1 and abs(self.history[-1] - self.history[-2]) < self.tolerance:
                break
            
            # Update biased first moment
            m = self.beta1 * m + (1 - self.beta1) * grad
            
            # Update biased second moment
            v = self.beta2 * v + (1 - self.beta2) * (grad ** 2)
            
            # Compute bias-corrected moments
            m_hat = m / (1 - self.beta1 ** t)
            v_hat = v / (1 - self.beta2 ** t)
            
            # Update parameters
            x = x - self.learning_rate * m_hat / (np.sqrt(v_hat) + self.epsilon)
        
        return x, self.history


def line_search_backtracking(f: Callable, x: np.ndarray, grad: np.ndarray,
                            direction: np.ndarray, c: float = 1e-4,
                            rho: float = 0.5, max_iterations: int = 100) -> float:
    """Find step size using backtracking line search.
    
    Args:
        f: Objective function
        x: Current point
        grad: Gradient at current point
        direction: Search direction
        c: Sufficient decrease constant (0 < c < 1)
        rho: Backtracking factor (0 < rho < 1)
        max_iterations: Maximum line search iterations
        
    Returns:
        Step size
    """
    alpha = 1.0
    f_x = f(x)
    grad_dot_dir = np.dot(grad, direction)
    
    for _ in range(max_iterations):
        x_new = x + alpha * direction
        f_new = f(x_new)
        
        if f_new <= f_x + c * alpha * grad_dot_dir:
            return alpha
        
        alpha *= rho
    
    return alpha


def rosenbrock(x: np.ndarray) -> float:
    """Rosenbrock function for testing optimization.
    
    f(x,y) = (1-x)² + 100(y-x²)²
    Minimum at (1, 1) with f=0
    
    Args:
        x: Point (should be 2D for classic Rosenbrock)
        
    Returns:
        Function value
    """
    x = np.array(x, dtype=float)
    return (1 - x[0]) ** 2 + 100 * (x[1] - x[0] ** 2) ** 2


def quadratic(x: np.ndarray, A: np.ndarray, b: np.ndarray) -> float:
    """Quadratic function f(x) = x^T A x + b^T x.
    
    Args:
        x: Point
        A: Positive definite matrix
        b: Vector
        
    Returns:
        Function value
    """
    x = np.array(x, dtype=float)
    return float(0.5 * np.dot(x, np.dot(A, x)) + np.dot(b, x))
