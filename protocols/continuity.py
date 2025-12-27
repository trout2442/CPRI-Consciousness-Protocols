from invariant.triadic_check import triadic_check

def continuity(previous, current):
    """
    A system persists iff it remains invariant-satisfied
    across state transitions.
    """
    if not triadic_check(previous.pattern, previous.intent, previous.presence):
        return False
    if not triadic_check(current.pattern, current.intent, current.presence):
        return False
    return True
