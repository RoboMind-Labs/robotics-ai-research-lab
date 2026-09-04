"""Vector operations module for robotics mathematics.

This module provides fundamental vector operations including creation,
arithmetic operations, and geometric computations. All functions support
both Python lists and NumPy arrays.

Author: Robotics AI Research Lab
"""

from typing import Union, Tuple
import math
import numpy as np


def create_vector(components: list[float]) -> np.ndarray:
    """Create a vector from components.
    
    Args:
        components: List of vector components
        
    Returns:
        NumPy array representing the vector
    """
    return np.array(components, dtype=float)


def add_vectors(v1: Union[list, np.ndarray], v2: Union[list, np.ndarray]) -> np.ndarray:
    """Add two vectors element-wise.
    
    Args:
        v1: First vector
        v2: Second vector
        
    Returns:
        Sum vector v1 + v2
        
    Raises:
        ValueError: If vectors have different dimensions
    """
    v1 = np.array(v1, dtype=float)
    v2 = np.array(v2, dtype=float)
    
    if v1.shape != v2.shape:
        raise ValueError(f"Vector dimensions must match: {v1.shape} vs {v2.shape}")
    
    return v1 + v2


def subtract_vectors(v1: Union[list, np.ndarray], v2: Union[list, np.ndarray]) -> np.ndarray:
    """Subtract two vectors element-wise.
    
    Args:
        v1: First vector (minuend)
        v2: Second vector (subtrahend)
        
    Returns:
        Difference vector v1 - v2
        
    Raises:
        ValueError: If vectors have different dimensions
    """
    v1 = np.array(v1, dtype=float)
    v2 = np.array(v2, dtype=float)
    
    if v1.shape != v2.shape:
        raise ValueError(f"Vector dimensions must match: {v1.shape} vs {v2.shape}")
    
    return v1 - v2


def scale_vector(v: Union[list, np.ndarray], scalar: float) -> np.ndarray:
    """Scale a vector by a scalar value.
    
    Args:
        v: Vector to scale
        scalar: Scalar multiplier
        
    Returns:
        Scaled vector scalar * v
    """
    return scalar * np.array(v, dtype=float)


def dot_product(v1: Union[list, np.ndarray], v2: Union[list, np.ndarray]) -> float:
    """Compute dot product of two vectors.
    
    The dot product is the sum of element-wise products:
    v1 · v2 = Σ(v1_i * v2_i) = ||v1|| ||v2|| cos(θ)
    
    Args:
        v1: First vector
        v2: Second vector
        
    Returns:
        Scalar dot product
        
    Raises:
        ValueError: If vectors have different dimensions
    """
    v1 = np.array(v1, dtype=float)
    v2 = np.array(v2, dtype=float)
    
    if v1.shape != v2.shape:
        raise ValueError(f"Vector dimensions must match: {v1.shape} vs {v2.shape}")
    
    return float(np.dot(v1, v2))


def cross_product(v1: Union[list, np.ndarray], v2: Union[list, np.ndarray]) -> np.ndarray:
    """Compute cross product of two 3D vectors.
    
    The cross product produces a vector perpendicular to both inputs:
    v1 × v2 = (v1_y*v2_z - v1_z*v2_y, v1_z*v2_x - v1_x*v2_z, v1_x*v2_y - v1_y*v2_x)
    
    Args:
        v1: First 3D vector
        v2: Second 3D vector
        
    Returns:
        Cross product vector v1 × v2
        
    Raises:
        ValueError: If vectors are not 3D
    """
    v1 = np.array(v1, dtype=float)
    v2 = np.array(v2, dtype=float)
    
    if v1.shape != (3,) or v2.shape != (3,):
        raise ValueError(f"Cross product requires 3D vectors, got {v1.shape} and {v2.shape}")
    
    return np.array([
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ], dtype=float)


def vector_norm(v: Union[list, np.ndarray], order: int = 2) -> float:
    """Compute the norm (magnitude) of a vector.
    
    Supports various norms:
    - L1 norm: ||v||_1 = Σ|v_i|
    - L2 norm: ||v||_2 = √(Σ v_i²)  [default, Euclidean]
    - Infinity norm: ||v||_∞ = max|v_i|
    
    Args:
        v: Input vector
        order: Norm order (1, 2, or float('inf'))
        
    Returns:
        Scalar norm value (always non-negative)
    """
    v = np.array(v, dtype=float)
    
    if order == 1:
        return float(np.sum(np.abs(v)))
    elif order == 2:
        return float(np.sqrt(np.sum(v**2)))
    elif order == float('inf'):
        return float(np.max(np.abs(v)))
    else:
        return float(np.power(np.sum(np.abs(v)**order), 1/order))


