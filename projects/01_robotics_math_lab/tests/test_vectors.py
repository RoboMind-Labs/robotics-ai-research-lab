"""Unit tests for vector operations module.

Tests all vector operations including basic arithmetic, geometric
operations, and edge cases.
"""

import pytest
import math
import numpy as np
from src import vectors


class TestVectorCreation:
    """Test vector creation."""
    
    def test_create_vector(self):
        """Test basic vector creation."""
        v = vectors.create_vector([1, 2, 3])
        assert v.shape == (3,)
        np.testing.assert_array_almost_equal(v, [1, 2, 3])
    
    def test_create_vector_from_array(self):
        """Test creating vector from NumPy array."""
        arr = np.array([1, 2, 3])
        v = vectors.create_vector(arr)
        np.testing.assert_array_almost_equal(v, arr)


class TestVectorArithmetic:
    """Test vector arithmetic operations."""
    
    def test_add_vectors(self):
        """Test vector addition."""
        v1 = [1, 2, 3]
        v2 = [4, 5, 6]
        result = vectors.add_vectors(v1, v2)
        expected = np.array([5, 7, 9])
        np.testing.assert_array_almost_equal(result, expected)
    
    def test_add_vectors_dimension_mismatch(self):
        """Test that adding vectors of different dimensions raises error."""
        v1 = [1, 2]
        v2 = [1, 2, 3]
        with pytest.raises(ValueError):
            vectors.add_vectors(v1, v2)
    
    def test_subtract_vectors(self):
        """Test vector subtraction."""
        v1 = [5, 7, 9]
        v2 = [1, 2, 3]
        result = vectors.subtract_vectors(v1, v2)
        expected = np.array([4, 5, 6])
        np.testing.assert_array_almost_equal(result, expected)
    
    def test_scale_vector(self):
        """Test scalar multiplication."""
        v = [1, 2, 3]
        scaled = vectors.scale_vector(v, 2)
        expected = np.array([2, 4, 6])
        np.testing.assert_array_almost_equal(scaled, expected)
    
    def test_scale_vector_zero(self):
        """Test scaling by zero."""
        v = [1, 2, 3]
        scaled = vectors.scale_vector(v, 0)
        expected = np.array([0, 0, 0])
        np.testing.assert_array_almost_equal(scaled, expected)


class TestDotProduct:
    """Test dot product operations."""
    
    def test_dot_product_basic(self):
        """Test basic dot product."""
        v1 = [1, 0, 0]
        v2 = [0, 1, 0]
        dot = vectors.dot_product(v1, v2)
        assert abs(dot) < 1e-10
    
    def test_dot_product_parallel(self):
        """Test dot product of parallel vectors."""
        v1 = [1, 0, 0]
        v2 = [2, 0, 0]
        dot = vectors.dot_product(v1, v2)
        assert abs(dot - 2.0) < 1e-10
    
    def test_dot_product_self(self):
        """Test dot product of vector with itself."""
        v = [3, 4]
        dot = vectors.dot_product(v, v)
        assert abs(dot - 25.0) < 1e-10  # 3^2 + 4^2 = 25


class TestCrossProduct:
    """Test cross product operations."""
    
    def test_cross_product_basic(self):
        """Test basic cross product."""
        v1 = [1, 0, 0]
        v2 = [0, 1, 0]
        cross = vectors.cross_product(v1, v2)
        expected = np.array([0, 0, 1])
        np.testing.assert_array_almost_equal(cross, expected)
    
    def test_cross_product_anticommutative(self):
        """Test that cross product is anti-commutative."""
        v1 = [1, 2, 3]
        v2 = [4, 5, 6]
        cross1 = vectors.cross_product(v1, v2)
        cross2 = vectors.cross_product(v2, v1)
        np.testing.assert_array_almost_equal(cross1, -cross2)
    
    def test_cross_product_2d_fails(self):
        """Test that 2D vectors raise error."""
        v1 = [1, 2]
        v2 = [3, 4]
        with pytest.raises(ValueError):
            vectors.cross_product(v1, v2)


