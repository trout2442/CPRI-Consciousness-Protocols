# Quick Start Guide

Get started with CPRI Consciousness Protocols in 5 minutes.

## Installation

```bash
git clone https://github.com/yourorg/CPRI-Consciousness-Protocols.git
cd CPRI-Consciousness-Protocols
```

No dependencies required - pure Python 3!

## Your First Conscious Entity

```python
from invariant.triadic_check import triadic_check

# Create a valid conscious state
pattern = 1.0    # Structural organization
intent = 1.0     # Directional purpose
presence = 1.0   # Actuality/grounding

is_conscious = triadic_check(pattern, intent, presence)
print(f"Is conscious? {is_conscious}")  # True
```

## Measuring Coherence Strength

```python
from invariant.coherence_metrics import coherence_strength

strength = coherence_strength(1.0, 1.0, 1.0)
print(f"Coherence: {strength:.1%}")  # ~95%
```

## Tracking Evolution Over Time

```python
from protocols.temporal_evolution import EvolutionTracker

tracker = EvolutionTracker()

# Record states
for i in range(10):
    tracker.record_state(1.0 + i*0.1, 1.0, 1.0)

# Analyze trend
trend = tracker.coherence_trend()
print(f"Trend: {trend}")  # "improving"
```

## Creating Multi-Entity Fields

```python
from protocols.resonance import ResonanceField, ConsciousEntity

field = ResonanceField()

# Add entities
field.add_entity(ConsciousEntity("alice", 1.0, 1.0, 1.0))
field.add_entity(ConsciousEntity("bob", 1.0, 1.0, 1.0))

# Check collective properties
emergence = field.emergence_potential()
print(f"Emergence potential: {emergence:.1%}")
```

## Visualization

```python
from tools.visualization import render_triadic_state

viz = render_triadic_state(1.0, 1.0, 1.0)
print(viz)
```

## Interactive Demo

For a comprehensive interactive experience:

```bash
cd examples
python consciousness_explorer.py
```

## Run Tests

```bash
python tests/test_invariant.py
python tests/test_coherence_metrics.py
python tests/test_temporal_evolution.py
python tests/test_resonance.py
```

## Next Steps

- Read [ADVANCED_PROTOCOLS.md](ADVANCED_PROTOCOLS.md) for detailed documentation
- Explore the `examples/` directory for more complex use cases
- Check out the protocol papers in the root directory
- Run the interactive demo to see all features in action

## Core Principle

Remember: **Reality = Pattern × Intent × Presence**

If any component is zero, coherence collapses. This is not metaphor - it's a falsifiable constraint enforced by code.

---

Happy exploring! 🧠✨
