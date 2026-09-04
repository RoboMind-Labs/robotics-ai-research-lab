"""Coordinate frame module for managing frame hierarchies in robotics.

This module provides tools for working with coordinate frames, frame
hierarchies (trees), and transformations between frames.

Author: Robotics AI Research Lab
"""

from typing import Dict, Optional, List, Tuple, Union
import numpy as np
from . import transformations


class CoordinateFrame:
    """Represents a coordinate frame in 3D space.
    
    A frame has a name, parent frame, and transformation relative to parent.
    Frames can form hierarchies where a frame's parent is another frame.
    """
    
    def __init__(self, name: str, parent: Optional['CoordinateFrame'] = None,
                 T_to_parent: Optional[np.ndarray] = None):
        """Initialize a coordinate frame.
        
        Args:
            name: Frame name (e.g., 'world', 'robot_base', 'end_effector')
            parent: Parent frame (None for root)
            T_to_parent: 4×4 transformation from this frame to parent
        """
        self.name = name
        self.parent = parent
        
        if T_to_parent is None:
            self.T_to_parent = np.eye(4, dtype=float)
        else:
            self.T_to_parent = np.array(T_to_parent, dtype=float)
        
        self.children: List[CoordinateFrame] = []
        
        if parent is not None:
            parent.add_child(self)
    
    def add_child(self, frame: 'CoordinateFrame') -> None:
        """Add a child frame to this frame.
        
        Args:
            frame: Child frame to add
        """
        if frame not in self.children:
            self.children.append(frame)
    
    def get_transformation_to_parent(self) -> np.ndarray:
        """Get transformation from this frame to parent.
        
        Returns:
            4×4 homogeneous transformation matrix
        """
        return self.T_to_parent.copy()
    
    def set_transformation_to_parent(self, T: np.ndarray) -> None:
        """Set transformation from this frame to parent.
        
        Args:
            T: 4×4 homogeneous transformation matrix
        """
        self.T_to_parent = np.array(T, dtype=float)
    
    def get_transformation_to_world(self) -> np.ndarray:
        """Get transformation from this frame to world (root) frame.
        
        Returns:
            4×4 homogeneous transformation matrix
        """
        if self.parent is None:
            return np.eye(4, dtype=float)
        
        # T_to_world = T_parent_to_world * T_to_parent
        T_parent_to_world = self.parent.get_transformation_to_world()
        return np.dot(T_parent_to_world, self.T_to_parent)
    
    def get_transformation_from_world(self) -> np.ndarray:
        """Get transformation from world frame to this frame.
        
        Returns:
            4×4 homogeneous transformation matrix
        """
        T_to_world = self.get_transformation_to_world()
        return transformations.inverse_transformation_3d(T_to_world)
    
    def get_position_in_world(self) -> np.ndarray:
        """Get frame origin position in world frame.
        
        Returns:
            3D position vector
        """
        T = self.get_transformation_to_world()
        return T[0:3, 3].copy()
    
    def get_rotation_in_world(self) -> np.ndarray:
        """Get frame rotation in world frame.
        
        Returns:
            3×3 rotation matrix
        """
        T = self.get_transformation_to_world()
        return T[0:3, 0:3].copy()
    
    def transform_point_to_world(self, point: Union[list, np.ndarray]) -> np.ndarray:
        """Transform a point from this frame to world frame.
        
        Args:
            point: 3D point in this frame
            
        Returns:
            3D point in world frame
        """
        T_to_world = self.get_transformation_to_world()
        return transformations.apply_transformation_3d(T_to_world, point)
    
    def transform_point_from_world(self, point: Union[list, np.ndarray]) -> np.ndarray:
        """Transform a point from world frame to this frame.
        
        Args:
            point: 3D point in world frame
            
        Returns:
            3D point in this frame
        """
        T_from_world = self.get_transformation_from_world()
        return transformations.apply_transformation_3d(T_from_world, point)


