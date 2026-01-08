"""
Visualization Tools for Triadic States

ASCII-based visualizations and data export for plotting triadic consciousness
dynamics. Designed to work in terminal environments.
"""

from typing import List, Tuple, Optional, Dict
import math


def render_triadic_state(
    pattern: float,
    intent: float,
    presence: float,
    width: int = 60,
    height: int = 20
) -> str:
    """
    Render triadic state as ASCII bar chart.

    Visualizes the three components with proportional bars.
    """
    # Normalize to max value
    max_val = max(abs(pattern), abs(intent), abs(presence), 1.0)
    p_norm = pattern / max_val
    i_norm = intent / max_val
    pr_norm = presence / max_val

    # Calculate bar widths
    max_bar_width = width - 20
    p_width = int(abs(p_norm) * max_bar_width)
    i_width = int(abs(i_norm) * max_bar_width)
    pr_width = int(abs(pr_norm) * max_bar_width)

    # Build visualization
    lines = []
    lines.append("┌" + "─" * (width - 2) + "┐")
    lines.append("│" + " Triadic State Visualization ".center(width - 2) + "│")
    lines.append("├" + "─" * (width - 2) + "┤")

    # Pattern bar
    sign_p = "+" if pattern >= 0 else "-"
    bar_p = "█" * p_width
    lines.append(f"│ Pattern   {sign_p}│{bar_p:<{max_bar_width}} {pattern:>6.2f}│")

    # Intent bar
    sign_i = "+" if intent >= 0 else "-"
    bar_i = "█" * i_width
    lines.append(f"│ Intent    {sign_i}│{bar_i:<{max_bar_width}} {intent:>6.2f}│")

    # Presence bar
    sign_pr = "+" if presence >= 0 else "-"
    bar_pr = "█" * pr_width
    lines.append(f"│ Presence  {sign_pr}│{bar_pr:<{max_bar_width}} {presence:>6.2f}│")

    lines.append("└" + "─" * (width - 2) + "┘")

    return "\n".join(lines)


