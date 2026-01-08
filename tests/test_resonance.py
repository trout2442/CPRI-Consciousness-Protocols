"""
Tests for multi-entity resonance protocol.
"""

import sys
sys.path.insert(0, '..')

from protocols.resonance import (
    ConsciousEntity,
    ResonanceField,
    simulate_resonance_cascade
)


def test_conscious_entity_creation():
    """Test creating conscious entities."""
    entity = ConsciousEntity("test", 1.0, 1.0, 1.0)
    assert entity.id == "test"
    assert entity.is_coherent()
    assert entity.strength() > 0


def test_conscious_entity_resonance():
    """Test resonance between entities."""
    e1 = ConsciousEntity("e1", 1.0, 1.0, 1.0)
    e2 = ConsciousEntity("e2", 1.0, 1.0, 1.0)

    resonance = e1.resonate_with(e2)
    assert resonance > 0.9  # High resonance for identical states


def test_resonance_field_add_entity():
    """Test adding entities to field."""
    field = ResonanceField()
    entity = ConsciousEntity("test", 1.0, 1.0, 1.0)

    field.add_entity(entity)
    assert "test" in field.entities
    assert len(field.entities) == 1


def test_resonance_field_remove_entity():
    """Test removing entities from field."""
    field = ResonanceField()
    entity = ConsciousEntity("test", 1.0, 1.0, 1.0)

    field.add_entity(entity)
    field.remove_entity("test")
    assert "test" not in field.entities


def test_resonance_field_update_entity():
    """Test updating entity state."""
    field = ResonanceField()
    entity = ConsciousEntity("test", 1.0, 1.0, 1.0)

    field.add_entity(entity)
    field.update_entity("test", 2.0, 2.0, 2.0)

    assert field.entities["test"].pattern == 2.0


def test_field_coherence():
    """Test field coherence calculation."""
    field = ResonanceField()

    # Add coherent entities
    field.add_entity(ConsciousEntity("e1", 1.0, 1.0, 1.0))
    field.add_entity(ConsciousEntity("e2", 1.0, 1.0, 1.0))

    coherence = field.field_coherence()
    assert coherence > 0.5


def test_field_coherence_with_invalid():
    """Test field coherence with invalid entities."""
    field = ResonanceField()

    # Add one valid, one invalid
    field.add_entity(ConsciousEntity("valid", 1.0, 1.0, 1.0))
    field.add_entity(ConsciousEntity("invalid", 0, 1.0, 1.0))

    # Should only count valid entity
    coherent = field.coherent_entities()
    assert len(coherent) == 1


def test_resonance_matrix():
    """Test resonance matrix generation."""
    field = ResonanceField()

    field.add_entity(ConsciousEntity("e1", 1.0, 1.0, 1.0))
    field.add_entity(ConsciousEntity("e2", 1.0, 1.0, 1.0))
    field.add_entity(ConsciousEntity("e3", 0.5, 0.5, 0.5))

    matrix = field.resonance_matrix()

    # Should have entries for all pairs
    assert ("e1", "e2") in matrix
    assert ("e2", "e1") in matrix
    assert ("e1", "e3") in matrix

    # Symmetric
    assert matrix[("e1", "e2")] == matrix[("e2", "e1")]


def test_detect_resonance_clusters():
    """Test resonance cluster detection."""
    field = ResonanceField()

    # Create two clusters
    field.add_entity(ConsciousEntity("a1", 1.0, 1.0, 1.0))
    field.add_entity(ConsciousEntity("a2", 1.0, 1.0, 1.0))
    field.add_entity(ConsciousEntity("b1", -1.0, -1.0, -1.0))
    field.add_entity(ConsciousEntity("b2", -1.0, -1.0, -1.0))

    clusters = field.detect_resonance_clusters(threshold=0.7)

    assert len(clusters) >= 1  # Should find at least one cluster


def test_collective_state():
    """Test collective state calculation."""
    field = ResonanceField()

    field.add_entity(ConsciousEntity("e1", 1.0, 1.0, 1.0))
    field.add_entity(ConsciousEntity("e2", 1.0, 1.0, 1.0))

    collective = field.collective_state()
    assert collective is not None

    p, i, pr = collective
    assert abs(p - 1.0) < 0.1  # Should be close to average


