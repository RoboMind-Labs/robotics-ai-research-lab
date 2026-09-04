"""Comprehensive example demonstrating all Project 01 modules.

This script shows usage of vectors, matrices, transformations,
coordinate frames, eigenvalues, gradients, and probability modules.

Run with: python examples/complete_demo.py
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import vectors, matrices, transformations, gradients, probability, eigenvalues


def demo_vectors():
    """Demonstrate vector operations."""
    print("\n" + "="*60)
    print("VECTOR OPERATIONS DEMO")
    print("="*60)
    
    v1 = vectors.create_vector([1, 2, 3])
    v2 = vectors.create_vector([4, 5, 6])
    
    print(f"Vector 1: {v1}")
    print(f"Vector 2: {v2}")
    print(f"Sum: {vectors.add_vectors(v1, v2)}")
    print(f"Dot product: {vectors.dot_product(v1, v2)}")
    print(f"Cross product: {vectors.cross_product(v1, v2)}")
    print(f"Norm of v1: {vectors.vector_norm(v1)}")
    print(f"Normalized v1: {vectors.normalize_vector(v1)}")


def demo_matrices():
    """Demonstrate matrix operations."""
    print("\n" + "="*60)
    print("MATRIX OPERATIONS DEMO")
    print("="*60)
    
    A = [[1, 2], [3, 4]]
    B = [[2, 0], [1, 2]]
    
    print(f"Matrix A:\n{np.array(A)}")
    print(f"Matrix B:\n{np.array(B)}")
    print(f"A * B:\n{matrices.matrix_multiply(A, B)}")
    print(f"Determinant of A: {matrices.matrix_determinant(A)}")
    print(f"Trace of A: {matrices.matrix_trace(A)}")
    print(f"Rank of A: {matrices.matrix_rank(A)}")
    print(f"A^(-1):\n{matrices.matrix_inverse(A)}")


def demo_transformations():
    """Demonstrate transformations."""
    print("\n" + "="*60)
    print("TRANSFORMATION OPERATIONS DEMO")
    print("="*60)
    
    # 2D rotation
    R2d = transformations.rotation_matrix_2d(np.pi / 4)
    print(f"2D rotation (45°):\n{R2d}")
    
    # 3D rotation about Z
    R3d = transformations.rotation_matrix_3d_z(np.pi / 4)
    print(f"3D Z rotation (45°):\n{R3d}")
    
    # Homogeneous transformation
    R = np.eye(3)
    t = [1, 2, 3]
    T = transformations.homogeneous_transformation_matrix_3d(R, t)
    print(f"Homogeneous transformation (identity + translation):\n{T}")
    
    # Transform a point
    point = [0, 0, 0]
    transformed = transformations.apply_transformation_3d(T, point)
    print(f"Point {point} transformed: {transformed}")


def demo_eigenvalues():
    """Demonstrate eigenvalue decomposition."""
    print("\n" + "="*60)
    print("EIGENVALUE DECOMPOSITION DEMO")
    print("="*60)
    
    A = [[4, -2], [-2, 1]]
    eigenvals, eigenvecs = eigenvalues.eigenvalue_decomposition(A)
    print(f"Matrix:\n{np.array(A)}")
    print(f"Eigenvalues: {eigenvals}")
    print(f"Eigenvectors:\n{eigenvecs}")


def demo_gradients():
    """Demonstrate gradient descent optimization."""
    print("\n" + "="*60)
    print("GRADIENT DESCENT OPTIMIZATION DEMO")
    print("="*60)
    
    # Optimize a simple quadratic function
    def quadratic(x):
        return (x[0] - 2)**2 + (x[1] - 3)**2
    
    optimizer = gradients.GradientDescentOptimizer(
        learning_rate=0.1,
        max_iterations=200
    )
    x0 = np.array([0.0, 0.0])
    x_opt, history = optimizer.optimize(quadratic, x0)
    
    print(f"Initial point: {x0}")
    print(f"Optimal point: {x_opt}")
    print(f"Final value: {quadratic(x_opt):.6f}")
    print(f"Iterations: {len(history)}")


def demo_probability():
    """Demonstrate probability distributions."""
    print("\n" + "="*60)
    print("PROBABILITY DISTRIBUTIONS DEMO")
    print("="*60)
    
    # Create Gaussian distribution
    gaussian = probability.Gaussian(mean=0, variance=1)
    
    print(f"Gaussian: mean=0, variance=1")
    print(f"PDF at x=0: {gaussian.pdf(0):.4f}")
    print(f"CDF at x=0: {gaussian.cdf(0):.4f}")
    
    # Generate samples
    samples = gaussian.sample(n_samples=5)
    print(f"5 samples: {samples}")


def create_visualizations():
    """Create visualization plots."""
    print("\n" + "="*60)
    print("Creating visualizations...")
    print("="*60)
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Robotics Mathematics Lab - Visualizations', fontsize=16, fontweight='bold')
    
    # Plot 1: Vector operations
    ax = axes[0, 0]
    v1 = np.array([3, 4])
    v2 = np.array([1, 2])
    ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='b', label='v1')
    ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='r', label='v2')
    v_sum = vectors.add_vectors(v1, v2)
    ax.quiver(0, 0, v_sum[0], v_sum[1], angles='xy', scale_units='xy', scale=1, color='g', label='v1+v2')
    ax.set_xlim(-1, 6)
    ax.set_ylim(-1, 8)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('Vector Addition')
    ax.legend()
    
    # Plot 2: 2D rotations
    ax = axes[0, 1]
    angles = np.linspace(0, 2*np.pi, 8, endpoint=False)
    for angle in angles:
        R = transformations.rotation_matrix_2d(angle)
        v = np.array([1, 0])
        v_rot = np.dot(R, v)
        ax.arrow(0, 0, v_rot[0], v_rot[1], head_width=0.1, head_length=0.1, fc='blue', ec='blue', alpha=0.6)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('2D Rotations (Unit Vector)')
    
    # Plot 3: Matrix eigenvalues
    ax = axes[0, 2]
    A = np.array([[2, 1], [1, 2]])
    eigenvals, eigenvecs = eigenvalues.eigenvalue_decomposition(A)
    for i, (lam, v) in enumerate(zip(eigenvals, eigenvecs.T)):
        ax.arrow(0, 0, v[0]*np.sqrt(lam), v[1]*np.sqrt(lam), 
                head_width=0.1, head_length=0.1, label=f'λ={lam:.2f}')
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('Eigenvectors & Eigenvalues')
    ax.legend()
    
    # Plot 4: Gradient descent convergence
    ax = axes[1, 0]
    def f(x):
        return (x[0] - 2)**2 + (x[1] - 3)**2
    
    optimizer = gradients.GradientDescentOptimizer(learning_rate=0.1, max_iterations=100)
    x_opt, history = optimizer.optimize(f, np.array([0.0, 0.0]))
    ax.plot(history, linewidth=2, color='blue')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Function Value')
    ax.set_title('Gradient Descent Convergence')
    ax.grid(True, alpha=0.3)
    ax.set_yscale('log')
    
    # Plot 5: Gaussian distribution
    ax = axes[1, 1]
    x_vals = np.linspace(-4, 4, 200)
    y_vals = [probability.normal_distribution_pdf(x) for x in x_vals]
    ax.plot(x_vals, y_vals, linewidth=2, color='blue')
    ax.fill_between(x_vals, y_vals, alpha=0.3)
    ax.set_xlabel('x')
    ax.set_ylabel('Probability Density')
    ax.set_title('Gaussian Distribution (μ=0, σ=1)')
    ax.grid(True, alpha=0.3)
    
    # Plot 6: Rosenbrock function
    ax = axes[1, 2]
    x = np.linspace(-0.5, 2.5, 100)
    y = np.linspace(-0.5, 2.5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X)
    for i in range(len(x)):
        for j in range(len(y)):
            Z[j, i] = gradients.rosenbrock(np.array([X[j, i], Y[j, i]]))
    
    contour = ax.contour(X, Y, Z, levels=20, cmap='viridis')
    ax.clabel(contour, inline=True, fontsize=8)
    ax.plot(1, 1, 'r*', markersize=15, label='Minimum')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Rosenbrock Function')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('visualizations/complete_demo.png', dpi=150, bbox_inches='tight')
    print("Successfully saved visualization to visualizations/complete_demo.png")
    plt.close()


if __name__ == "__main__":
    print("\n" + "="*60)
    print("ROBOTICS MATHEMATICS LAB - COMPLETE DEMO")
    print("="*60)
    
    try:
        demo_vectors()
        demo_matrices()
        demo_transformations()
        demo_eigenvalues()
        demo_gradients()
        demo_probability()
        create_visualizations()
        
        print("\n" + "="*60)
        print("All demonstrations completed successfully")
        print("="*60 + "\n")
        
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
