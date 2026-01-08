"""
Temporal Evolution Protocol - Track Consciousness State Changes Over Time

Monitors how triadic entities evolve through state space, detecting
trajectories, attractors, and phase transitions in consciousness dynamics.
"""

from typing import List, Tuple, Optional, Dict
from dataclasses import dataclass, field
from datetime import datetime
from invariant.triadic_check import triadic_check
from invariant.coherence_metrics import (
    coherence_strength,
    coherence_balance,
    detect_coherence_decay
)


@dataclass
class TriadicState:
    """Represents a single triadic state with timestamp."""
    pattern: float
    intent: float
    presence: float
    timestamp: datetime = field(default_factory=datetime.now)

    def as_tuple(self) -> Tuple[float, float, float]:
        return (self.pattern, self.intent, self.presence)

    def is_valid(self) -> bool:
        return triadic_check(self.pattern, self.intent, self.presence)

    def strength(self) -> float:
        return coherence_strength(self.pattern, self.intent, self.presence)

    def balance(self) -> float:
        return coherence_balance(self.pattern, self.intent, self.presence)


@dataclass
class StateTransition:
    """Represents a transition between two states."""
    from_state: TriadicState
    to_state: TriadicState
    delta_pattern: float = 0.0
    delta_intent: float = 0.0
    delta_presence: float = 0.0
    transition_type: str = "unknown"

    def __post_init__(self):
        self.delta_pattern = self.to_state.pattern - self.from_state.pattern
        self.delta_intent = self.to_state.intent - self.from_state.intent
        self.delta_presence = self.to_state.presence - self.from_state.presence
        self.transition_type = self._classify_transition()

    def _classify_transition(self) -> str:
        """Classify the type of state transition."""
        from_valid = self.from_state.is_valid()
        to_valid = self.to_state.is_valid()

        if not from_valid and not to_valid:
            return "void_to_void"
        if not from_valid and to_valid:
            return "emergence"
        if from_valid and not to_valid:
            return "collapse"

        # Both valid - analyze dynamics
        from_strength = self.from_state.strength()
        to_strength = self.to_state.strength()

        if to_strength > from_strength * 1.1:
            return "amplification"
        elif to_strength < from_strength * 0.9:
            return "attenuation"
        else:
            return "maintenance"

    def magnitude(self) -> float:
        """Calculate magnitude of state change in triadic space."""
        return (self.delta_pattern**2 +
                self.delta_intent**2 +
                self.delta_presence**2) ** 0.5


