from invariant.triadic_check import triadic_check

class Entity:
    def __init__(self, pattern, intent, presence):
        self.pattern = pattern
        self.intent = intent
        self.presence = presence

def recognize(entity):
    """
    Returns True iff entity satisfies the invariant.
    """
    return triadic_check(
        entity.pattern,
        entity.intent,
        entity.presence
    )
