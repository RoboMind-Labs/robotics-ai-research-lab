"""Unit tests for matrix operations module."""

import pytest
import numpy as np
from src import matrices


class TestMatrixCreation:
    """Test matrix creation and initialization."""
    
    def test_create_matrix(self):
        """Test creating a matrix."""
        M = matrices.create_matrix(2, 3)
        assert M.shape == (2, 3)
        assert np.all(M == 0)
    
    def test_identity_matrix(self):
        """Test identity matrix creation."""
        I = matrices.identity_matrix(3)
        expected = np.eye(3)
        np.testing.assert_array_almost_equal(I, expected)


class TestMatrixMultiplication:
    """Test matrix multiplication."""
    
    def test_multiply_basic(self):
        """Test basic matrix multiplication."""
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        C = matrices.matrix_multiply(A, B)
        expected = np.array([[19, 22], [43, 50]])
        np.testing.assert_array_almost_equal(C, expected)
    
    def test_multiply_dimension_mismatch(self):
        """Test that dimension mismatch raises error."""
        A = [[1, 2, 3]]
        B = [[4, 5]]
        with pytest.raises(ValueError):
            matrices.matrix_multiply(A, B)
    
    def test_multiply_rectangular(self):
        """Test multiplication of rectangular matrices."""
        A = [[1, 2, 3]]  # 1x3
        B = [[4], [5], [6]]  # 3x1
        C = matrices.matrix_multiply(A, B)
        expected = np.array([[32]])
        np.testing.assert_array_almost_equal(C, expected)


class TestMatrixTranspose:
    """Test matrix transpose."""
    
    def test_transpose_square(self):
        """Test transposing square matrix."""
        A = [[1, 2], [3, 4]]
        AT = matrices.matrix_transpose(A)
        expected = np.array([[1, 3], [2, 4]])
        np.testing.assert_array_almost_equal(AT, expected)
    
    def test_transpose_rectangular(self):
        """Test transposing rectangular matrix."""
        A = [[1, 2, 3], [4, 5, 6]]
        AT = matrices.matrix_transpose(A)
        assert AT.shape == (3, 2)


class TestMatrixDeterminant:
    """Test determinant calculation."""
    
    def test_determinant_2x2(self):
        """Test 2×2 determinant."""
        A = [[1, 2], [3, 4]]
        det = matrices.matrix_determinant(A)
        assert abs(det - (-2)) < 1e-10
    
    def test_determinant_identity(self):
        """Test determinant of identity matrix."""
        I = matrices.identity_matrix(3)
        det = matrices.matrix_determinant(I)
        assert abs(det - 1.0) < 1e-10
    
    def test_determinant_non_square(self):
        """Test that non-square matrix raises error."""
        A = [[1, 2, 3], [4, 5, 6]]
        with pytest.raises(ValueError):
            matrices.matrix_determinant(A)


class TestMatrixInverse:
    """Test matrix inversion."""
    
    def test_inverse_basic(self):
        """Test basic matrix inversion."""
        A = [[1, 2], [3, 4]]
        A_inv = matrices.matrix_inverse(A)
        product = matrices.matrix_multiply(A, A_inv)
        expected = matrices.identity_matrix(2)
        np.testing.assert_array_almost_equal(product, expected)
    
    def test_inverse_singular_fails(self):
        """Test that singular matrix raises error."""
        A = [[1, 2], [2, 4]]  # Singular (det = 0)
        with pytest.raises(ValueError):
            matrices.matrix_inverse(A)


class TestMatrixRank:
    """Test matrix rank."""
    
    def test_rank_full(self):
        """Test rank of full rank matrix."""
        A = [[1, 0], [0, 1]]
        rank = matrices.matrix_rank(A)
        assert rank == 2
    
    def test_rank_deficient(self):
        """Test rank of rank-deficient matrix."""
        A = [[1, 2], [2, 4]]
        rank = matrices.matrix_rank(A)
        assert rank == 1


class TestMatrixTrace:
    """Test matrix trace."""
    
    def test_trace_basic(self):
        """Test basic trace calculation."""
        A = [[1, 2], [3, 4]]
        trace = matrices.matrix_trace(A)
        assert abs(trace - 5.0) < 1e-10
    
    def test_trace_identity(self):
        """Test trace of identity matrix."""
        I = matrices.identity_matrix(3)
        trace = matrices.matrix_trace(I)
        assert abs(trace - 3.0) < 1e-10


class TestLinearSystemSolving:
    """Test linear system solving."""
    
    def test_solve_basic(self):
        """Test solving linear system."""
        A = [[2, 1], [1, 3]]
        b = [8, 13]
        x = matrices.solve_linear_system(A, b)
        # Verify: A*x = b
        result = np.dot(A, x)
        np.testing.assert_array_almost_equal(result, b)
    
    def test_solve_singular_fails(self):
        """Test that singular system raises error."""
        A = [[1, 2], [2, 4]]
        b = [1, 2]
        with pytest.raises(ValueError):
            matrices.solve_linear_system(A, b)


class TestMatrixNorms:
    """Test matrix norms."""
    
    def test_frobenius_norm(self):
        """Test Frobenius norm."""
        A = [[1, 2], [3, 4]]
        norm = matrices.matrix_norm(A, 'frobenius')
        expected = np.sqrt(1 + 4 + 9 + 16)  # sqrt(30)
        assert abs(norm - expected) < 1e-10


class TestMatrixProperties:
    """Test matrix property checks."""
    
    def test_is_symmetric(self):
        """Test symmetric matrix check."""
        A = [[1, 2], [2, 3]]
        assert matrices.is_symmetric(A)
    
    def test_is_symmetric_false(self):
        """Test non-symmetric matrix."""
        A = [[1, 2], [3, 4]]
        assert not matrices.is_symmetric(A)
    
    def test_is_orthogonal(self):
        """Test orthogonal matrix check."""
        A = [[1, 0], [0, 1]]
        assert matrices.is_orthogonal(A)
    
    def test_is_positive_definite(self):
        """Test positive definite check."""
        A = [[2, 0], [0, 2]]
        assert matrices.is_positive_definite(A)


class TestMatrixDecompositions:
    """Test matrix decompositions."""
    
    def test_eigenvalue_decomposition(self):
        """Test eigenvalue decomposition."""
        A = [[4, -2], [-2, 1]]
        eigenvalues, eigenvectors = matrices.eigenvalue_decomposition(A)
        
        # Test: A*v = λ*v for each eigenpair
        for i, lam in enumerate(eigenvalues):
            v = eigenvectors[:, i]
            Av = np.dot(A, v)
            lam_v = lam * v
            np.testing.assert_array_almost_equal(Av, lam_v)
    
    def test_svd(self):
        """Test Singular Value Decomposition."""
        A = [[1, 2], [3, 4], [5, 6]]
        U, s, Vh = matrices.singular_value_decomposition(A)
        
        # Reconstruct and verify
        reconstructed = U @ np.diag(s) @ Vh
        np.testing.assert_array_almost_equal(reconstructed, A, decimal=10)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
