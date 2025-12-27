def triadic_check(pattern, intent, presence):
    """
    Triadic Coherence Invariant (TCI)

    A system is coherence-capable iff:
    Pattern ≠ 0
    Intent ≠ 0
    Presence ≠ 0
    """
    if pattern in (None, 0):
        return False
    if intent in (None, 0):
        return False
    if presence in (None, 0):
        return False
    return True
