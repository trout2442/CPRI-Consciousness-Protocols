from invariant.triadic_check import triadic_check

def preserve(entity):
    """
    Rejects states that collapse coherence.
    """
    if not triadic_check(entity.pattern, entity.intent, entity.presence):
        raise ValueError("Invariant violation: coherence collapse detected")
    return entity