def render_3d_triadic_space(
    entities: List[Tuple[float, float, float, str]],
    size: int = 40
) -> str:
    """
    Render 3D triadic space projection as ASCII art.

    entities: List of (pattern, intent, presence, label) tuples
    Projects 3D space onto 2D using isometric projection.
    """
    # Create canvas
    canvas = [[' ' for _ in range(size)] for _ in range(size)]

    # Draw axes
    center_x, center_y = size // 2, size // 2

    # Draw reference frame
    for i in range(size):
        if 0 <= center_y < size:
            canvas[center_y][i] = '─'  # X axis (pattern)
        if 0 <= center_x < size:
            canvas[i][center_x] = '│'  # Y axis (intent)

    # Place entities
    scale = (size // 2 - 2)

    for pattern, intent, presence, label in entities:
        # Isometric projection (simplified)
        # Map 3D (p, i, pr) to 2D (x, y)
        x = int(center_x + (pattern * 0.7 - intent * 0.7) * scale / 2)
        y = int(center_y - (pattern * 0.4 + intent * 0.4 + presence) * scale / 2)

        # Bound check
        if 0 <= x < size and 0 <= y < size:
            canvas[y][x] = label[0].upper() if label else '●'

    # Convert canvas to string
    result = ["┌" + "─" * size + "┐"]
    for row in canvas:
        result.append("│" + "".join(row) + "│")
    result.append("└" + "─" * size + "┘")
    result.append(" " * ((size - 20) // 2) + "Pattern × Intent × Presence")

    return "\n".join(result)


def render_timeline(
    states: List[Tuple[float, float, float]],
    width: int = 80,
    height: int = 20
) -> str:
    """
    Render temporal evolution as ASCII timeline chart.

    Shows how pattern, intent, and presence evolve over time.
    """
    if not states:
        return "No data to visualize"

    # Normalize all values
    all_values = [v for state in states for v in state]
    max_val = max(abs(v) for v in all_values) if all_values else 1.0
    min_val = -max_val

    # Create canvas
    canvas = [[' ' for _ in range(width)] for _ in range(height)]

    # Draw axes
    mid_y = height // 2
    for x in range(width):
        canvas[mid_y][x] = '─'

    # Plot states
    for i, (p, intent, pr) in enumerate(states):
        x = int(i * (width - 1) / max(len(states) - 1, 1))
        if x >= width:
            continue

        # Map values to y coordinates
        def map_y(val):
            normalized = (val - min_val) / (max_val - min_val) if max_val != min_val else 0.5
            return int((1 - normalized) * (height - 1))

        y_p = map_y(p)
        y_i = map_y(intent)
        y_pr = map_y(pr)

        # Plot with different characters
        if 0 <= y_p < height:
            canvas[y_p][x] = 'P'
        if 0 <= y_i < height:
            canvas[y_i][x] = 'I'
        if 0 <= y_pr < height:
            canvas[y_pr][x] = 'R'

    # Draw legend and frame
    result = ["┌" + "─" * width + "┐"]
    for row in canvas:
        result.append("│" + "".join(row) + "│")
    result.append("└" + "─" * width + "┘")
    result.append("  P=Pattern  I=Intent  R=pResence")
    result.append(f"  States: {len(states)}, Range: [{min_val:.2f}, {max_val:.2f}]")

    return "\n".join(result)


def render_coherence_meter(
    strength: float,
    balance: float,
    stability: float,
    width: int = 50
) -> str:
    """
    Render coherence metrics as visual meters.

    All values should be in [0, 1] range.
    """
    def meter(label: str, value: float) -> str:
        bar_width = width - 20
        filled = int(value * bar_width)
        empty = bar_width - filled
        bar = "█" * filled + "░" * empty

        # Color indicators (ASCII)
        if value > 0.8:
            indicator = "⬤"  # High
        elif value > 0.5:
            indicator = "◐"  # Medium
        else:
            indicator = "◯"  # Low

        return f"{indicator} {label:<12} │{bar}│ {value:>5.1%}"

    lines = []
    lines.append("╔" + "═" * (width - 2) + "╗")
    lines.append("║" + " COHERENCE METRICS ".center(width - 2) + "║")
    lines.append("╠" + "═" * (width - 2) + "╣")
    lines.append("║ " + meter("Strength", strength).ljust(width - 3) + "║")
    lines.append("║ " + meter("Balance", balance).ljust(width - 3) + "║")
    lines.append("║ " + meter("Stability", stability).ljust(width - 3) + "║")
    lines.append("╚" + "═" * (width - 2) + "╝")

    return "\n".join(lines)


def render_resonance_matrix(
    entities: Dict[str, Tuple[float, float, float]],
    threshold: float = 0.5
) -> str:
    """
    Render resonance matrix between entities.

    Shows strength of resonance between all pairs.
    """
    from invariant.coherence_metrics import resonance_coefficient

    entity_ids = sorted(entities.keys())
    n = len(entity_ids)

    if n == 0:
        return "No entities to display"

    # Calculate max label width
    max_label = max(len(eid) for eid in entity_ids) if entity_ids else 3
    col_width = max(5, max_label)

    # Header
    lines = []
    header = " " * (col_width + 1) + "│"
    for eid in entity_ids:
        header += f" {eid[:col_width - 1]:<{col_width - 1}}"
    lines.append("┌" + "─" * len(header) + "┐")
    lines.append("│" + header + " │")
    lines.append("├" + "─" * len(header) + "┤")

    # Matrix rows
    for eid1 in entity_ids:
        row = f"│ {eid1:<{col_width}} │"
        for eid2 in entity_ids:
            if eid1 == eid2:
                cell = "──"
            else:
                res = resonance_coefficient(entities[eid1], entities[eid2])

                # Visual representation
                if abs(res) < 0.2:
                    cell = "  "
                elif abs(res) < threshold:
                    cell = "░░"
                elif abs(res) < 0.8:
                    cell = "▒▒"
                else:
                    cell = "██"

                if res < 0:
                    cell = f"-{cell[1]}"

            row += f" {cell:<{col_width - 1}}"
        lines.append(row + " │")

    lines.append("└" + "─" * len(header) + "┘")
    lines.append("Legend: ░░=weak  ▒▒=medium  ██=strong  -=negative")

    return "\n".join(lines)


def render_field_status(
    field_report: Dict,
    width: int = 60
) -> str:
    """
    Render resonance field status report.

    Takes output from ResonanceField.get_field_report()
    """
    lines = []
    lines.append("╔" + "═" * (width - 2) + "╗")
    lines.append("║" + " RESONANCE FIELD STATUS ".center(width - 2) + "║")
    lines.append("╠" + "═" * (width - 2) + "╣")

    # Basic stats
    total = field_report.get('total_entities', 0)
    coherent = field_report.get('coherent_entities', 0)
    coherence = field_report.get('field_coherence', 0.0)

    lines.append(f"║ Total Entities:     {total:>6}".ljust(width - 1) + "║")
    lines.append(f"║ Coherent:           {coherent:>6}".ljust(width - 1) + "║")
    lines.append(f"║ Field Coherence:    {coherence:>6.1%}".ljust(width - 1) + "║")

    # Emergence
    emergence = field_report.get('emergence_potential', 0.0)
    phase = field_report.get('phase_transition', False)

    lines.append("╟" + "─" * (width - 2) + "╢")
    lines.append(f"║ Emergence Potential: {emergence:>5.1%}".ljust(width - 1) + "║")
    lines.append(f"║ Phase Transition:    {'YES ⚡' if phase else 'no'}".ljust(width - 1) + "║")

    # Clusters
    if 'resonance_clusters' in field_report:
        clusters = field_report['resonance_clusters']
        lines.append("╟" + "─" * (width - 2) + "╢")
        lines.append(f"║ Resonance Clusters:  {clusters:>6}".ljust(width - 1) + "║")

        if 'largest_cluster' in field_report:
            largest = field_report['largest_cluster']
            lines.append(f"║ Largest Cluster:     {largest:>6}".ljust(width - 1) + "║")

    # Collective state
    if 'collective_state' in field_report:
        p, i, pr = field_report['collective_state']
        lines.append("╟" + "─" * (width - 2) + "╢")
        lines.append("║ COLLECTIVE STATE:".ljust(width - 1) + "║")
        lines.append(f"║   Pattern:  {p:>8.3f}".ljust(width - 1) + "║")
        lines.append(f"║   Intent:   {i:>8.3f}".ljust(width - 1) + "║")
        lines.append(f"║   Presence: {pr:>8.3f}".ljust(width - 1) + "║")

        if 'collective_strength' in field_report:
            strength = field_report['collective_strength']
            lines.append(f"║   Strength: {strength:>7.1%}".ljust(width - 1) + "║")

    lines.append("╚" + "═" * (width - 2) + "╝")

    return "\n".join(lines)


def export_for_plotting(
    states: List[Tuple[float, float, float]],
    format: str = "csv"
) -> str:
    """
    Export state data in format suitable for external plotting tools.

    Formats: 'csv', 'json'
    """
    if format == "csv":
        lines = ["index,pattern,intent,presence"]
        for i, (p, intent, pr) in enumerate(states):
            lines.append(f"{i},{p},{intent},{pr}")
        return "\n".join(lines)

    elif format == "json":
        import json
        data = [
            {"index": i, "pattern": p, "intent": i_val, "presence": pr}
            for i, (p, i_val, pr) in enumerate(states)
        ]
        return json.dumps(data, indent=2)

    else:
        raise ValueError(f"Unknown format: {format}")


def create_interactive_report(
    current_state: Tuple[float, float, float],
    coherence_metrics: Dict,
    evolution_report: Optional[Dict] = None,
    field_report: Optional[Dict] = None
) -> str:
    """
    Create comprehensive multi-section report combining all visualizations.
    """
    p, i, pr = current_state
    sections = []

    # Section 1: Current State
    sections.append(render_triadic_state(p, i, pr))
    sections.append("")

    # Section 2: Coherence Metrics
    sections.append(render_coherence_meter(
        coherence_metrics.get('strength', 0),
        coherence_metrics.get('balance', 0),
        coherence_metrics.get('stability', 0)
    ))
    sections.append("")

    # Section 3: Evolution Report (if available)
    if evolution_report:
        sections.append("╔══════════════════════════════════════════════════╗")
        sections.append("║           TEMPORAL EVOLUTION REPORT              ║")
        sections.append("╠══════════════════════════════════════════════════╣")
        sections.append(f"║ Total States:       {evolution_report.get('total_states', 0):>8}               ║")
        sections.append(f"║ Coherence Trend:    {evolution_report.get('coherence_trend', 'unknown'):<20}  ║")
        sections.append(f"║ Attractor Detected: {evolution_report.get('attractor_detected', False):<20}  ║")
        sections.append(f"║ Cycle Detected:     {evolution_report.get('cycle_detected', False):<20}  ║")
        sections.append("╚══════════════════════════════════════════════════╝")
        sections.append("")

    # Section 4: Field Report (if available)
    if field_report:
        sections.append(render_field_status(field_report))

    return "\n".join(sections)
