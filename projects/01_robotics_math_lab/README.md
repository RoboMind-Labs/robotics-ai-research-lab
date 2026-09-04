# Project 01: Robotics Mathematics Lab

## Overview

This project provides a comprehensive introduction to the mathematical foundations essential for robotics. Through hands-on Python implementations and interactive examples, you'll build intuition for the key concepts that underpin robot kinematics, control, and planning.

## Learning Objectives

By completing this project, you will:

- ✓ Understand vector operations and their geometric meaning
- ✓ Master matrix operations and linear transformations
- ✓ Implement 2D and 3D rotation representations
- ✓ Build coordinate frame hierarchies and transformations
- ✓ Compute eigenvalues/eigenvectors and their applications
- ✓ Implement gradient-based optimization from scratch
- ✓ Work with probability distributions
- ✓ Visualize all concepts through plots and animations

## Project Structure

```
01_robotics_math_lab/
├── README.md (this file)
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── vectors.py              # Vector operations
│   ├── matrices.py             # Matrix operations
│   ├── transformations.py      # Rotation matrices and transforms
│   ├── coordinate_frames.py    # Frame hierarchies
│   ├── eigenvalues.py          # Eigenvalue decomposition
│   ├── gradients.py            # Gradient computation & optimization
│   └── probability.py          # Probability distributions
├── examples/
│   ├── 01_vector_operations.py
│   ├── 02_matrix_operations.py
│   ├── 03_transformations_2d.py
│   ├── 04_transformations_3d.py
│   ├── 05_coordinate_frames.py
│   ├── 06_gradient_descent.py
│   └── 07_robotics_applications.py
├── tests/
│   ├── test_vectors.py
│   ├── test_matrices.py
│   ├── test_transformations.py
│   └── test_gradients.py
└── visualizations/
    └── (plots saved here)
```

## Topics Covered

### 1. Vector Operations (`vectors.py`)
- Vector creation and representation
- Vector addition and subtraction
- Scalar multiplication
- Dot product (inner product)
- Cross product
- Vector norms (L1, L2, infinity)
- Vector normalization
- Angle between vectors

**Applications**: Position representation, velocity calculations, direction vectors

### 2. Matrix Operations (`matrices.py`)
- Matrix creation and manipulation
- Matrix multiplication
- Matrix transpose
- Matrix inverse
- Determinant calculation
- Matrix rank
- Matrix trace
- Solving linear systems

**Applications**: Transformation composition, linear system solving, coordinate changes

### 3. Transformations (`transformations.py`)
- 2D rotation matrices
- 2D transformation matrices (rotation + translation)
- 3D rotation matrices (Euler angles, axis-angle)
- Quaternion representation
- Homogeneous transformation matrices
- Transformation composition
- Transformation inversion

**Applications**: Robot pose representation, camera transformations, coordinate conversions

### 4. Coordinate Frames (`coordinate_frames.py`)
- Coordinate frame representation
- Frame hierarchies and trees
- Forward transformations (world to frame)
- Inverse transformations (frame to world)
- Multi-frame chains
- Jacobian computation
- Singularity analysis

**Applications**: Robot kinematics, sensor mounting, multi-body systems

### 5. Eigenvalues (`eigenvalues.py`)
- Eigenvalue computation
- Eigenvector calculation
- Eigenvalue decomposition
- Matrix diagonalization
- Power method
- Applications to PCA and stability

**Applications**: Principal component analysis, stability analysis, mode analysis

### 6. Gradients & Optimization (`gradients.py`)
- Numerical gradient computation
- Analytical gradients for simple functions
- Gradient descent algorithm
- Momentum variants
- Nesterov momentum
- Learning rate scheduling
- Convergence analysis

**Applications**: Robot learning, parameter optimization, trajectory fitting

### 7. Probability (`probability.py`)
- Probability basics
- Gaussian/Normal distribution
- Probability density functions
- Cumulative distribution functions
- Sampling from distributions
- Multivariate Gaussian

**Applications**: Sensor noise modeling, probabilistic planning, uncertainty quantification

## Getting Started

### Installation

```bash
# Navigate to project directory
cd projects/01_robotics_math_lab

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/Scripts/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running Examples

```bash
# Run a specific example
python examples/01_vector_operations.py

