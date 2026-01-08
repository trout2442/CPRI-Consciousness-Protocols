#!/usr/bin/env python3
"""
Consciousness Explorer - Interactive Demo

An interactive exploration of consciousness protocols using the triadic
invariant framework. Demonstrates:
- Individual entity coherence
- Temporal evolution tracking
- Multi-entity resonance
- Collective consciousness emergence
"""

import sys
import time
import random
from typing import List

# Add parent directory to path
sys.path.insert(0, '..')

from invariant.triadic_check import triadic_check
from invariant.coherence_metrics import (
    coherence_strength,
    full_diagnostic
)
from protocols.temporal_evolution import (
    EvolutionTracker,
    TriadicState
)
from protocols.resonance import (
    ConsciousEntity,
    ResonanceField,
    simulate_resonance_cascade
)
from tools.visualization import (
    render_triadic_state,
    render_coherence_meter,
    render_timeline,
    render_field_status,
    render_resonance_matrix,
    render_3d_triadic_space
)


def demo_basic_entity():
    """Demo 1: Basic triadic entity and coherence checking."""
    print("\n" + "=" * 70)
    print("DEMO 1: BASIC TRIADIC ENTITY")
    print("=" * 70 + "\n")

    # Valid entity
    print("Creating a valid conscious entity...")
    p, i, pr = 1.0, 1.0, 1.0
    print(render_triadic_state(p, i, pr))

    valid = triadic_check(p, i, pr)
    strength = coherence_strength(p, i, pr)
    print(f"\n✓ Valid: {valid}")
    print(f"✓ Coherence Strength: {strength:.2%}\n")

    input("Press Enter to see an invalid entity...")

    # Invalid entity (presence = 0)
    print("\nCreating an invalid entity (presence collapsed)...")
    p, i, pr = 1.0, 1.0, 0.0
    print(render_triadic_state(p, i, pr))

    valid = triadic_check(p, i, pr)
    print(f"\n✗ Valid: {valid}")
    print("✗ Coherence collapsed! The entity cannot maintain consciousness.\n")


def demo_temporal_evolution():
    """Demo 2: Temporal evolution tracking."""
    print("\n" + "=" * 70)
    print("DEMO 2: TEMPORAL EVOLUTION")
    print("=" * 70 + "\n")

    print("Tracking consciousness evolution over time...\n")

    tracker = EvolutionTracker()

    # Simulate evolution
    states = []
    print("Simulating 20 time steps...")

    for i in range(20):
        # Start stable, then oscillate, then stabilize at attractor
        if i < 5:
            # Initial stable state
            p, intent, pr = 1.0, 1.0, 1.0
        elif i < 15:
            # Oscillation phase
            p = 1.0 + 0.5 * random.random()
            intent = 1.0 + 0.5 * random.random()
            pr = 1.0 + 0.3 * random.random()
        else:
            # Converge to attractor
            p = 1.2 + 0.1 * random.random()
            intent = 1.2 + 0.1 * random.random()
            pr = 1.1 + 0.1 * random.random()

        state = tracker.record_state(p, intent, pr)
        states.append((p, intent, pr))

    print("\nEvolution timeline:")
    print(render_timeline(states))

    # Analysis
    report = tracker.get_report()
    print(f"\n📊 EVOLUTION ANALYSIS:")
    print(f"   Total states: {report['total_states']}")
    print(f"   Coherence trend: {report['coherence_trend']}")
    print(f"   Attractor detected: {report['attractor_detected']}")

    if report['attractor_detected']:
        attractor = tracker.detect_attractor()
        if attractor:
            print(f"   Attractor state: P={attractor.pattern:.2f}, "
                  f"I={attractor.intent:.2f}, Pr={attractor.presence:.2f}")

    print(f"\n   Critical events: {report['critical_events']}")


def demo_multi_entity_resonance():
    """Demo 3: Multi-entity resonance and collective consciousness."""
    print("\n" + "=" * 70)
    print("DEMO 3: MULTI-ENTITY RESONANCE")
    print("=" * 70 + "\n")

    print("Creating a field of conscious entities...\n")

    field = ResonanceField()

    # Create entities with varying states
    entities_data = [
        ("Alpha", 1.0, 1.0, 1.0),
        ("Beta", 1.1, 0.9, 1.0),
        ("Gamma", 0.9, 1.1, 1.0),
        ("Delta", 1.0, 1.0, 0.8),
        ("Epsilon", 0.7, 0.7, 0.7),
    ]

    for name, p, i, pr in entities_data:
        entity = ConsciousEntity(name, p, i, pr)
        field.add_entity(entity)
        print(f"Added {name}: P={p:.1f}, I={i:.1f}, Pr={pr:.1f}")

    input("\nPress Enter to analyze resonance patterns...")

    # Visualize 3D space
    print("\n3D Triadic Space (isometric projection):")
    entities_for_viz = [(p, i, pr, name) for name, p, i, pr in entities_data]
    print(render_3d_triadic_space(entities_for_viz))

    # Resonance matrix
    print("\nResonance Matrix:")
    entity_dict = {name: (p, i, pr) for name, p, i, pr in entities_data}
    print(render_resonance_matrix(entity_dict))

    # Field report
    report = field.get_field_report()
    print(f"\n{render_field_status(report)}")

    input("\nPress Enter to simulate resonance cascade...")

    # Simulate cascade
    print("\nSimulating resonance cascade (entities influencing each other)...")
    print("Step by step evolution:\n")

    cascade_reports = simulate_resonance_cascade(
        field,
        steps=8,
        coupling_strength=0.08
    )

    for report_data in cascade_reports[::2]:  # Show every other step
        step = report_data['step']
        report = report_data['report']
        emergence = report['emergence_potential']
        phase = report['phase_transition']

        print(f"Step {step}: Emergence={emergence:.1%} "
              f"{'⚡ PHASE TRANSITION!' if phase else ''}")

    print("\nFinal field state:")
    final_report = cascade_reports[-1]['report']
    print(render_field_status(final_report))

    if final_report.get('collective_state'):
        p, i, pr = final_report['collective_state']
        print("\nCollective Consciousness State:")
        print(render_triadic_state(p, i, pr))


