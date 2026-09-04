"""Unit tests for gradients and optimization module."""

import pytest
import math
import numpy as np
from src import gradients


class TestNumericalGradient:
    """Test numerical gradient computation."""
    
    def test_gradient_quadratic(self):
        """Test gradient of quadratic function."""
        def f(x):
            return x[0]**2 + 2*x[1]**2
        
        x = np.array([1.0, 2.0])
        grad = gradients.numerical_gradient(f, x)
        expected = np.array([2.0, 8.0])  # df/dx = 2x, df/dy = 4y
        np.testing.assert_array_almost_equal(grad, expected, decimal=4)
    
    def test_gradient_rosenbrock(self):
        """Test gradient of Rosenbrock function."""
        grad = gradients.numerical_gradient(gradients.rosenbrock, [1.0, 1.0])
        # At minimum, gradient should be close to zero
        np.testing.assert_array_almost_equal(grad, [0, 0], decimal=2)


class TestGradientDescentOptimizer:
    """Test gradient descent optimization."""
    
    def test_minimize_quadratic(self):
        """Test minimizing a quadratic function."""
        def f(x):
            return (x[0] - 2)**2 + (x[1] - 3)**2
        
        optimizer = gradients.GradientDescentOptimizer(learning_rate=0.1, max_iterations=1000)
        x0 = np.array([0.0, 0.0])
        x_opt, history = optimizer.optimize(f, x0)
        
        # Should converge near [2, 3]
        expected = np.array([2.0, 3.0])
        np.testing.assert_array_almost_equal(x_opt, expected, decimal=1)
        
        # History should be decreasing
        for i in range(1, len(history)):
            assert history[i] <= history[i-1] + 1e-6


class TestMomentumOptimizer:
    """Test momentum-based optimization."""
    
    def test_momentum_optimization(self):
        """Test optimization with momentum."""
        def f(x):
            return (x[0] - 1)**2 + (x[1] - 1)**2
        
        optimizer = gradients.GradientDescentOptimizer(
            learning_rate=0.1,
            momentum=0.9,
            max_iterations=1000
        )
        x0 = np.array([0.0, 0.0])
        x_opt, history = optimizer.optimize(f, x0)
        
        # Should converge near [1, 1]
        expected = np.array([1.0, 1.0])
        np.testing.assert_array_almost_equal(x_opt, expected, decimal=1)


class TestNesterovMomentum:
    """Test Nesterov momentum optimization."""
    
    def test_nesterov_optimization(self):
        """Test optimization with Nesterov momentum."""
        def f(x):
            return (x[0] - 1)**2 + (x[1] - 1)**2
        
        optimizer = gradients.GradientDescentOptimizer(
            learning_rate=0.1,
            momentum=0.9,
            nesterov=True,
            max_iterations=1000
        )
        x0 = np.array([0.0, 0.0])
        x_opt, history = optimizer.optimize(f, x0)
        
        # Should converge
        expected = np.array([1.0, 1.0])
        np.testing.assert_array_almost_equal(x_opt, expected, decimal=1)


class TestAdamOptimizer:
    """Test Adam optimizer."""
    
    def test_adam_optimization(self):
        """Test Adam optimizer."""
        def f(x):
            return (x[0] - 2)**2 + 4*(x[1] - 3)**2
        
        optimizer = gradients.AdamOptimizer(learning_rate=0.1, max_iterations=1000)
        x0 = np.array([0.0, 0.0])
        x_opt, history = optimizer.optimize(f, x0)
        
        # Should converge near [2, 3]
        expected = np.array([2.0, 3.0])
        np.testing.assert_array_almost_equal(x_opt, expected, decimal=1)
        
        # History should be mostly decreasing (allow small numerical fluctuations)
        for i in range(1, len(history)):
            assert history[i] <= history[i-1] + 0.01


class TestTestFunctions:
    """Test functions used for optimization testing."""
    
    def test_rosenbrock_minimum(self):
        """Test Rosenbrock function at minimum."""
        x_min = np.array([1.0, 1.0])
        assert abs(gradients.rosenbrock(x_min)) < 1e-10
    
    def test_quadratic_function(self):
        """Test quadratic function."""
        A = np.array([[2, 0], [0, 3]])
        b = np.array([1, 2])
        x = np.array([0.5, 1.0])
        
        # f(x) = 0.5*x^T*A*x + b^T*x
        result = gradients.quadratic(x, A, b)
        expected = 0.5 * (2*0.25 + 3*1) + 1*0.5 + 2*1
        assert abs(result - expected) < 1e-10


class TestConvergence:
    """Test convergence criteria."""
    
    def test_convergence_detected(self):
        """Test that optimizer detects convergence."""
        def f(x):
            return x[0]**2 + x[1]**2
        
        optimizer = gradients.GradientDescentOptimizer(
            learning_rate=0.1,
            tolerance=1e-6,
            max_iterations=10000
        )
        x0 = np.array([0.1, 0.1])
        x_opt, history = optimizer.optimize(f, x0)
        
        # Should converge in fewer iterations
        assert len(history) < 10000


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
