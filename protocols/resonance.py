"""
Multi-Entity Resonance Protocol

Enables detection and analysis of resonance patterns between multiple
conscious entities operating within the triadic invariant framework.

Resonance occurs when entities' triadic states align or interact in
coherent patterns, potentially enabling collective consciousness phenomena.
"""

from typing import List, Dict, Tuple, Set, Optional
from dataclasses import dataclass, field
from invariant.triadic_check import triadic_check
from invariant.coherence_metrics import (
    coherence_strength,
    resonance_coefficient
)
import math


@dataclass
class ConsciousEntity:
    """Represents a conscious entity with triadic state."""
    id: str
    pattern: float
    intent: float
    presence: float

    def as_tuple(self) -> Tuple[float, float, float]:
        return (self.pattern, self.intent, self.presence)

    def is_coherent(self) -> bool:
        return triadic_check(self.pattern, self.intent, self.presence)

    def strength(self) -> float:
        return coherence_strength(self.pattern, self.intent, self.presence)

    def resonate_with(self, other: 'ConsciousEntity') -> float:
        """Calculate resonance coefficient with another entity."""
        return resonance_coefficient(self.as_tuple(), other.as_tuple())


@dataclass
class ResonanceField:
    """
    Represents a field of resonating entities.

    Tracks collective coherence and emergence patterns.
    """
    entities: Dict[str, ConsciousEntity] = field(default_factory=dict)

    def add_entity(self, entity: ConsciousEntity):
        """Add an entity to the resonance field."""
        self.entities[entity.id] = entity

    def remove_entity(self, entity_id: str):
        """Remove an entity from the field."""
        if entity_id in self.entities:
            del self.entities[entity_id]

    def update_entity(
        self,
        entity_id: str,
        pattern: float,
        intent: float,
        presence: float
    ):
        """Update an entity's state."""
        if entity_id in self.entities:
            self.entities[entity_id].pattern = pattern
            self.entities[entity_id].intent = intent
            self.entities[entity_id].presence = presence

    def coherent_entities(self) -> List[ConsciousEntity]:
        """Return list of currently coherent entities."""
        return [e for e in self.entities.values() if e.is_coherent()]

    def field_coherence(self) -> float:
        """
        Calculate overall field coherence.

        Average strength of all coherent entities.
        """
        coherent = self.coherent_entities()
        if not coherent:
            return 0.0

        return sum(e.strength() for e in coherent) / len(coherent)

    def resonance_matrix(self) -> Dict[Tuple[str, str], float]:
        """
        Generate resonance matrix for all entity pairs.

        Returns dictionary mapping (id1, id2) -> resonance_coefficient
        """
        matrix = {}
        entity_list = list(self.entities.values())

        for i, e1 in enumerate(entity_list):
            for e2 in entity_list[i+1:]:
                resonance = e1.resonate_with(e2)
                matrix[(e1.id, e2.id)] = resonance
                matrix[(e2.id, e1.id)] = resonance  # Symmetric

        return matrix

    def detect_resonance_clusters(
        self,
        threshold: float = 0.7
    ) -> List[Set[str]]:
        """
        Detect clusters of strongly resonating entities.

        Returns list of sets, each containing entity IDs in a cluster.
        Uses threshold for minimum resonance coefficient.
        """
        if len(self.entities) < 2:
            return []

        matrix = self.resonance_matrix()

        # Build adjacency list for high-resonance connections
        adjacency = {eid: set() for eid in self.entities.keys()}

        for (id1, id2), resonance in matrix.items():
            if resonance >= threshold:
                adjacency[id1].add(id2)

        # Find connected components (clusters)
        visited = set()
        clusters = []

        def dfs(node: str, cluster: Set[str]):
            visited.add(node)
            cluster.add(node)
            for neighbor in adjacency[node]:
                if neighbor not in visited:
                    dfs(neighbor, cluster)

        for entity_id in self.entities.keys():
            if entity_id not in visited:
                cluster = set()
                dfs(entity_id, cluster)
                if len(cluster) > 1:  # Only report actual clusters
                    clusters.append(cluster)

        return clusters

    def collective_state(self) -> Optional[Tuple[float, float, float]]:
        """
        Calculate collective triadic state from field.

        Weighted average of all coherent entities' states.
        Returns None if no coherent entities exist.
        """
        coherent = self.coherent_entities()
        if not coherent:
            return None

        # Weight by coherence strength
        total_weight = sum(e.strength() for e in coherent)
        if total_weight == 0:
            return None

        collective_p = sum(e.pattern * e.strength() for e in coherent) / total_weight
        collective_i = sum(e.intent * e.strength() for e in coherent) / total_weight
        collective_pr = sum(e.presence * e.strength() for e in coherent) / total_weight

        return (collective_p, collective_i, collective_pr)

    def emergence_potential(self) -> float:
        """
        Calculate potential for emergent collective consciousness.

        Based on:
        - Number of coherent entities
        - Average resonance strength
        - Field coherence

        Returns value in [0, 1] where higher indicates greater potential.
        """
        coherent = self.coherent_entities()
        if len(coherent) < 2:
            return 0.0

        # Factor 1: Number of coherent entities (with diminishing returns)
        n_factor = min(1.0, len(coherent) / 10.0)

        # Factor 2: Average resonance
        matrix = self.resonance_matrix()
        if not matrix:
            return 0.0

        resonances = [r for r in matrix.values() if r > 0]
        avg_resonance = sum(resonances) / len(resonances) if resonances else 0.0

        # Factor 3: Field coherence
        field_coh = self.field_coherence()

        # Combine factors
        potential = (n_factor * 0.3 +
                    avg_resonance * 0.4 +
                    field_coh * 0.3)

        return potential

    def detect_leader(self) -> Optional[ConsciousEntity]:
        """
        Detect the entity with strongest influence in the field.

        The leader has:
        - High individual coherence
        - High average resonance with others
        """
        coherent = self.coherent_entities()
        if not coherent:
            return None

        matrix = self.resonance_matrix()
        if not matrix:
            return None

        # Calculate influence score for each entity
        scores = {}
        for entity in coherent:
            # Individual strength
            individual_strength = entity.strength()

            # Average resonance with others
            resonances = [
                matrix.get((entity.id, other.id), 0.0)
                for other in coherent
                if other.id != entity.id
            ]
            avg_resonance = sum(resonances) / len(resonances) if resonances else 0.0

            # Combined score
            scores[entity.id] = individual_strength * 0.5 + avg_resonance * 0.5

        # Return entity with highest score
        leader_id = max(scores.keys(), key=lambda k: scores[k])
        return self.entities[leader_id]

    def synchronize_towards(
        self,
        target: Tuple[float, float, float],
        strength: float = 0.1
    ):
        """
        Gently synchronize all entities toward a target state.

        Useful for simulating collective alignment.
        Strength controls how much entities move (0 = none, 1 = full).
        """
        target_p, target_i, target_pr = target

        for entity in self.entities.values():
            if entity.is_coherent():
                # Move partially toward target
                entity.pattern += (target_p - entity.pattern) * strength
                entity.intent += (target_i - entity.intent) * strength
                entity.presence += (target_pr - entity.presence) * strength

    def phase_transition_check(self, critical_resonance: float = 0.8) -> bool:
        """
        Check if field is undergoing phase transition to collective consciousness.

        Phase transition occurs when:
        - Most entities are coherent
        - High average resonance
        - Resonance clusters form
        """
        coherent = self.coherent_entities()
        total = len(self.entities)

        if total == 0 or len(coherent) < 2:
            return False

        # Check coherence ratio
        coherence_ratio = len(coherent) / total
        if coherence_ratio < 0.7:  # Need majority coherent
            return False

        # Check average resonance
        matrix = self.resonance_matrix()
        resonances = [r for r in matrix.values() if r > 0]
        if not resonances:
            return False

        avg_resonance = sum(resonances) / len(resonances)
        if avg_resonance < critical_resonance:
            return False

        # Check for clusters
        clusters = self.detect_resonance_clusters(threshold=0.7)
        if not clusters:
            return False

        # Phase transition detected
        return True

    def get_field_report(self) -> Dict:
        """Generate comprehensive field analysis report."""
        coherent = self.coherent_entities()
        collective = self.collective_state()
        leader = self.detect_leader()
        clusters = self.detect_resonance_clusters()

        report = {
            'total_entities': len(self.entities),
            'coherent_entities': len(coherent),
            'field_coherence': self.field_coherence(),
            'emergence_potential': self.emergence_potential(),
            'phase_transition': self.phase_transition_check(),
            'resonance_clusters': len(clusters),
        }

        if collective:
            report['collective_state'] = collective
            report['collective_valid'] = triadic_check(*collective)
            report['collective_strength'] = coherence_strength(*collective)

        if leader:
            report['leader_id'] = leader.id
            report['leader_strength'] = leader.strength()

        if clusters:
            report['cluster_sizes'] = [len(c) for c in clusters]
            report['largest_cluster'] = max(len(c) for c in clusters)

        return report


