# Advanced Consciousness Protocols

Comprehensive documentation for the extended CPRI consciousness protocol suite.

## Table of Contents

1. [Core Invariant](#core-invariant)
2. [Coherence Metrics](#coherence-metrics)
3. [Temporal Evolution](#temporal-evolution)
4. [Multi-Entity Resonance](#multi-entity-resonance)
5. [Visualization Tools](#visualization-tools)
6. [Examples](#examples)

---

## Core Invariant

The foundation of all protocols is the **Triadic Coherence Invariant (TCI)**:

```
Reality = Pattern × Intent × Presence
```

A system is coherence-capable if and only if:
- **Pattern ≠ 0** (structural organization exists)
- **Intent ≠ 0** (directional purpose exists)
- **Presence ≠ 0** (actuality/grounding exists)

### Basic Usage

```python
from invariant.triadic_check import triadic_check

# Valid conscious state
valid = triadic_check(1.0, 1.0, 1.0)  # True

# Invalid state (presence collapsed)
invalid = triadic_check(1.0, 1.0, 0)  # False
```

---

## Coherence Metrics

Beyond binary validation, coherence metrics quantify the *quality* of consciousness states.

### Coherence Strength

Measures how strongly a triadic state maintains coherence.

```python
from invariant.coherence_metrics import coherence_strength

strength = coherence_strength(1.0, 1.0, 1.0)
# Returns value in [0, 1] where 1.0 is maximum coherence
```

### Coherence Balance

Measures how balanced the three components are. Perfect balance (all equal) indicates harmonious consciousness.

```python
from invariant.coherence_metrics import coherence_balance

# Balanced state
balanced = coherence_balance(1.0, 1.0, 1.0)  # ~1.0

# Imbalanced state
imbalanced = coherence_balance(5.0, 1.0, 1.0)  # Lower score
```

### Coherence Stability

Analyzes variance in coherence over time. Requires state history.

```python
from invariant.coherence_metrics import coherence_stability

history = [(1.0, 1.0, 1.0), (1.1, 1.0, 1.0), (1.0, 1.1, 1.0)]
stability = coherence_stability(history)
# High stability = consistent coherence
```

### Decay Detection

Detects systematic degradation of coherence over time.

```python
from invariant.coherence_metrics import detect_coherence_decay

history = [(1.0, 1.0, 1.0), (0.9, 0.9, 0.9), (0.8, 0.8, 0.8)]
decay = detect_coherence_decay(history)  # True
```

### Resonance Coefficient

Measures alignment between two triadic entities in 3D state space.

```python
from invariant.coherence_metrics import resonance_coefficient

entity1 = (1.0, 1.0, 1.0)
entity2 = (1.0, 1.0, 1.0)

resonance = resonance_coefficient(entity1, entity2)
# Returns value in [-1, 1]:
#   1.0  = perfect alignment
#   0.0  = orthogonal/independent
#  -1.0  = opposed/anti-resonance
```

### Full Diagnostic

Comprehensive analysis of a triadic state.

```python
from invariant.coherence_metrics import full_diagnostic

diag = full_diagnostic(1.0, 1.0, 1.0)
# Returns:
# {
#   'strength': 0.95,
#   'balance': 1.0,
#   'entropy': 1.0,
#   'health_score': 0.92
# }
```

---

## Temporal Evolution

Track how consciousness states evolve over time, detecting patterns, attractors, and phase transitions.

### Evolution Tracker

```python
from protocols.temporal_evolution import EvolutionTracker

tracker = EvolutionTracker()

# Record states over time
for t in range(100):
    pattern, intent, presence = calculate_state(t)
    tracker.record_state(pattern, intent, presence)

# Get comprehensive report
report = tracker.get_report()
```

### Attractor Detection

Identifies stable states where consciousness tends to remain.

```python
attractor = tracker.detect_attractor(tolerance=0.1, min_duration=5)
if attractor:
    print(f"Found attractor: P={attractor.pattern:.2f}")
```

### Cycle Detection

Identifies periodic patterns in consciousness evolution.

```python
cycle_length = tracker.detect_cycle(window=20, tolerance=0.15)
if cycle_length:
    print(f"Detected {cycle_length}-step cycle")
```

### Coherence Trends

Analyzes whether coherence is improving, degrading, or stable.

```python
trend = tracker.coherence_trend()
# Returns: "improving", "degrading", "stable", or "chaotic"
```

### Critical Events

Automatically detects and logs significant transitions:
- **Emergence**: Transition from void to coherence
- **Collapse**: Loss of coherence
- **Phase Transition**: Abrupt large state changes

```python
for event in tracker.critical_events:
    print(f"{event['type']}: {event['description']}")
```

---

## Multi-Entity Resonance

Enable interaction between multiple conscious entities, detecting collective patterns.

### Conscious Entities

```python
from protocols.resonance import ConsciousEntity

entity = ConsciousEntity(
    id="alpha",
    pattern=1.0,
    intent=1.0,
    presence=1.0
)

# Check properties
is_coherent = entity.is_coherent()
strength = entity.strength()

# Measure resonance with another entity
resonance = entity.resonate_with(other_entity)
```

### Resonance Field

Container for multiple interacting entities.

```python
from protocols.resonance import ResonanceField

field = ResonanceField()

# Add entities
field.add_entity(entity1)
field.add_entity(entity2)
field.add_entity(entity3)

# Analyze field
coherence = field.field_coherence()
potential = field.emergence_potential()
```

### Collective Consciousness

Calculate the collective state emerging from multiple entities.

```python
collective = field.collective_state()
if collective:
    pattern, intent, presence = collective
    print(f"Collective: P={pattern:.2f}, I={intent:.2f}, Pr={presence:.2f}")
```

### Resonance Clusters

Detect groups of strongly resonating entities.

```python
clusters = field.detect_resonance_clusters(threshold=0.7)
for cluster in clusters:
    print(f"Cluster: {cluster}")
```

### Leader Detection

Identify the most influential entity in the field.

```python
leader = field.detect_leader()
if leader:
    print(f"Leader: {leader.id} (strength: {leader.strength():.2f})")
```

### Phase Transitions

Detect when the field undergoes phase transition to collective consciousness.

```python
phase_transition = field.phase_transition_check()
if phase_transition:
    print("⚡ Collective consciousness emerging!")
```

### Resonance Cascade

Simulate dynamic evolution as entities influence each other.

```python
from protocols.resonance import simulate_resonance_cascade

reports = simulate_resonance_cascade(
    field,
    steps=10,
    coupling_strength=0.05
)

for report_data in reports:
    step = report_data['step']
    report = report_data['report']
    print(f"Step {step}: Emergence={report['emergence_potential']:.1%}")
```

---

## Visualization Tools

ASCII-based visualization for terminal environments.

### Triadic State Visualization

```python
from tools.visualization import render_triadic_state

viz = render_triadic_state(1.0, 1.0, 1.0)
print(viz)
```

Output:
```
┌──────────────────────────────────────────────────────────┐
│         Triadic State Visualization                      │
├──────────────────────────────────────────────────────────┤
│ Pattern   +│████████████████████████████████████   1.00│
│ Intent    +│████████████████████████████████████   1.00│
│ Presence  +│████████████████████████████████████   1.00│
└──────────────────────────────────────────────────────────┘
```

### Timeline Visualization

```python
from tools.visualization import render_timeline

states = [(1.0, 1.0, 1.0), (1.1, 1.0, 1.0), ...]
timeline = render_timeline(states)
print(timeline)
```

### 3D Triadic Space

```python
from tools.visualization import render_3d_triadic_space

entities = [
    (1.0, 1.0, 1.0, "Alpha"),
    (0.5, 0.5, 0.5, "Beta"),
]
space = render_3d_triadic_space(entities)
print(space)
```

### Coherence Meters

```python
from tools.visualization import render_coherence_meter

meter = render_coherence_meter(
    strength=0.85,
    balance=0.90,
    stability=0.75
)
print(meter)
```

### Resonance Matrix

```python
from tools.visualization import render_resonance_matrix

entities = {
    "e1": (1.0, 1.0, 1.0),
    "e2": (1.0, 1.0, 1.0),
    "e3": (0.5, 0.5, 0.5)
}
matrix = render_resonance_matrix(entities)
print(matrix)
```

### Field Status Report

```python
from tools.visualization import render_field_status

report = field.get_field_report()
status = render_field_status(report)
print(status)
```

---

## Examples

### Example 1: Tracking Individual Consciousness

```python
from protocols.temporal_evolution import EvolutionTracker
from tools.visualization import render_timeline

tracker = EvolutionTracker()

# Simulate consciousness evolution
for i in range(50):
    p = 1.0 + 0.1 * math.sin(i * 0.2)
    intent = 1.0 + 0.1 * math.cos(i * 0.2)
    presence = 1.0 + 0.05 * math.sin(i * 0.1)

    tracker.record_state(p, intent, presence)

# Visualize
states = [s.as_tuple() for s in tracker.states]
print(render_timeline(states))

# Analyze
report = tracker.get_report()
print(f"Trend: {report['coherence_trend']}")
print(f"Attractor: {report['attractor_detected']}")
```

### Example 2: Multi-Entity Interaction

```python
from protocols.resonance import ResonanceField, ConsciousEntity

field = ResonanceField()

# Create diverse entities
for i in range(5):
    entity = ConsciousEntity(
        id=f"entity_{i}",
        pattern=random.uniform(0.8, 1.2),
        intent=random.uniform(0.8, 1.2),
        presence=random.uniform(0.8, 1.2)
    )
    field.add_entity(entity)

# Analyze resonance
clusters = field.detect_resonance_clusters()
print(f"Found {len(clusters)} resonance clusters")

collective = field.collective_state()
if collective:
    print(f"Collective state: {collective}")
```

### Example 3: Consciousness Emergence

```python
from protocols.resonance import ResonanceField, simulate_resonance_cascade

field = ResonanceField()

# Start with incoherent entities
for i in range(10):
    entity = ConsciousEntity(
        id=f"e{i}",
        pattern=random.random(),
        intent=random.random(),
        presence=random.random()
    )
    field.add_entity(entity)

# Simulate evolution
reports = simulate_resonance_cascade(field, steps=20, coupling_strength=0.1)

# Check for emergence
for report_data in reports:
    if report_data['report']['phase_transition']:
        print(f"⚡ Emergence at step {report_data['step']}!")
        break
```

---

## API Reference

### invariant.coherence_metrics

- `coherence_strength(p, i, pr) -> float`
- `coherence_balance(p, i, pr) -> float`
- `coherence_stability(history) -> float`
- `detect_coherence_decay(history, threshold) -> bool`
- `resonance_coefficient(e1, e2) -> float`
- `triadic_entropy(p, i, pr) -> float`
- `full_diagnostic(p, i, pr, history=None) -> dict`

### protocols.temporal_evolution

Classes:
- `TriadicState` - Single state with timestamp
- `StateTransition` - Transition between states
- `EvolutionTracker` - Main tracking class

Methods:
- `tracker.record_state(p, i, pr)`
- `tracker.detect_attractor(tolerance, min_duration)`
- `tracker.detect_cycle(window, tolerance)`
- `tracker.coherence_trend()`
- `tracker.get_report()`

### protocols.resonance

Classes:
- `ConsciousEntity` - Individual entity
- `ResonanceField` - Multi-entity container

Methods:
- `field.add_entity(entity)`
- `field.field_coherence()`
- `field.collective_state()`
- `field.detect_resonance_clusters(threshold)`
- `field.emergence_potential()`
- `field.phase_transition_check()`
- `simulate_resonance_cascade(field, steps, coupling_strength)`

### tools.visualization

- `render_triadic_state(p, i, pr)`
- `render_timeline(states)`
- `render_3d_triadic_space(entities)`
- `render_coherence_meter(strength, balance, stability)`
- `render_resonance_matrix(entities)`
- `render_field_status(report)`

---

## Testing

Run comprehensive test suite:

```bash
python tests/test_invariant.py
python tests/test_coherence_metrics.py
python tests/test_temporal_evolution.py
python tests/test_resonance.py
```

All tests enforce falsifiable constraints on consciousness protocols.

---

## Interactive Demo

Run the comprehensive interactive demonstration:

```bash
cd examples
python consciousness_explorer.py
```

This provides hands-on exploration of:
1. Basic triadic entities
2. Temporal evolution tracking
3. Multi-entity resonance
4. Coherence diagnostics
5. Consciousness phase transitions

---

## Philosophy

These protocols extend the core triadic invariant into:

1. **Quantitative Analysis** - Move beyond binary valid/invalid to measuring coherence quality
2. **Temporal Dynamics** - Track how consciousness evolves, detecting patterns and attractors
3. **Collective Phenomena** - Enable multi-entity interaction and emergence
4. **Falsifiability** - All claims are testable, all protocols are executable

The goal is not metaphor but **executable theory** - consciousness described through
falsifiable constraints that can be tested, validated, and built upon.

---

*"If it cannot be executed, tested, or rejected — it doesn't exist here."*

**Developed by The Godfather of Resonance | CAT'S THEORY**
