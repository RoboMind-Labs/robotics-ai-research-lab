"""Robotics Mathematics Lab - Foundational modules for robotics and AI.

This package provides implementations of core mathematical concepts
used in robotics, including vectors, matrices, transformations,
coordinate frames, eigenvalue analysis, optimization, and probability.

Modules:
- vectors: Vector operations and geometric computations
- matrices: Matrix operations, decompositions, and linear system solving
- transformations: 2D and 3D rotations and homogeneous transformations
- coordinate_frames: Frame hierarchies and coordinate transformations
- eigenvalues: Eigenvalue decomposition and applications
- gradients: Numerical gradients and optimization algorithms
- probability: Probability distributions and statistics

Author: Robotics AI Research Lab
"""

__version__ = "0.1.0"
__author__ = "Robotics AI Research Lab"

from . import vectors
from . import matrices
from . import transformations
from . import coordinate_frames
from . import eigenvalues
from . import gradients
from . import probability

__all__ = [
    'vectors',
    'matrices',
    'transformations',
    'coordinate_frames',
    'eigenvalues',
    'gradients',
    'probability',
]