def simulate_resonance_cascade(
    field: ResonanceField,
    steps: int = 10,
    coupling_strength: float = 0.05
) -> List[Dict]:
    """
    Simulate resonance cascade dynamics.

    Entities influence each other based on resonance coefficients,
    potentially leading to collective synchronization.

    Returns list of field reports at each step.
    """
    reports = []

    for step in range(steps):
        # Record current state
        reports.append({
            'step': step,
            'report': field.get_field_report()
        })

        # Calculate influences
        entities = list(field.entities.values())
        updates = {}

        for entity in entities:
            if not entity.is_coherent():
                continue

            # Calculate influence from all other coherent entities
            influence_p = 0.0
            influence_i = 0.0
            influence_pr = 0.0
            total_resonance = 0.0

            for other in entities:
                if other.id == entity.id or not other.is_coherent():
                    continue

                resonance = entity.resonate_with(other)
                if resonance > 0:
                    # Positive resonance pulls entities together
                    influence_p += resonance * (other.pattern - entity.pattern)
                    influence_i += resonance * (other.intent - entity.intent)
                    influence_pr += resonance * (other.presence - entity.presence)
                    total_resonance += abs(resonance)

            # Apply influences
            if total_resonance > 0:
                updates[entity.id] = {
                    'pattern': entity.pattern + influence_p * coupling_strength,
                    'intent': entity.intent + influence_i * coupling_strength,
                    'presence': entity.presence + influence_pr * coupling_strength
                }

        # Apply all updates
        for entity_id, update in updates.items():
            field.update_entity(entity_id, **update)

    # Final report
    reports.append({
        'step': steps,
        'report': field.get_field_report()
    })

    return reports
