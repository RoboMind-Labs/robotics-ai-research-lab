"""Transformation module for 2D and 3D rotations and homogeneous transformations.

This module provides rotation matrices, transformation composition, and
conversions between different rotation representations (Euler angles,
axis-angle, quaternions).

Author: Robotics AI Research Lab
"""

from typing import Union, Tuple
import numpy as np
import math


def rotation_matrix_2d(angle: float) -> np.ndarray:
    """Create 2D rotation matrix.
    
    Rotates points counter-clockwise by angle θ:
    R(θ) = [cos(θ) -sin(θ)]
           [sin(θ)  cos(θ)]
    
    Args:
        angle: Rotation angle in radians
        
    Returns:
        2×2 rotation matrix
    """
    c = math.cos(angle)
    s = math.sin(angle)
    return np.array([
        [c, -s],
        [s,  c]
    ], dtype=float)


def transformation_matrix_2d(angle: float, tx: float, ty: float) -> np.ndarray:
    """Create 2D homogeneous transformation matrix.
    
    Combines rotation and translation:
    T = [R   t]
        [0   1]
    where R is 2×2 rotation, t is 2×1 translation
    
    Args:
        angle: Rotation angle in radians
        tx: Translation in x
        ty: Translation in y
        
    Returns:
        3×3 homogeneous transformation matrix
    """
    R = rotation_matrix_2d(angle)
    T = np.eye(3, dtype=float)
    T[0:2, 0:2] = R
    T[0:2, 2] = [tx, ty]
    return T


def rotation_matrix_3d_x(angle: float) -> np.ndarray:
    """Create 3D rotation matrix about X axis.
    
    Rx(θ) = [1    0       0    ]
            [0  cos(θ) -sin(θ)]
            [0  sin(θ)  cos(θ)]
    
    Args:
        angle: Rotation angle in radians
        
    Returns:
        3×3 rotation matrix
    """
    c = math.cos(angle)
    s = math.sin(angle)
    return np.array([
        [1, 0,  0],
        [0, c, -s],
        [0, s,  c]
    ], dtype=float)


def rotation_matrix_3d_y(angle: float) -> np.ndarray:
    """Create 3D rotation matrix about Y axis.
    
    Ry(θ) = [ cos(θ) 0 sin(θ)]
            [   0    1   0   ]
            [-sin(θ) 0 cos(θ)]
    
    Args:
        angle: Rotation angle in radians
        
    Returns:
        3×3 rotation matrix
    """
    c = math.cos(angle)
    s = math.sin(angle)
    return np.array([
        [ c, 0, s],
        [ 0, 1, 0],
        [-s, 0, c]
    ], dtype=float)


def rotation_matrix_3d_z(angle: float) -> np.ndarray:
    """Create 3D rotation matrix about Z axis.
    
    Rz(θ) = [cos(θ) -sin(θ) 0]
            [sin(θ)  cos(θ) 0]
            [  0       0    1]
    
    Args:
        angle: Rotation angle in radians
        
    Returns:
        3×3 rotation matrix
    """
    c = math.cos(angle)
    s = math.sin(angle)
    return np.array([
        [c, -s, 0],
        [s,  c, 0],
        [0,  0, 1]
    ], dtype=float)


def euler_angles_to_rotation_matrix(roll: float, pitch: float, yaw: float, 
                                   order: str = 'ZYX') -> np.ndarray:
    """Convert Euler angles to rotation matrix.
    
    Supports different rotation orders:
    - 'ZYX': R = Rz(yaw) * Ry(pitch) * Rx(roll) [common in robotics]
    - 'XYZ': R = Rx(roll) * Ry(pitch) * Rz(yaw)
    
    Args:
        roll: Rotation about X axis (radians)
        pitch: Rotation about Y axis (radians)
        yaw: Rotation about Z axis (radians)
        order: Rotation order ('ZYX' or 'XYZ')
        
    Returns:
        3×3 rotation matrix
    """
    Rx = rotation_matrix_3d_x(roll)
    Ry = rotation_matrix_3d_y(pitch)
    Rz = rotation_matrix_3d_z(yaw)
    
    if order == 'ZYX':
        return np.dot(Rz, np.dot(Ry, Rx))
    elif order == 'XYZ':
        return np.dot(Rx, np.dot(Ry, Rz))
    else:
        raise ValueError(f"Unknown Euler angle order: {order}")


