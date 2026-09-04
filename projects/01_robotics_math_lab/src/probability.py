"""Probability and statistical distributions for robotics.

This module provides basic probability distributions and sampling
utilities, with emphasis on Gaussian distributions commonly used
in robotics.

Author: Robotics AI Research Lab
"""

from typing import Union, Tuple
import numpy as np
import math


class Gaussian:
    """Gaussian (Normal) distribution.
    
    Represents univariate or multivariate Gaussian distribution with
    mean μ and covariance Σ.
    """
    
    def __init__(self, mean: Union[float, np.ndarray] = 0.0,
                variance: Union[float, np.ndarray] = 1.0):
        """Initialize Gaussian distribution.
        
        Args:
            mean: Mean (scalar or vector)
            variance: Variance/covariance (scalar or matrix)
        """
        self.mean = np.atleast_1d(np.array(mean, dtype=float))
        self.covariance = np.atleast_2d(np.array(variance, dtype=float))
        
        # Handle scalar variance
        if self.covariance.ndim == 1:
            self.covariance = np.diag(self.covariance)
        
        self.dim = len(self.mean)
        
        # Precompute Cholesky decomposition
        try:
            self.L = np.linalg.cholesky(self.covariance)
        except np.linalg.LinAlgError:
            # Use eigendecomposition if Cholesky fails
            eigvals, eigvecs = np.linalg.eig(self.covariance)
            self.L = eigvecs @ np.diag(np.sqrt(np.abs(eigvals)))
    
    def pdf(self, x: np.ndarray) -> float:
        """Evaluate probability density function.
        
        Args:
            x: Point to evaluate
            
        Returns:
            Probability density
        """
        x = np.array(x, dtype=float)
        diff = x - self.mean
        
        # Determinant and inverse of covariance
        det = np.linalg.det(self.covariance)
        if det <= 0:
            return 0.0
        
        inv_cov = np.linalg.inv(self.covariance)
        
        # Gaussian PDF: (2π)^(-k/2) |Σ|^(-1/2) exp(-0.5 (x-μ)^T Σ^(-1) (x-μ))
        coeff = (2 * np.pi) ** (-self.dim / 2) * np.sqrt(1.0 / det)
        exponent = -0.5 * np.dot(diff, np.dot(inv_cov, diff))
        
        return float(coeff * np.exp(exponent))
    
    def cdf(self, x: Union[float, np.ndarray]) -> float:
        """Evaluate cumulative distribution function.
        
        Only implemented for univariate case.
        
        Args:
            x: Point to evaluate
            
        Returns:
            Cumulative probability
        """
        if self.dim != 1:
            raise NotImplementedError("CDF only implemented for univariate Gaussian")
        
        x = float(np.atleast_1d(x)[0])
        mean = float(self.mean[0])
        std = float(np.sqrt(self.covariance[0, 0]))
        
        # Standard normal CDF
        z = (x - mean) / std
        return 0.5 * (1 + math.erf(z / math.sqrt(2)))
    
    def sample(self, n_samples: int = 1) -> np.ndarray:
        """Generate samples from Gaussian.
        
        Args:
            n_samples: Number of samples to generate
            
        Returns:
            Array of samples (n_samples × dim)
        """
        # Generate standard normal samples
        z = np.random.randn(n_samples, self.dim)
        
        # Transform to target Gaussian: x = μ + L z
        samples = self.mean + z @ self.L.T
        
        if n_samples == 1:
            return samples[0]
        return samples
    
    def entropy(self) -> float:
        """Compute entropy of Gaussian distribution.
        
        Returns:
            Entropy (in nats)
        """
        det = np.linalg.det(self.covariance)
        return 0.5 * np.log((2 * np.pi * np.e) ** self.dim * det)


def normal_distribution_pdf(x: float, mean: float = 0.0, std: float = 1.0) -> float:
    """Evaluate normal (Gaussian) distribution PDF.
    
    Args:
        x: Point to evaluate
        mean: Mean of distribution
        std: Standard deviation
        
    Returns:
        Probability density
    """
    coeff = 1.0 / (std * math.sqrt(2 * math.pi))
    exponent = -0.5 * ((x - mean) / std) ** 2
    return coeff * math.exp(exponent)