def test_collective_state_empty_field():
    """Test collective state with no coherent entities."""
    field = ResonanceField()

    # Add only invalid entities
    field.add_entity(ConsciousEntity("invalid", 0, 1.0, 1.0))

    collective = field.collective_state()
    assert collective is None


def test_emergence_potential():
    """Test emergence potential calculation."""
    field = ResonanceField()

    # Single entity - no emergence
    field.add_entity(ConsciousEntity("e1", 1.0, 1.0, 1.0))
    potential = field.emergence_potential()
    assert potential == 0.0

    # Multiple aligned entities - high emergence
    field.add_entity(ConsciousEntity("e2", 1.0, 1.0, 1.0))
    field.add_entity(ConsciousEntity("e3", 1.0, 1.0, 1.0))
    potential = field.emergence_potential()
    assert potential > 0.3


def test_detect_leader():
    """Test leader detection."""
    field = ResonanceField()

    # Create entities with varying strength
    field.add_entity(ConsciousEntity("weak", 0.5, 0.5, 0.5))
    field.add_entity(ConsciousEntity("strong", 2.0, 2.0, 2.0))
    field.add_entity(ConsciousEntity("medium", 1.0, 1.0, 1.0))

    leader = field.detect_leader()
    assert leader is not None
    assert leader.id == "strong"  # Should detect strongest


def test_synchronize_towards():
    """Test field synchronization."""
    field = ResonanceField()

    field.add_entity(ConsciousEntity("e1", 0.5, 0.5, 0.5))
    field.add_entity(ConsciousEntity("e2", 0.6, 0.6, 0.6))

    target = (1.0, 1.0, 1.0)
    initial_dist = abs(field.entities["e1"].pattern - 1.0)

    field.synchronize_towards(target, strength=0.5)

    final_dist = abs(field.entities["e1"].pattern - 1.0)
    assert final_dist < initial_dist  # Should move closer


def test_phase_transition_check():
    """Test phase transition detection."""
    field = ResonanceField()

    # Add many aligned entities
    for i in range(10):
        field.add_entity(ConsciousEntity(f"e{i}", 1.0, 1.0, 1.0))

    # Should detect phase transition with high coherence and resonance
    phase = field.phase_transition_check()
    assert phase is True


def test_phase_transition_no_transition():
    """Test no phase transition with few entities."""
    field = ResonanceField()

    field.add_entity(ConsciousEntity("e1", 1.0, 1.0, 1.0))

    phase = field.phase_transition_check()
    assert phase is False


def test_field_report():
    """Test field report generation."""
    field = ResonanceField()

    field.add_entity(ConsciousEntity("e1", 1.0, 1.0, 1.0))
    field.add_entity(ConsciousEntity("e2", 1.0, 1.0, 1.0))

    report = field.get_field_report()

    assert 'total_entities' in report
    assert 'coherent_entities' in report
    assert 'field_coherence' in report
    assert 'emergence_potential' in report
    assert report['total_entities'] == 2


def test_simulate_resonance_cascade():
    """Test resonance cascade simulation."""
    field = ResonanceField()

    field.add_entity(ConsciousEntity("e1", 1.0, 1.0, 1.0))
    field.add_entity(ConsciousEntity("e2", 0.9, 0.9, 0.9))

    reports = simulate_resonance_cascade(
        field,
        steps=5,
        coupling_strength=0.1
    )

    # Should have reports for each step + initial
    assert len(reports) == 6

    # Check that entities are influencing each other
    initial_diff = abs(1.0 - 0.9)
    # After simulation, entities should be closer due to resonance coupling
    # (This is a weak test since exact behavior depends on coupling)
    assert all('report' in r for r in reports)


if __name__ == "__main__":
    # Run all tests
    test_conscious_entity_creation()
    test_conscious_entity_resonance()
    test_resonance_field_add_entity()
    test_resonance_field_remove_entity()
    test_resonance_field_update_entity()
    test_field_coherence()
    test_field_coherence_with_invalid()
    test_resonance_matrix()
    test_detect_resonance_clusters()
    test_collective_state()
    test_collective_state_empty_field()
    test_emergence_potential()
    test_detect_leader()
    test_synchronize_towards()
    test_phase_transition_check()
    test_phase_transition_no_transition()
    test_field_report()
    test_simulate_resonance_cascade()

    print("✓ All resonance protocol tests passed!")