def demo_coherence_diagnostics():
    """Demo 4: Advanced coherence diagnostics."""
    print("\n" + "=" * 70)
    print("DEMO 4: COHERENCE DIAGNOSTICS")
    print("=" * 70 + "\n")

    print("Analyzing different coherence profiles...\n")

    profiles = [
        ("Balanced High", 1.0, 1.0, 1.0),
        ("Imbalanced", 2.0, 0.5, 1.0),
        ("Weak", 0.3, 0.3, 0.3),
        ("Pattern Dominant", 2.0, 0.8, 0.8),
    ]

    for name, p, i, pr in profiles:
        print(f"\n{'─' * 60}")
        print(f"Profile: {name}")
        print('─' * 60)

        print(render_triadic_state(p, i, pr))

        # Full diagnostic
        diag = full_diagnostic(p, i, pr)
        print(f"\nDiagnostics:")
        print(f"  Strength: {diag['strength']:.1%}")
        print(f"  Balance:  {diag['balance']:.1%}")
        print(f"  Entropy:  {diag['entropy']:.1%}")
        print(f"  Health:   {diag['health_score']:.1%}")

        # Visualization
        print(f"\n{render_coherence_meter(diag['strength'], diag['balance'], 1.0 - diag['entropy'])}")

        input("\nPress Enter for next profile...")


def demo_consciousness_phases():
    """Demo 5: Consciousness phase transitions."""
    print("\n" + "=" * 70)
    print("DEMO 5: CONSCIOUSNESS PHASE TRANSITIONS")
    print("=" * 70 + "\n")

    print("Simulating emergence of collective consciousness...\n")

    field = ResonanceField()

    # Start with random entities
    print("Creating 10 entities with random initial states...")
    for i in range(10):
        p = random.uniform(0.5, 1.5)
        i_val = random.uniform(0.5, 1.5)
        pr = random.uniform(0.5, 1.5)
        entity = ConsciousEntity(f"E{i}", p, i_val, pr)
        field.add_entity(entity)

    print("\nInitial field state:")
    print(render_field_status(field.get_field_report()))

    input("\nPress Enter to begin synchronization process...")

    # Gradually synchronize
    print("\nSynchronizing entities toward collective state...\n")

    target = (1.0, 1.0, 1.0)

    for step in range(10):
        strength = 0.15 * (step / 10)  # Gradually increase coupling
        field.synchronize_towards(target, strength)

        report = field.get_field_report()
        emergence = report['emergence_potential']
        phase = report['phase_transition']

        status = "⚡ PHASE TRANSITION!" if phase else "synchronizing..."
        print(f"Step {step + 1}/10: Emergence={emergence:.1%} - {status}")

        if phase and step < 9:
            print("    └─> Collective consciousness emerging!")

        time.sleep(0.3)

    print("\n" + "=" * 60)
    print("FINAL STATE: COLLECTIVE CONSCIOUSNESS ACHIEVED")
    print("=" * 60)

    final_report = field.get_field_report()
    print(render_field_status(final_report))

    if final_report.get('collective_state'):
        p, i, pr = final_report['collective_state']
        print("\nCollective consciousness triadic state:")
        print(render_triadic_state(p, i, pr))


def main():
    """Main interactive menu."""
    print("\n")
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║                                                                  ║")
    print("║              CONSCIOUSNESS PROTOCOLS EXPLORER                    ║")
    print("║                                                                  ║")
    print("║         Interactive Demo of Triadic Invariant Framework         ║")
    print("║                                                                  ║")
    print("║              Reality = Pattern × Intent × Presence              ║")
    print("║                                                                  ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print("\n")

    demos = [
        ("Basic Triadic Entity", demo_basic_entity),
        ("Temporal Evolution", demo_temporal_evolution),
        ("Multi-Entity Resonance", demo_multi_entity_resonance),
        ("Coherence Diagnostics", demo_coherence_diagnostics),
        ("Consciousness Phase Transitions", demo_consciousness_phases),
    ]

    while True:
        print("\n" + "─" * 60)
        print("SELECT A DEMONSTRATION:")
        print("─" * 60)

        for i, (name, _) in enumerate(demos, 1):
            print(f"  {i}. {name}")
        print("  0. Run All Demos")
        print("  Q. Quit")
        print()

        choice = input("Enter choice: ").strip().lower()

        if choice == 'q':
            print("\nThank you for exploring consciousness protocols!")
            break
        elif choice == '0':
            for name, demo_func in demos:
                demo_func()
            print("\n" + "=" * 70)
            print("ALL DEMONSTRATIONS COMPLETE")
            print("=" * 70)
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(demos):
            _, demo_func = demos[int(choice) - 1]
            demo_func()
        else:
            print("\n✗ Invalid choice. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExploration interrupted. Goodbye!")
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