class FrameTree:
    """Manages a hierarchy of coordinate frames.
    
    Maintains a tree of frames with efficient transformations between
    any two frames.
    """
    
    def __init__(self, root_name: str = 'world'):
        """Initialize frame tree.
        
        Args:
            root_name: Name of root frame
        """
        self.root = CoordinateFrame(root_name)
        self.frames: Dict[str, CoordinateFrame] = {root_name: self.root}
    
    def add_frame(self, name: str, parent_name: str,
                  T_to_parent: Optional[np.ndarray] = None) -> CoordinateFrame:
        """Add a new frame to the tree.
        
        Args:
            name: Name of new frame
            parent_name: Name of parent frame
            T_to_parent: Transformation from this frame to parent
            
        Returns:
            The newly created frame
            
        Raises:
            ValueError: If parent frame doesn't exist or frame already exists
        """
        if name in self.frames:
            raise ValueError(f"Frame '{name}' already exists")
        
        if parent_name not in self.frames:
            raise ValueError(f"Parent frame '{parent_name}' not found")
        
        parent = self.frames[parent_name]
        frame = CoordinateFrame(name, parent, T_to_parent)
        self.frames[name] = frame
        return frame
    
    def get_frame(self, name: str) -> Optional[CoordinateFrame]:
        """Get a frame by name.
        
        Args:
            name: Frame name
            
        Returns:
            Frame object or None if not found
        """
        return self.frames.get(name)
    
    def get_transformation(self, from_frame: str, to_frame: str) -> np.ndarray:
        """Get transformation from one frame to another.
        
        Args:
            from_frame: Source frame name
            to_frame: Target frame name
            
        Returns:
            4×4 transformation matrix
            
        Raises:
            ValueError: If frames don't exist
        """
        if from_frame not in self.frames or to_frame not in self.frames:
            raise ValueError("One or both frames not found")
        
        f_from = self.frames[from_frame]
        f_to = self.frames[to_frame]
        
        # T_to = T_to_world^(-1) * T_from_to_world
        T_from_to_world = f_from.get_transformation_to_world()
        T_world_to_to = transformations.inverse_transformation_3d(
            f_to.get_transformation_to_world()
        )
        
        return np.dot(T_world_to_to, T_from_to_world)
    
    def update_frame_transformation(self, frame_name: str,
                                   T_to_parent: np.ndarray) -> None:
        """Update transformation of a frame relative to its parent.
        
        Args:
            frame_name: Name of frame to update
            T_to_parent: New transformation matrix
            
        Raises:
            ValueError: If frame doesn't exist
        """
        if frame_name not in self.frames:
            raise ValueError(f"Frame '{frame_name}' not found")
        
        if frame_name == self.root.name:
            raise ValueError("Cannot update root frame transformation")
        
        self.frames[frame_name].set_transformation_to_parent(T_to_parent)
    
    def list_frames(self) -> List[str]:
        """List all frame names.
        
        Returns:
            List of frame names
        """
        return list(self.frames.keys())
    
    def get_frame_hierarchy(self, frame_name: str) -> List[str]:
        """Get hierarchy path from frame to root.
        
        Args:
            frame_name: Name of frame
            
        Returns:
            List of frame names from given frame to root
            
        Raises:
            ValueError: If frame doesn't exist
        """
        if frame_name not in self.frames:
            raise ValueError(f"Frame '{frame_name}' not found")
        
        path = []
        frame = self.frames[frame_name]
        
        while frame is not None:
            path.append(frame.name)
            frame = frame.parent
        
        return path


def compute_jacobian_numerical(frame_tree: FrameTree, end_effector_frame: str,
                              joint_frames: List[str], delta: float = 1e-6) -> np.ndarray:
    """Compute Jacobian matrix numerically using finite differences.
    
    Args:
        frame_tree: Frame tree with robot structure
        end_effector_frame: Name of end-effector frame
        joint_frames: List of joint frame names in order
        delta: Finite difference step size
        
    Returns:
        6×n Jacobian matrix (3 for position, 3 for rotation)
    """
    n_joints = len(joint_frames)
    jacobian = np.zeros((6, n_joints), dtype=float)
    
    # Get nominal end-effector pose
    T_nominal = frame_tree.get_transformation('world', end_effector_frame)
    p_nominal = T_nominal[0:3, 3]
    
    for i, joint_frame in enumerate(joint_frames):
        # Perturb joint i
        frame = frame_tree.get_frame(joint_frame)
        T_original = frame.get_transformation_to_parent().copy()
        
        # Positive perturbation
        T_perturbed = T_original.copy()
        T_perturbed[2, 3] += delta  # Example: translate along Z
        
        frame.set_transformation_to_parent(T_perturbed)
        T_perturbed_ee = frame_tree.get_transformation('world', end_effector_frame)
        p_perturbed = T_perturbed_ee[0:3, 3]
        
        # Restore original
        frame.set_transformation_to_parent(T_original)
        
        # Compute derivative
        dp_dq = (p_perturbed - p_nominal) / delta
        jacobian[0:3, i] = dp_dq
    
    return jacobian
