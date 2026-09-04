"""Matrix operations module for robotics mathematics.

This module provides matrix operations including creation, arithmetic,
decompositions, and system solving. Focuses on understanding the underlying
mathematics while using NumPy for efficient computation.

Author: Robotics AI Research Lab
"""

from typing import Union, Tuple
import numpy as np


def create_matrix(rows: int, cols: int, init_value: float = 0.0) -> np.ndarray:
    """Create a matrix with specified dimensions.
    
    Args:
        rows: Number of rows
        cols: Number of columns
        init_value: Initial value for all elements
        
    Returns:
        Matrix (2D array) of specified size
    """
    return np.full((rows, cols), init_value, dtype=float)


def identity_matrix(n: int) -> np.ndarray:
    """Create an n×n identity matrix.
    
    Args:
        n: Size of the matrix
        
    Returns:
        Identity matrix with 1s on diagonal, 0s elsewhere
    """
    return np.eye(n, dtype=float)


def matrix_multiply(A: Union[list, np.ndarray], B: Union[list, np.ndarray]) -> np.ndarray:
    """Multiply two matrices.
    
    Multiplies A (m×n) by B (n×p) to get result (m×p):
    C[i,j] = Σ_k A[i,k] * B[k,j]
    
    Args:
        A: First matrix (m×n)
        B: Second matrix (n×p)
        
    Returns:
        Product matrix (m×p)
        
    Raises:
        ValueError: If inner dimensions don't match
    """
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    
    if A.shape[1] != B.shape[0]:
        raise ValueError(f"Cannot multiply {A.shape} × {B.shape}: inner dimensions don't match")
    
    return np.dot(A, B)


def matrix_transpose(A: Union[list, np.ndarray]) -> np.ndarray:
    """Transpose a matrix.
    
    Swaps rows and columns: A^T[i,j] = A[j,i]
    
    Args:
        A: Input matrix
        
    Returns:
        Transposed matrix
    """
    return np.array(A, dtype=float).T


def matrix_determinant(A: Union[list, np.ndarray]) -> float:
    """Compute determinant of a square matrix.
    
    The determinant is a scalar value that represents the signed volume
    scaling factor of the linear transformation.
    
    Args:
        A: Square matrix (n×n)
        
    Returns:
        Determinant value
        
    Raises:
        ValueError: If matrix is not square
    """
    A = np.array(A, dtype=float)
    
    if A.shape[0] != A.shape[1]:
        raise ValueError(f"Determinant requires square matrix, got {A.shape}")
    
    return float(np.linalg.det(A))


def matrix_inverse(A: Union[list, np.ndarray]) -> np.ndarray:
    """Compute the inverse of a square matrix.
    
    For square matrix A, inverse A^(-1) satisfies: A * A^(-1) = I
    
    Args:
        A: Square matrix (n×n)
        
    Returns:
        Inverse matrix A^(-1)
        
    Raises:
        ValueError: If matrix is singular or not square
    """
    A = np.array(A, dtype=float)
    
    if A.shape[0] != A.shape[1]:
        raise ValueError(f"Matrix inverse requires square matrix, got {A.shape}")
    
    det = matrix_determinant(A)
    if abs(det) < 1e-10:
        raise ValueError(f"Matrix is singular (det ≈ {det}), cannot invert")
    
    return np.linalg.inv(A)


def matrix_rank(A: Union[list, np.ndarray]) -> int:
    """Compute the rank of a matrix.
    
    Rank is the dimension of the column/row space, indicating how many
    linearly independent rows or columns exist.
    
    Args:
        A: Input matrix
        
    Returns:
        Rank of the matrix
    """
    A = np.array(A, dtype=float)
    return int(np.linalg.matrix_rank(A))


def matrix_trace(A: Union[list, np.ndarray]) -> float:
    """Compute trace of a square matrix.
    
    Trace is the sum of diagonal elements: tr(A) = Σ A[i,i]
    
    Args:
        A: Square matrix
        
    Returns:
        Trace value
        
    Raises:
        ValueError: If matrix is not square
    """
    A = np.array(A, dtype=float)
    
    if A.shape[0] != A.shape[1]:
        raise ValueError(f"Trace requires square matrix, got {A.shape}")
    
    return float(np.trace(A))


def solve_linear_system(A: Union[list, np.ndarray], b: Union[list, np.ndarray]) -> np.ndarray:
    """Solve linear system A*x = b for x.
    
    Uses efficient Gaussian elimination via NumPy.
    
    Args:
        A: Coefficient matrix (n×n)
        b: Right-hand side vector (n,) or (n×m)
        
    Returns:
        Solution vector(s)
        
    Raises:
        ValueError: If system is singular
    """
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    
    if A.shape[0] != A.shape[1]:
        raise ValueError(f"Coefficient matrix must be square, got {A.shape}")
    
    if abs(matrix_determinant(A)) < 1e-10:
        raise ValueError("System matrix is singular, no unique solution")
    
    return np.linalg.solve(A, b)


