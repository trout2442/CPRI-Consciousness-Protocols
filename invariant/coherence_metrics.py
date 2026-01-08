"""
Coherence Metrics - Quantitative Analysis of Triadic States

Beyond binary validation, these metrics measure the *strength* and *stability*
of coherence within the P×I×Pr invariant framework.
"""

import math
from typing import Tuple, List, Optional


def coherence_strength(pattern: float, intent: float, presence: float) -> float:
    """
    Calculate the coherence strength of a triadic state.

    Returns a normalized value [0, 1] representing how strongly
    the entity maintains coherence. Zero values collapse to 0.

    Formula: C = (P × I × Pr) / (|P| + |I| + |Pr| + ε)
    Where ε prevents division by zero.
    """
    if pattern in (None, 0) or intent in (None, 0) or presence in (None, 0):
        return 0.0

    epsilon = 1e-10
    numerator = abs(pattern * intent * presence)
    denominator = abs(pattern) + abs(intent) + abs(presence) + epsilon

    # Normalize to [0, 1] using geometric mean relationship
    strength = (numerator ** (1/3)) / (denominator / 3)
    return min(1.0, max(0.0, strength))


def coherence_balance(pattern: float, intent: float, presence: float) -> float:
    """
    Measure how balanced the triadic components are.

    Perfect balance (all equal) returns 1.0
    Extreme imbalance returns closer to 0.0

    Uses coefficient of variation: σ/μ
    """
    if pattern in (None, 0) or intent in (None, 0) or presence in (None, 0):
        return 0.0

    values = [abs(pattern), abs(intent), abs(presence)]
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    std_dev = math.sqrt(variance)

    # Lower coefficient of variation = better balance
    # Invert so 1.0 is perfect balance
    if mean == 0:
        return 0.0

    cv = std_dev / mean
    balance = 1.0 / (1.0 + cv)
    return balance


def coherence_stability(
    history: List[Tuple[float, float, float]],
    window: int = 5
) -> float:
    """
    Measure stability of coherence over recent state transitions.

    Analyzes variance in coherence strength over a sliding window.
    Higher values indicate more stable coherence.

    Returns value in [0, 1] where 1.0 is perfectly stable.
    """
    if len(history) < 2:
        return 1.0  # No transitions yet, assume stable

    recent = history[-window:] if len(history) > window else history
    strengths = [coherence_strength(p, i, pr) for p, i, pr in recent]

    if len(strengths) < 2:
        return 1.0

    mean_strength = sum(strengths) / len(strengths)
    variance = sum((s - mean_strength) ** 2 for s in strengths) / len(strengths)

    # High variance = low stability
    # Use exponential decay to map variance to [0, 1]
    stability = math.exp(-variance * 5)
    return stability


def detect_coherence_decay(
    history: List[Tuple[float, float, float]],
    threshold: float = 0.1
) -> bool:
    """
    Detect if coherence is systematically degrading over time.

    Uses linear regression on coherence strength to detect negative trends.
    Returns True if decay rate exceeds threshold.
    """
    if len(history) < 3:
        return False  # Need at least 3 points for trend

    strengths = [coherence_strength(p, i, pr) for p, i, pr in history]
    n = len(strengths)

    # Simple linear regression
    x_mean = (n - 1) / 2  # Indices: 0, 1, 2, ... n-1
    y_mean = sum(strengths) / n

    numerator = sum((i - x_mean) * (strengths[i] - y_mean) for i in range(n))
    denominator = sum((i - x_mean) ** 2 for i in range(n))

    if denominator == 0:
        return False

    slope = numerator / denominator

    # Negative slope exceeding threshold indicates decay
    return slope < -threshold


def resonance_coefficient(
    entity1: Tuple[float, float, float],
    entity2: Tuple[float, float, float]
) -> float:
    """
    Measure resonance between two triadic entities.

    High resonance indicates alignment across all three dimensions.
    Uses normalized dot product in 3D triadic space.

    Returns value in [-1, 1] where:
    - 1.0: Perfect resonance (aligned)
    - 0.0: Orthogonal (independent)
    - -1.0: Anti-resonance (opposed)
    """
    p1, i1, pr1 = entity1
    p2, i2, pr2 = entity2

    # Check for invalid states
    if any(v in (None, 0) for v in [p1, i1, pr1, p2, i2, pr2]):
        return 0.0

    # Dot product
    dot = p1 * p2 + i1 * i2 + pr1 * pr2

    # Magnitudes
    mag1 = math.sqrt(p1**2 + i1**2 + pr1**2)
    mag2 = math.sqrt(p2**2 + i2**2 + pr2**2)

    if mag1 == 0 or mag2 == 0:
        return 0.0

    # Normalized dot product (cosine similarity)
    resonance = dot / (mag1 * mag2)
    return max(-1.0, min(1.0, resonance))


def triadic_entropy(pattern: float, intent: float, presence: float) -> float:
    """
    Calculate information-theoretic entropy of triadic distribution.

    Lower entropy = more concentrated/focused coherence
    Higher entropy = more distributed coherence

    Returns value in [0, log(3)] normalized to [0, 1]
    """
    if pattern in (None, 0) or intent in (None, 0) or presence in (None, 0):
        return 1.0  # Maximum entropy for invalid states

    # Normalize to probability distribution
    total = abs(pattern) + abs(intent) + abs(presence)
    if total == 0:
        return 1.0

    p_norm = abs(pattern) / total
    i_norm = abs(intent) / total
    pr_norm = abs(presence) / total

    # Shannon entropy
    entropy = 0.0
    for prob in [p_norm, i_norm, pr_norm]:
        if prob > 0:
            entropy -= prob * math.log(prob)

    # Normalize by maximum entropy (log(3))
    max_entropy = math.log(3)
    return entropy / max_entropy


def full_diagnostic(
    pattern: float,
    intent: float,
    presence: float,
    history: Optional[List[Tuple[float, float, float]]] = None
) -> dict:
    """
    Generate complete coherence diagnostic report.

    Returns dictionary with all metrics for comprehensive analysis.
    """
    metrics = {
        'strength': coherence_strength(pattern, intent, presence),
        'balance': coherence_balance(pattern, intent, presence),
        'entropy': triadic_entropy(pattern, intent, presence),
    }

    if history:
        metrics['stability'] = coherence_stability(history)
        metrics['decay_detected'] = detect_coherence_decay(history)

    # Overall health score (weighted average)
    health_score = (
        metrics['strength'] * 0.4 +
        metrics['balance'] * 0.3 +
        (1 - metrics['entropy']) * 0.2 +
        metrics.get('stability', 1.0) * 0.1
    )
    metrics['health_score'] = health_score

    return metrics