# Run all examples
for example in examples/*.py:
    python $example

# Or on Windows:
for /r "examples" %f in (*.py) do python %f
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_vectors.py

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=src
```

## Implementation Details

### Type Hints
All functions use Python type hints for clarity and IDE support:

```python
def add_vectors(v1: list[float], v2: list[float]) -> list[float]:
    """Add two vectors element-wise."""
```

### Docstrings
Google-style docstrings on all functions:

```python
def cross_product(v1: list[float], v2: list[float]) -> list[float]:
    """Compute cross product of two 3D vectors.
    
    Args:
        v1: First 3D vector
        v2: Second 3D vector
        
    Returns:
        Cross product vector v1 × v2
        
    Raises:
        ValueError: If vectors are not 3D
    """
```

### NumPy Integration
Uses NumPy for efficient numerical operations where appropriate, but also provides implementations from scratch for learning.

### Visualization
All examples include matplotlib plots to visualize:
- Vector operations geometrically
- Transformations in 2D and 3D
- Gradient descent convergence
- Rotation behaviors

## Key Equations

### Vector Norm (L2)
```
||v|| = √(Σ vᵢ²)
```

### Dot Product
```
v₁ · v₂ = Σ v₁ᵢ * v₂ᵢ = ||v₁|| ||v₂|| cos(θ)
```

### Cross Product (3D)
```
v₁ × v₂ = (v₁ᵧv₂ᵤ - v₁ᵤv₂ᵧ, v₁ᵤv₂ₓ - v₁ₓv₂ᵤ, v₁ₓv₂ᵧ - v₁ᵧv₂ₓ)
```

### 2D Rotation Matrix
```
R(θ) = [cos(θ) -sin(θ)]
       [sin(θ)  cos(θ)]
```

### Gradient Descent Update
```
x_{n+1} = x_n - α ∇f(x_n)
```

### Eigenvalue Equation
```
A v = λ v
where λ is eigenvalue, v is eigenvector
```

## Expected Learning Timeline

| Topic | Time | Difficulty |
|-------|------|------------|
| Vectors | 1-2 hours | Easy |
| Matrices | 2-3 hours | Easy-Medium |
| Transformations | 2-3 hours | Medium |
| Coordinate Frames | 2-3 hours | Medium |
| Eigenvalues | 1-2 hours | Medium |
| Gradients & Optimization | 2-3 hours | Medium-Hard |
| Probability | 1-2 hours | Easy-Medium |
| **Total** | **12-18 hours** | |

## Success Criteria

You should be able to:

1. **Theory**: Explain each concept in your own words without references
2. **Implementation**: Code functions from scratch without looking at solutions
3. **Application**: Solve new problems using these tools
4. **Visualization**: Create plots demonstrating concepts
5. **Testing**: Write tests achieving >90% code coverage
6. **Integration**: Combine concepts for robotics applications

## Verification Checklist

- [ ] All 7 modules implemented and documented
- [ ] All 7 example scripts run without errors
- [ ] All 4 test files pass with pytest
- [ ] Code coverage >90%
- [ ] All plots generated correctly
- [ ] Documentation is comprehensive
- [ ] All type hints are correct
- [ ] No hard-coded values (use parameters)

## Common Challenges & Solutions

### Challenge 1: Matrix Multiplication Order
**Problem**: Getting dimension mismatch errors  
**Solution**: Remember A(m×n) × B(n×p) = C(m×p). Check dimensions carefully.

### Challenge 2: Angle Conventions
**Problem**: Rotations give unexpected results  
**Solution**: Be consistent with angle units (radians vs degrees) and rotation order (XYZ vs ZYX).

### Challenge 3: Singular Matrices
**Problem**: Matrix inverse fails  
**Solution**: Check determinant is non-zero. Use pseudo-inverse for singular matrices.

### Challenge 4: Numerical Stability
**Problem**: Large errors in computations  
**Solution**: Use appropriate matrix decompositions (QR, SVD) instead of direct methods.

## Next Steps

After completing this project:

1. Review the mathematics.md documentation in the root directory
2. Proceed to Project 02: Machine Learning Fundamentals
3. Apply these tools to robotics problems in later projects
4. Experiment with creating your own examples

## Additional Resources

### Online References
- [MIT OpenCourseWare - Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra)
- [Khan Academy - Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
- [NumPy Documentation](https://numpy.org/doc/)

### Textbooks
- Strang, G. (2016). "Linear Algebra and Its Applications"
- Craig, J. J. (2009). "Introduction to Robotics"
- Boyd & Vandenberghe (2004). "Convex Optimization"

### Visualization Tools
- Matplotlib for 2D plotting
- Mpl_toolkits.mplot3d for 3D plotting
- Mayavi for advanced 3D visualization (optional)

## Contributing

If you extend this project, please:

1. Follow the existing code style and documentation format
2. Add unit tests for any new functions
3. Update this README with new topics
4. Create visualizations for new concepts

## Author Notes

This project is designed to build deep understanding through implementation. Rather than using high-level libraries like scikit-learn, we implement core algorithms from scratch to understand the mathematics. NumPy is used for efficient array operations, but the focus remains on understanding what's happening mathematically.

The progression from basic vectors to coordinate frames to optimization demonstrates how foundational concepts build into practical robotics tools.

---

**Status**: 🟡 In Development  
**Last Updated**: 2024-09-04  
**Completion Target**: 100% ✓

Good luck, and remember: understanding the mathematics deeply now will save enormous time when tackling complex robotics problems later!