def rotation_matrix_to_euler_angles(R: np.ndarray, order: str = 'ZYX') -> Tuple[float, float, float]:
    """Convert rotation matrix to Euler angles.
    
    Extracts roll, pitch, yaw from rotation matrix.
    Note: Singular configurations may give discontinuous results.
    
    Args:
        R: 3×3 rotation matrix
        order: Rotation order ('ZYX' or 'XYZ')
        
    Returns:
        Tuple of (roll, pitch, yaw) in radians
    """
    R = np.array(R, dtype=float)
    
    if order == 'ZYX':
        # From R = Rz(yaw) * Ry(pitch) * Rx(roll)
        pitch = math.asin(-R[2, 0])
        if abs(math.cos(pitch)) > 1e-6:
            roll = math.atan2(R[2, 1], R[2, 2])
            yaw = math.atan2(R[1, 0], R[0, 0])
        else:
            # Singular configuration
            roll = 0
            yaw = math.atan2(-R[0, 1], R[1, 1])
    elif order == 'XYZ':
        # From R = Rx(roll) * Ry(pitch) * Rz(yaw)
        pitch = math.asin(R[0, 2])
        if abs(math.cos(pitch)) > 1e-6:
            roll = math.atan2(-R[1, 2], R[2, 2])
            yaw = math.atan2(-R[0, 1], R[0, 0])
        else:
            # Singular configuration
            roll = 0
            yaw = math.atan2(R[1, 0], R[1, 1])
    else:
        raise ValueError(f"Unknown Euler angle order: {order}")
    
    return roll, pitch, yaw


def axis_angle_to_rotation_matrix(axis: Union[list, np.ndarray], angle: float) -> np.ndarray:
    """Convert axis-angle representation to rotation matrix.
    
    Uses Rodrigues' rotation formula:
    R = I + sin(θ)*[axis]_x + (1-cos(θ))*[axis]_x²
    
    Args:
        axis: Unit rotation axis (3D vector)
        angle: Rotation angle in radians
        
    Returns:
        3×3 rotation matrix
    """
    axis = np.array(axis, dtype=float)
    axis = axis / np.linalg.norm(axis)  # Normalize
    
    # Skew-symmetric matrix of axis
    K = np.array([
        [0, -axis[2], axis[1]],
        [axis[2], 0, -axis[0]],
        [-axis[1], axis[0], 0]
    ], dtype=float)
    
    # Rodrigues formula
    R = np.eye(3) + np.sin(angle) * K + (1 - np.cos(angle)) * np.dot(K, K)
    return R


def rotation_matrix_to_axis_angle(R: np.ndarray) -> Tuple[np.ndarray, float]:
    """Convert rotation matrix to axis-angle representation.
    
    Args:
        R: 3×3 rotation matrix
        
    Returns:
        Tuple of (axis, angle) where axis is unit vector and angle is radians
    """
    R = np.array(R, dtype=float)
    
    angle = math.acos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    
    if abs(angle) < 1e-6:
        # Identity rotation
        axis = np.array([1, 0, 0])
    elif abs(angle - np.pi) < 1e-6:
        # 180 degree rotation
        diagonal = np.diag(R)
        idx = np.argmax(diagonal + 1)
        axis = np.zeros(3)
        axis[idx] = math.sqrt((R[idx, idx] + 1) / 2)
        if idx == 0:
            axis[1] = R[0, 1] / (2 * axis[0])
            axis[2] = R[0, 2] / (2 * axis[0])
        elif idx == 1:
            axis[0] = R[1, 0] / (2 * axis[1])
            axis[2] = R[1, 2] / (2 * axis[1])
        else:
            axis[0] = R[2, 0] / (2 * axis[2])
            axis[1] = R[2, 1] / (2 * axis[2])
    else:
        # General case: extract from skew-symmetric part
        axis = np.array([
            R[2, 1] - R[1, 2],
            R[0, 2] - R[2, 0],
            R[1, 0] - R[0, 1]
        ]) / (2 * math.sin(angle))
    
    axis = axis / np.linalg.norm(axis)
    return axis, angle


