"""Unit tests for transformations module."""

import pytest
import math
import numpy as np
from src import transformations


class TestRotationMatrix2D:
    """Test 2D rotation matrix."""
    
    def test_rotation_90_degrees(self):
        """Test 90-degree rotation."""
        R = transformations.rotation_matrix_2d(math.pi / 2)
        # Rotate [1, 0] by 90 degrees should give [0, 1]
        v = np.array([1, 0])
        result = np.dot(R, v)
        expected = np.array([0, 1])
        np.testing.assert_array_almost_equal(result, expected)
    
    def test_rotation_is_orthogonal(self):
        """Test that rotation matrix is orthogonal."""
        R = transformations.rotation_matrix_2d(0.5)
        product = np.dot(R.T, R)
        expected = np.eye(2)
        np.testing.assert_array_almost_equal(product, expected)


class TestTransformationMatrix2D:
    """Test 2D homogeneous transformation matrix."""
    
    def test_transformation_applies_rotation_and_translation(self):
        """Test that transformation applies both rotation and translation."""
        T = transformations.transformation_matrix_2d(0, 2, 3)  # 0 rotation, translate by (2,3)
        point = np.array([1, 0])
        transformed = transformations.apply_transformation_2d(T, point)
        expected = np.array([3, 3])
        np.testing.assert_array_almost_equal(transformed, expected)


class TestRotationMatrix3D:
    """Test 3D rotation matrices."""
    
    def test_rotation_x_axis(self):
        """Test rotation about X axis."""
        R = transformations.rotation_matrix_3d_x(math.pi / 2)
        # Rotate [0, 1, 0] by 90 degrees about X should give [0, 0, 1]
        v = np.array([0, 1, 0])
        result = np.dot(R, v)
        expected = np.array([0, 0, 1])
        np.testing.assert_array_almost_equal(result, expected)
    
    def test_rotation_y_axis(self):
        """Test rotation about Y axis."""
        R = transformations.rotation_matrix_3d_y(math.pi / 2)
        # Rotate [1, 0, 0] by 90 degrees about Y should give [0, 0, -1]
        v = np.array([1, 0, 0])
        result = np.dot(R, v)
        expected = np.array([0, 0, -1])
        np.testing.assert_array_almost_equal(result, expected)
    
    def test_rotation_z_axis(self):
        """Test rotation about Z axis."""
        R = transformations.rotation_matrix_3d_z(math.pi / 2)
        # Rotate [1, 0, 0] by 90 degrees about Z should give [0, 1, 0]
        v = np.array([1, 0, 0])
        result = np.dot(R, v)
        expected = np.array([0, 1, 0])
        np.testing.assert_array_almost_equal(result, expected)


class TestEulerAngles:
    """Test Euler angle conversions."""
    
    def test_euler_to_rotation_zyx(self):
        """Test Euler angles to rotation matrix (ZYX order)."""
        roll, pitch, yaw = 0, 0, math.pi / 2
        R = transformations.euler_angles_to_rotation_matrix(roll, pitch, yaw, order='ZYX')
        # Should rotate [1, 0, 0] to [0, 1, 0]
        v = np.array([1, 0, 0])
        result = np.dot(R, v)
        expected = np.array([0, 1, 0])
        np.testing.assert_array_almost_equal(result, expected)
    
    def test_euler_round_trip(self):
        """Test converting Euler angles to matrix and back."""
        roll_orig, pitch_orig, yaw_orig = 0.1, 0.2, 0.3
        R = transformations.euler_angles_to_rotation_matrix(roll_orig, pitch_orig, yaw_orig)
        roll, pitch, yaw = transformations.rotation_matrix_to_euler_angles(R)
        
        # Should recover original angles
        assert abs(roll - roll_orig) < 1e-9
        assert abs(pitch - pitch_orig) < 1e-9
        assert abs(yaw - yaw_orig) < 1e-9


class TestAxisAngle:
    """Test axis-angle representation."""
    
    def test_axis_angle_to_rotation(self):
        """Test axis-angle to rotation matrix."""
        axis = [0, 0, 1]  # Z axis
        angle = math.pi / 2
        R = transformations.axis_angle_to_rotation_matrix(axis, angle)
        # Should be same as Rz(pi/2)
        v = np.array([1, 0, 0])
        result = np.dot(R, v)
        expected = np.array([0, 1, 0])
        np.testing.assert_array_almost_equal(result, expected)


class TestHomogeneousTransformation:
    """Test homogeneous transformation matrices."""
    
    def test_homogeneous_transformation_3d(self):
        """Test creating 3D homogeneous transformation."""
        R = np.eye(3)
        t = [1, 2, 3]
        T = transformations.homogeneous_transformation_matrix_3d(R, t)
        
        # Check structure
        assert T.shape == (4, 4)
        np.testing.assert_array_almost_equal(T[0:3, 0:3], R)
        np.testing.assert_array_almost_equal(T[0:3, 3], t)
        np.testing.assert_array_almost_equal(T[3, :], [0, 0, 0, 1])
    
    def test_apply_transformation_3d(self):
        """Test applying 3D transformation."""
        R = np.eye(3)
        t = [1, 2, 3]
        T = transformations.homogeneous_transformation_matrix_3d(R, t)
        point = [0, 0, 0]
        
        transformed = transformations.apply_transformation_3d(T, point)
        expected = np.array([1, 2, 3])
        np.testing.assert_array_almost_equal(transformed, expected)


class TestTransformationComposition:
    """Test composing transformations."""
    
    def test_compose_transformations_2d(self):
        """Test composing 2D transformations."""
        T1 = transformations.transformation_matrix_2d(0, 1, 0)
        T2 = transformations.transformation_matrix_2d(0, 1, 0)
        T_combined = transformations.compose_transformations_2d(T1, T2)
        
        # Applying T_combined should be same as T1 then T2
        point = [0, 0]
        result1 = transformations.apply_transformation_2d(T2, 
                  transformations.apply_transformation_2d(T1, point))
        result2 = transformations.apply_transformation_2d(T_combined, point)
        np.testing.assert_array_almost_equal(result1, result2)


class TestTransformationInverse:
    """Test computing transformation inverses."""
    
    def test_inverse_2d(self):
        """Test 2D transformation inverse."""
        T = transformations.transformation_matrix_2d(math.pi / 4, 1, 2)
        T_inv = transformations.inverse_transformation_2d(T)
        
        # T * T_inv should be identity
        product = np.dot(T, T_inv)
        expected = np.eye(3)
        np.testing.assert_array_almost_equal(product, expected)
    
    def test_inverse_3d(self):
        """Test 3D transformation inverse."""
        R = transformations.rotation_matrix_3d_z(0.5)
        t = [1, 2, 3]
        T = transformations.homogeneous_transformation_matrix_3d(R, t)
        T_inv = transformations.inverse_transformation_3d(T)
        
        # T * T_inv should be identity
        product = np.dot(T, T_inv)
        expected = np.eye(4)
        np.testing.assert_array_almost_equal(product, expected)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