def normal_distribution_cdf(x: float, mean: float = 0.0, std: float = 1.0) -> float:
    """Evaluate normal distribution CDF.
    
    Args:
        x: Point to evaluate
        mean: Mean of distribution
        std: Standard deviation
        
    Returns:
        Cumulative probability
    """
    z = (x - mean) / std
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def normal_distribution_inverse_cdf(p: float, mean: float = 0.0,
                                   std: float = 1.0) -> float:
    """Compute inverse CDF (quantile) of normal distribution.
    
    Args:
        p: Probability (0 < p < 1)
        mean: Mean
        std: Standard deviation
        
    Returns:
        Quantile value
    """
    from scipy.special import erfinv
    
    if p <= 0 or p >= 1:
        raise ValueError("Probability must be in (0, 1)")
    
    # Inverse CDF of standard normal
    z = math.sqrt(2) * erfinv(2 * p - 1)
    return mean + std * z


def mahalanobis_distance(x: np.ndarray, mean: np.ndarray,
                        covariance: np.ndarray) -> float:
    """Compute Mahalanobis distance.
    
    Measures distance accounting for covariance:
    d = √((x - μ)^T Σ^(-1) (x - μ))
    
    Args:
        x: Point
        mean: Mean
        covariance: Covariance matrix
        
    Returns:
        Mahalanobis distance
    """
    x = np.array(x, dtype=float)
    mean = np.array(mean, dtype=float)
    covariance = np.array(covariance, dtype=float)
    
    diff = x - mean
    inv_cov = np.linalg.inv(covariance)
    
    distance = np.sqrt(np.dot(diff, np.dot(inv_cov, diff)))
    return float(distance)


def covariance_matrix_from_samples(samples: np.ndarray) -> np.ndarray:
    """Compute covariance matrix from samples.
    
    Args:
        samples: Sample matrix (n_samples × n_features)
        
    Returns:
        Covariance matrix (n_features × n_features)
    """
    samples = np.array(samples, dtype=float)
    return np.cov(samples.T)


def correlation_coefficient(x: np.ndarray, y: np.ndarray) -> float:
    """Compute Pearson correlation coefficient.
    
    Args:
        x: First variable samples
        y: Second variable samples
        
    Returns:
        Correlation coefficient (-1 to 1)
    """
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    
    if len(x) != len(y):
        raise ValueError("Samples must have same length")
    
    cov = np.cov(x, y)[0, 1]
    std_x = np.std(x)
    std_y = np.std(y)
    
    if std_x == 0 or std_y == 0:
        return 0.0
    
    return float(cov / (std_x * std_y))


def confidence_interval(samples: np.ndarray, confidence: float = 0.95) -> Tuple[float, float]:
    """Compute confidence interval for mean.
    
    Uses t-distribution for small samples.
    
    Args:
        samples: Sample array
        confidence: Confidence level (0 < confidence < 1)
        
    Returns:
        Tuple of (lower_bound, upper_bound)
    """
    from scipy.stats import t
    
    samples = np.array(samples, dtype=float)
    n = len(samples)
    mean = np.mean(samples)
    std_error = np.std(samples, ddof=1) / np.sqrt(n)
    
    # t-distribution critical value
    alpha = 1 - confidence
    t_crit = t.ppf(1 - alpha/2, n - 1)
    
    margin = t_crit * std_error
    return float(mean - margin), float(mean + margin)


def probability_in_range(mean: float, std: float, lower: float,
                        upper: float) -> float:
    """Compute probability of value in range for normal distribution.
    
    Args:
        mean: Distribution mean
        std: Distribution standard deviation
        lower: Lower bound
        upper: Upper bound
        
    Returns:
        Probability (0 to 1)
    """
    cdf_lower = normal_distribution_cdf(lower, mean, std)
    cdf_upper = normal_distribution_cdf(upper, mean, std)
    return cdf_upper - cdf_lower


def chi_squared_distribution_pdf(x: float, df: int) -> float:
    """Evaluate chi-squared distribution PDF.
    
    Args:
        x: Point to evaluate (x ≥ 0)
        df: Degrees of freedom
        
    Returns:
        Probability density
    """
    if x < 0:
        return 0.0
    
    from scipy.stats import chi2
    return float(chi2.pdf(x, df))


def exponential_distribution_pdf(x: float, rate: float = 1.0) -> float:
    """Evaluate exponential distribution PDF.
    
    Args:
        x: Point to evaluate (x ≥ 0)
        rate: Rate parameter (λ)
        
    Returns:
        Probability density
    """
    if x < 0 or rate <= 0:
        return 0.0
    
    return rate * math.exp(-rate * x)