def matrix_norm(A: Union[list, np.ndarray], norm_type: str = 'frobenius') -> float:
    """Compute norm of a matrix.
    
    Supported norms:
    - 'frobenius': ||A||_F = √(Σ A[i,j]²)
    - 'spectral': ||A||_2 = largest singular value
    - 'max': ||A||_∞ = max row sum (absolute values)
    
    Args:
        A: Input matrix
        norm_type: Type of norm ('frobenius', 'spectral', 'max')
        
    Returns:
        Norm value
    """
    A = np.array(A, dtype=float)
    
    if norm_type == 'frobenius':
        return float(np.linalg.norm(A, 'fro'))
    elif norm_type == 'spectral':
        return float(np.linalg.norm(A, 2))
    elif norm_type == 'max':
        return float(np.max(np.sum(np.abs(A), axis=1)))
    else:
        raise ValueError(f"Unknown norm type: {norm_type}")


def matrix_condition_number(A: Union[list, np.ndarray]) -> float:
    """Compute condition number of a matrix.
    
    Condition number measures numerical stability: high values indicate
    ill-conditioned systems prone to numerical errors.
    
    Args:
        A: Input matrix
        
    Returns:
        Condition number (cond = ||A|| * ||A^(-1)||)
    """
    A = np.array(A, dtype=float)
    return float(np.linalg.cond(A))


def eigenvalue_decomposition(A: Union[list, np.ndarray]) -> Tuple[np.ndarray, np.ndarray]:
    """Compute eigenvalues and eigenvectors.
    
    For square matrix A: A*v = λ*v where λ are eigenvalues, v are eigenvectors.
    
    Args:
        A: Square matrix
        
    Returns:
        Tuple of (eigenvalues, eigenvectors)
        - eigenvalues: 1D array of eigenvalues
        - eigenvectors: 2D array, columns are eigenvectors
        
    Raises:
        ValueError: If matrix is not square
    """
    A = np.array(A, dtype=float)
    
    if A.shape[0] != A.shape[1]:
        raise ValueError(f"Eigenvalue decomposition requires square matrix, got {A.shape}")
    
    eigenvalues, eigenvectors = np.linalg.eig(A)
    return eigenvalues, eigenvectors


def singular_value_decomposition(A: Union[list, np.ndarray]) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute Singular Value Decomposition (SVD).
    
    Decomposes A into: A = U * Σ * V^T where:
    - U: Left singular vectors (orthogonal)
    - Σ: Singular values (diagonal)
    - V^T: Transpose of right singular vectors
    
    Args:
        A: Input matrix (m×n)
        
    Returns:
        Tuple of (U, s, Vh) where:
        - U: Left singular vectors (m×k)
        - s: Singular values (k,)
        - Vh: Transpose of right singular vectors (k×n)
    """
    A = np.array(A, dtype=float)
    U, s, Vh = np.linalg.svd(A, full_matrices=False)
    return U, s, Vh


def qr_decomposition(A: Union[list, np.ndarray]) -> Tuple[np.ndarray, np.ndarray]:
    """Compute QR decomposition.
    
    Decomposes A into: A = Q * R where:
    - Q: Orthogonal matrix
    - R: Upper triangular matrix
    
    Args:
        A: Input matrix (m×n)
        
    Returns:
        Tuple of (Q, R)
    """
    A = np.array(A, dtype=float)
    Q, R = np.linalg.qr(A)
    return Q, R


def matrix_pseudo_inverse(A: Union[list, np.ndarray]) -> np.ndarray:
    """Compute Moore-Penrose pseudo-inverse.
    
    The pseudo-inverse A^+ is the generalized inverse that works for
    non-square or singular matrices.
    
    Args:
        A: Input matrix
        
    Returns:
        Pseudo-inverse matrix
    """
    A = np.array(A, dtype=float)
    return np.linalg.pinv(A)


def is_symmetric(A: Union[list, np.ndarray], tolerance: float = 1e-9) -> bool:
    """Check if matrix is symmetric.
    
    A matrix is symmetric if A = A^T
    
    Args:
        A: Input matrix
        tolerance: Numerical tolerance for comparison
        
    Returns:
        True if matrix is symmetric
    """
    A = np.array(A, dtype=float)
    return np.allclose(A, A.T, atol=tolerance)


def is_orthogonal(A: Union[list, np.ndarray], tolerance: float = 1e-9) -> bool:
    """Check if matrix is orthogonal.
    
    A matrix is orthogonal if A * A^T = I
    
    Args:
        A: Input matrix
        tolerance: Numerical tolerance for comparison
        
    Returns:
        True if matrix is orthogonal
    """
    A = np.array(A, dtype=float)
    product = matrix_multiply(A, matrix_transpose(A))
    return np.allclose(product, identity_matrix(A.shape[0]), atol=tolerance)


def is_positive_definite(A: Union[list, np.ndarray]) -> bool:
    """Check if matrix is positive definite.
    
    A symmetric matrix is positive definite if all eigenvalues are positive.
    
    Args:
        A: Input matrix
        
    Returns:
        True if matrix is positive definite
    """
    A = np.array(A, dtype=float)
    
    try:
        np.linalg.cholesky(A)
        return True
    except np.linalg.LinAlgError:
        return False