def homogeneous_transformation_matrix_3d(R: np.ndarray, t: Union[list, np.ndarray]) -> np.ndarray:
    """Create 3D homogeneous transformation matrix.
    
    Combines 3×3 rotation matrix and 3×1 translation vector:
    T = [R   t]
        [0   1]
    
    Args:
        R: 3×3 rotation matrix
        t: 3×1 translation vector
        
    Returns:
        4×4 homogeneous transformation matrix
    """
    R = np.array(R, dtype=float)
    t = np.array(t, dtype=float)
    
    T = np.eye(4, dtype=float)
    T[0:3, 0:3] = R
    T[0:3, 3] = t
    return T


def apply_transformation_2d(T: np.ndarray, point: Union[list, np.ndarray]) -> np.ndarray:
    """Apply 2D homogeneous transformation to a point.
    
    Args:
        T: 3×3 transformation matrix
        point: 2D point (x, y)
        
    Returns:
        Transformed 2D point
    """
    point = np.array(point, dtype=float)
    point_h = np.append(point, 1)  # Homogeneous coordinates
    transformed_h = np.dot(T, point_h)
    return transformed_h[:2]


def apply_transformation_3d(T: np.ndarray, point: Union[list, np.ndarray]) -> np.ndarray:
    """Apply 3D homogeneous transformation to a point.
    
    Args:
        T: 4×4 transformation matrix
        point: 3D point (x, y, z)
        
    Returns:
        Transformed 3D point
    """
    point = np.array(point, dtype=float)
    point_h = np.append(point, 1)  # Homogeneous coordinates
    transformed_h = np.dot(T, point_h)
    return transformed_h[:3]


def compose_transformations_2d(T1: np.ndarray, T2: np.ndarray) -> np.ndarray:
    """Compose two 2D transformations.
    
    Applies T1 first, then T2: T_total = T2 * T1
    
    Args:
        T1: First 3×3 transformation
        T2: Second 3×3 transformation
        
    Returns:
        Composed transformation T2 * T1
    """
    return np.dot(T2, T1)


def compose_transformations_3d(T1: np.ndarray, T2: np.ndarray) -> np.ndarray:
    """Compose two 3D transformations.
    
    Applies T1 first, then T2: T_total = T2 * T1
    
    Args:
        T1: First 4×4 transformation
        T2: Second 4×4 transformation
        
    Returns:
        Composed transformation T2 * T1
    """
    return np.dot(T2, T1)


def inverse_transformation_2d(T: np.ndarray) -> np.ndarray:
    """Compute inverse of 2D homogeneous transformation.
    
    Args:
        T: 3×3 transformation matrix
        
    Returns:
        Inverse transformation T^(-1)
    """
    T = np.array(T, dtype=float)
    T_inv = np.linalg.inv(T)
    return T_inv


def inverse_transformation_3d(T: np.ndarray) -> np.ndarray:
    """Compute inverse of 3D homogeneous transformation.
    
    For T = [R t; 0 1], the inverse is efficiently computed as:
    T^(-1) = [R^T -R^T*t; 0 1]
    
    Args:
        T: 4×4 transformation matrix
        
    Returns:
        Inverse transformation T^(-1)
    """
    T = np.array(T, dtype=float)
    
    R = T[0:3, 0:3]
    t = T[0:3, 3]
    
    R_inv = R.T  # For rotation matrix, inverse = transpose
    t_inv = -np.dot(R_inv, t)
    
    T_inv = np.eye(4, dtype=float)
    T_inv[0:3, 0:3] = R_inv
    T_inv[0:3, 3] = t_inv
    return T_inv
