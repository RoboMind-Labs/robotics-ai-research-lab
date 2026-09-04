"""Eigenvalue and eigenvector operations for robotics applications.

This module provides functions for eigenvalue decomposition and
applications including principal component analysis and stability
analysis.

Author: Robotics AI Research Lab
"""

from typing import Tuple
import numpy as np


def eigenvalue_decomposition(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Compute eigenvalues and eigenvectors of a square matrix.
    
    For matrix A: A*v = λ*v where:
    - λ (lambda) are eigenvalues
    - v are the corresponding eigenvectors
    
    Args:
        A: Square matrix (n×n)
        
    Returns:
        Tuple of (eigenvalues, eigenvectors)
        - eigenvalues: Array of eigenvalues
        - eigenvectors: Matrix where column i is eigenvector for eigenvalue i
        
    Raises:
        ValueError: If matrix is not square
    """
    A = np.array(A, dtype=float)
    
    if A.shape[0] != A.shape[1]:
        raise ValueError(f"Eigenvalue decomposition requires square matrix, got {A.shape}")
    
    eigenvalues, eigenvectors = np.linalg.eig(A)
    return eigenvalues, eigenvectors


def power_method(A: np.ndarray, iterations: int = 100, 
                tolerance: float = 1e-6) -> Tuple[float, np.ndarray]:
    """Find largest eigenvalue and corresponding eigenvector using power method.
    
    Iteratively computes: x_{k+1} = A * x_k / ||A * x_k||
    Converges to dominant eigenvalue and eigenvector.
    
    Args:
        A: Square matrix (n×n)
        iterations: Maximum number of iterations
        tolerance: Convergence tolerance
        
    Returns:
        Tuple of (eigenvalue, eigenvector)
    """
    A = np.array(A, dtype=float)
    n = A.shape[0]
    
    # Start with random vector
    x = np.random.randn(n)
    x = x / np.linalg.norm(x)
    
    lambda_old = 0.0
    
    for _ in range(iterations):
        # Compute A*x
        y = np.dot(A, x)
        
        # Normalize
        x_new = y / np.linalg.norm(y)
        
        # Compute eigenvalue estimate using Rayleigh quotient
        lambda_new = np.dot(x_new, np.dot(A, x_new))
        
        # Check convergence
        if abs(lambda_new - lambda_old) < tolerance:
            break
        
        x = x_new
        lambda_old = lambda_new
    
    return lambda_new, x


def is_positive_definite(A: np.ndarray, tolerance: float = 1e-9) -> bool:
    """Check if matrix is positive definite using eigenvalues.
    
    A symmetric matrix is positive definite if all eigenvalues are positive.
    
    Args:
        A: Input matrix
        tolerance: Tolerance for positive eigenvalue threshold
        
    Returns:
        True if matrix is positive definite
    """
    eigenvalues, _ = eigenvalue_decomposition(A)
    return np.all(eigenvalues > tolerance)


def is_stable(A: np.ndarray, discrete: bool = False, 
             tolerance: float = 1e-9) -> bool:
    """Check stability of a system matrix using eigenvalues.
    
    Continuous system: Stable if all eigenvalues have negative real part
    Discrete system: Stable if all eigenvalues have magnitude < 1
    
    Args:
        A: System matrix
        discrete: True for discrete-time system, False for continuous
        tolerance: Numerical tolerance
        
    Returns:
        True if system is stable
    """
    eigenvalues, _ = eigenvalue_decomposition(A)
    
    if discrete:
        # Discrete: magnitude < 1
        return np.all(np.abs(eigenvalues) < (1 - tolerance))
    else:
        # Continuous: real part < 0
        return np.all(np.real(eigenvalues) < -tolerance)


def principal_component_analysis(X: np.ndarray, n_components: int = 2) -> Tuple[np.ndarray, np.ndarray]:
    """Perform Principal Component Analysis on data.
    
    Finds principal components (directions of maximum variance) and
    projects data onto these components.
    
    Args:
        X: Data matrix (n_samples × n_features)
        n_components: Number of components to keep
        
    Returns:
        Tuple of (transformed_data, components)
        - transformed_data: Data projected onto principal components
        - components: Principal component directions
    """
    # Center data
    X = np.array(X, dtype=float)
    X_centered = X - np.mean(X, axis=0)
    
    # Compute covariance matrix
    cov = np.cov(X_centered.T)
    
    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = eigenvalue_decomposition(cov)
    
    # Sort by eigenvalue magnitude (descending)
    idx = np.argsort(np.abs(eigenvalues))[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    
    # Keep top n_components
    components = eigenvectors[:, :n_components]
    
    # Project data
    transformed = np.dot(X_centered, components)
    
    return transformed, components


def matrix_condition_number_from_eigenvalues(A: np.ndarray) -> float:
    """Compute condition number from eigenvalues.
    
    For symmetric matrix: κ(A) = λ_max / λ_min
    Measures how well-conditioned the matrix is numerically.
    
    Args:
        A: Input matrix
        
    Returns:
        Condition number
    """
    eigenvalues, _ = eigenvalue_decomposition(A)
    eigenvalues = np.abs(eigenvalues)
    
    # Avoid division by zero
    if np.min(eigenvalues) < 1e-15:
        return float('inf')
    
    return np.max(eigenvalues) / np.min(eigenvalues)


def sort_eigenvalues(eigenvalues: np.ndarray, eigenvectors: np.ndarray,
                    descending: bool = True) -> Tuple[np.ndarray, np.ndarray]:
    """Sort eigenvalues and eigenvectors by magnitude.
    
    Args:
        eigenvalues: Array of eigenvalues
        eigenvectors: Matrix of eigenvectors (column vectors)
        descending: Sort in descending order if True
        
    Returns:
        Sorted (eigenvalues, eigenvectors)
    """
    idx = np.argsort(np.abs(eigenvalues))
    if descending:
        idx = idx[::-1]
    
    eigenvalues_sorted = eigenvalues[idx]
    eigenvectors_sorted = eigenvectors[:, idx]
    
    return eigenvalues_sorted, eigenvectors_sorted