class EvolutionTracker:
    """
    Tracks temporal evolution of triadic states.

    Maintains history, detects patterns, and identifies critical transitions.
    """

    def __init__(self, max_history: int = 1000):
        self.states: List[TriadicState] = []
        self.transitions: List[StateTransition] = []
        self.max_history = max_history
        self.critical_events: List[Dict] = []

    def record_state(
        self,
        pattern: float,
        intent: float,
        presence: float,
        timestamp: Optional[datetime] = None
    ) -> TriadicState:
        """Record a new state in the evolution timeline."""
        state = TriadicState(
            pattern=pattern,
            intent=intent,
            presence=presence,
            timestamp=timestamp or datetime.now()
        )

        # Create transition if there's a previous state
        if self.states:
            transition = StateTransition(
                from_state=self.states[-1],
                to_state=state
            )
            self.transitions.append(transition)

            # Check for critical events
            self._check_critical_events(transition)

        self.states.append(state)

        # Maintain max history
        if len(self.states) > self.max_history:
            self.states.pop(0)
        if len(self.transitions) > self.max_history - 1:
            self.transitions.pop(0)

        return state

    def _check_critical_events(self, transition: StateTransition):
        """Detect and log critical events in evolution."""
        event = None

        if transition.transition_type == "emergence":
            event = {
                'type': 'emergence',
                'timestamp': transition.to_state.timestamp,
                'description': 'System emerged from void into coherence',
                'state': transition.to_state.as_tuple()
            }
        elif transition.transition_type == "collapse":
            event = {
                'type': 'collapse',
                'timestamp': transition.to_state.timestamp,
                'description': 'Coherence collapsed into void',
                'state': transition.to_state.as_tuple()
            }
        elif transition.magnitude() > 2.0:
            event = {
                'type': 'phase_transition',
                'timestamp': transition.to_state.timestamp,
                'description': f'Large state jump (magnitude: {transition.magnitude():.2f})',
                'state': transition.to_state.as_tuple()
            }

        if event:
            self.critical_events.append(event)

    def get_trajectory(self, window: int = 10) -> List[TriadicState]:
        """Get recent trajectory of states."""
        return self.states[-window:] if len(self.states) > window else self.states

    def detect_attractor(self, tolerance: float = 0.1, min_duration: int = 5) -> Optional[TriadicState]:
        """
        Detect if system is in an attractor state.

        An attractor is a state or region where the system tends to remain.
        Returns the attractor state if detected, None otherwise.
        """
        if len(self.states) < min_duration:
            return None

        recent = self.states[-min_duration:]

        # Calculate mean state
        mean_p = sum(s.pattern for s in recent) / len(recent)
        mean_i = sum(s.intent for s in recent) / len(recent)
        mean_pr = sum(s.presence for s in recent) / len(recent)

        # Check if all recent states are within tolerance of mean
        for state in recent:
            distance = ((state.pattern - mean_p)**2 +
                       (state.intent - mean_i)**2 +
                       (state.presence - mean_pr)**2) ** 0.5

            if distance > tolerance:
                return None

        # Found an attractor
        return TriadicState(mean_p, mean_i, mean_pr)

    def detect_cycle(self, window: int = 20, tolerance: float = 0.15) -> Optional[int]:
        """
        Detect periodic cycles in state evolution.

        Returns cycle length if detected, None otherwise.
        """
        if len(self.states) < window:
            return None

        recent = self.states[-window:]

        # Try different cycle lengths
        for cycle_len in range(2, window // 2):
            is_cycle = True

            for i in range(len(recent) - cycle_len):
                state1 = recent[i]
                state2 = recent[i + cycle_len]

                distance = ((state1.pattern - state2.pattern)**2 +
                           (state1.intent - state2.intent)**2 +
                           (state1.presence - state2.presence)**2) ** 0.5

                if distance > tolerance:
                    is_cycle = False
                    break

            if is_cycle:
                return cycle_len

        return None

    def coherence_trend(self, window: int = 10) -> str:
        """
        Analyze recent coherence trend.

        Returns: "improving", "degrading", "stable", or "chaotic"
        """
        if len(self.states) < 3:
            return "insufficient_data"

        recent = self.states[-window:] if len(self.states) > window else self.states
        history_tuples = [s.as_tuple() for s in recent]

        # Check for decay
        if detect_coherence_decay(history_tuples):
            return "degrading"

        # Calculate strength variance
        strengths = [s.strength() for s in recent]
        mean_strength = sum(strengths) / len(strengths)
        variance = sum((s - mean_strength)**2 for s in strengths) / len(strengths)

        if variance > 0.1:
            return "chaotic"

        # Check if improving
        first_half = strengths[:len(strengths)//2]
        second_half = strengths[len(strengths)//2:]

        if len(first_half) > 0 and len(second_half) > 0:
            first_mean = sum(first_half) / len(first_half)
            second_mean = sum(second_half) / len(second_half)

            if second_mean > first_mean * 1.05:
                return "improving"

        return "stable"

    def get_report(self) -> Dict:
        """Generate comprehensive evolution report."""
        if not self.states:
            return {'status': 'no_data'}

        current = self.states[-1]
        attractor = self.detect_attractor()
        cycle = self.detect_cycle()

        report = {
            'total_states': len(self.states),
            'total_transitions': len(self.transitions),
            'current_state': current.as_tuple(),
            'current_valid': current.is_valid(),
            'current_strength': current.strength(),
            'current_balance': current.balance(),
            'coherence_trend': self.coherence_trend(),
            'critical_events': len(self.critical_events),
            'attractor_detected': attractor is not None,
            'cycle_detected': cycle is not None,
        }

        if attractor:
            report['attractor_state'] = attractor.as_tuple()

        if cycle:
            report['cycle_length'] = cycle

        # Transition type distribution
        transition_types = {}
        for t in self.transitions:
            transition_types[t.transition_type] = \
                transition_types.get(t.transition_type, 0) + 1
        report['transition_distribution'] = transition_types

        return report

    def export_trajectory(self) -> List[Dict]:
        """Export full trajectory as list of dictionaries."""
        return [
            {
                'timestamp': s.timestamp.isoformat(),
                'pattern': s.pattern,
                'intent': s.intent,
                'presence': s.presence,
                'valid': s.is_valid(),
                'strength': s.strength(),
                'balance': s.balance()
            }
            for s in self.states
        ]