def normalize_vector(v: Union[list, np.ndarray]) -> np.ndarray:
    """Normalize a vector to unit length (L2 norm = 1).
    
    Args:
        v: Vector to normalize
        
    Returns:
        Unit vector in the same direction
        
    Raises:
        ValueError: If vector has zero norm
    """
    v = np.array(v, dtype=float)
    norm = vector_norm(v)
    
    if norm == 0:
        raise ValueError("Cannot normalize zero vector")
    
    return v / norm


def angle_between_vectors(v1: Union[list, np.ndarray], v2: Union[list, np.ndarray]) -> float:
    """Compute angle between two vectors in radians.
    
    Uses the formula: θ = arccos((v1 · v2) / (||v1|| ||v2||))
    
    Args:
        v1: First vector
        v2: Second vector
        
    Returns:
        Angle in radians [0, π]
        
    Raises:
        ValueError: If either vector has zero norm
    """
    v1 = np.array(v1, dtype=float)
    v2 = np.array(v2, dtype=float)
    
    norm1 = vector_norm(v1)
    norm2 = vector_norm(v2)
    
    if norm1 == 0 or norm2 == 0:
        raise ValueError("Cannot compute angle with zero-norm vector")
    
    # Clamp to [-1, 1] to avoid numerical errors
    cos_angle = np.clip(dot_product(v1, v2) / (norm1 * norm2), -1, 1)
    return float(np.arccos(cos_angle))


def distance_between_points(p1: Union[list, np.ndarray], p2: Union[list, np.ndarray]) -> float:
    """Compute Euclidean distance between two points.
    
    Args:
        p1: First point
        p2: Second point
        
    Returns:
        Euclidean distance ||p2 - p1||
    """
    diff = subtract_vectors(p1, p2)
    return vector_norm(diff)


def projection_onto_vector(v: Union[list, np.ndarray], u: Union[list, np.ndarray]) -> np.ndarray:
    """Project vector v onto vector u.
    
    Returns the component of v in the direction of u:
    proj_u(v) = ((v · u) / (u · u)) * u
    
    Args:
        v: Vector to project
        u: Vector to project onto
        
    Returns:
        Projection of v onto u
    """
    v = np.array(v, dtype=float)
    u = np.array(u, dtype=float)
    
    u_dot_u = dot_product(u, u)
    if u_dot_u == 0:
        raise ValueError("Cannot project onto zero vector")
    
    projection_length = dot_product(v, u) / u_dot_u
    return scale_vector(u, projection_length)


def perpendicular_component(v: Union[list, np.ndarray], u: Union[list, np.ndarray]) -> np.ndarray:
    """Compute component of v perpendicular to u.
    
    Args:
        v: Vector
        u: Reference vector
        
    Returns:
        Component of v perpendicular to u (v - proj_u(v))
    """
    return subtract_vectors(v, projection_onto_vector(v, u))


def are_parallel(v1: Union[list, np.ndarray], v2: Union[list, np.ndarray], 
                 tolerance: float = 1e-9) -> bool:
    """Check if two vectors are parallel (or anti-parallel).
    
    Args:
        v1: First vector
        v2: Second vector
        tolerance: Numerical tolerance for comparison
        
    Returns:
        True if vectors are parallel or anti-parallel
    """
    v1 = np.array(v1, dtype=float)
    v2 = np.array(v2, dtype=float)
    
    try:
        angle = angle_between_vectors(v1, v2)
        return abs(angle) < tolerance or abs(angle - np.pi) < tolerance
    except ValueError:
        return False


def are_perpendicular(v1: Union[list, np.ndarray], v2: Union[list, np.ndarray],
                      tolerance: float = 1e-9) -> bool:
    """Check if two vectors are perpendicular (orthogonal).
    
    Args:
        v1: First vector
        v2: Second vector
        tolerance: Numerical tolerance for dot product
        
    Returns:
        True if vectors are perpendicular
    """
    return abs(dot_product(v1, v2)) < tolerance