class TestVectorNorms:
    """Test vector norm calculations."""
    
    def test_l2_norm(self):
        """Test L2 (Euclidean) norm."""
        v = [3, 4]
        norm = vectors.vector_norm(v, order=2)
        assert abs(norm - 5.0) < 1e-10
    
    def test_l1_norm(self):
        """Test L1 norm."""
        v = [1, 2, 3]
        norm = vectors.vector_norm(v, order=1)
        assert abs(norm - 6.0) < 1e-10
    
    def test_inf_norm(self):
        """Test infinity norm."""
        v = [1, -5, 3]
        norm = vectors.vector_norm(v, order=float('inf'))
        assert abs(norm - 5.0) < 1e-10
    
    def test_normalize_vector(self):
        """Test vector normalization."""
        v = [3, 4]
        normalized = vectors.normalize_vector(v)
        norm = vectors.vector_norm(normalized)
        assert abs(norm - 1.0) < 1e-10
    
    def test_normalize_zero_vector_fails(self):
        """Test that normalizing zero vector raises error."""
        v = [0, 0, 0]
        with pytest.raises(ValueError):
            vectors.normalize_vector(v)


class TestVectorAngles:
    """Test angle computations."""
    
    def test_angle_between_perpendicular(self):
        """Test angle between perpendicular vectors."""
        v1 = [1, 0, 0]
        v2 = [0, 1, 0]
        angle = vectors.angle_between_vectors(v1, v2)
        assert abs(angle - math.pi/2) < 1e-10
    
    def test_angle_between_parallel(self):
        """Test angle between parallel vectors."""
        v1 = [1, 0, 0]
        v2 = [2, 0, 0]
        angle = vectors.angle_between_vectors(v1, v2)
        assert abs(angle) < 1e-10
    
    def test_angle_between_antiparallel(self):
        """Test angle between anti-parallel vectors."""
        v1 = [1, 0, 0]
        v2 = [-1, 0, 0]
        angle = vectors.angle_between_vectors(v1, v2)
        assert abs(angle - math.pi) < 1e-10


class TestDistance:
    """Test distance calculations."""
    
    def test_distance_basic(self):
        """Test basic distance calculation."""
        p1 = [0, 0, 0]
        p2 = [3, 4, 0]
        dist = vectors.distance_between_points(p1, p2)
        assert abs(dist - 5.0) < 1e-10


class TestProjection:
    """Test projection operations."""
    
    def test_projection_onto_vector(self):
        """Test projecting one vector onto another."""
        v = [3, 4]
        u = [1, 0]
        proj = vectors.projection_onto_vector(v, u)
        expected = np.array([3, 0])
        np.testing.assert_array_almost_equal(proj, expected)
    
    def test_perpendicular_component(self):
        """Test perpendicular component."""
        v = [3, 4]
        u = [1, 0]
        perp = vectors.perpendicular_component(v, u)
        expected = np.array([0, 4])
        np.testing.assert_array_almost_equal(perp, expected)


class TestOrthogonality:
    """Test orthogonality checks."""
    
    def test_are_perpendicular_true(self):
        """Test perpendicularity check - true case."""
        v1 = [1, 0, 0]
        v2 = [0, 1, 0]
        assert vectors.are_perpendicular(v1, v2)
    
    def test_are_perpendicular_false(self):
        """Test perpendicularity check - false case."""
        v1 = [1, 0, 0]
        v2 = [1, 1, 0]
        assert not vectors.are_perpendicular(v1, v2)
    
    def test_are_parallel_true(self):
        """Test parallel check - true case."""
        v1 = [1, 2, 3]
        v2 = [2, 4, 6]
        assert vectors.are_parallel(v1, v2)
    
    def test_are_parallel_antiparallel(self):
        """Test parallel check - anti-parallel case."""
        v1 = [1, 2, 3]
        v2 = [-1, -2, -3]
        assert vectors.are_parallel(v1, v2)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
