from enum import Enum

class Relationship(Enum):
    """
    Character relationships (Inspired from Sims 4)

    Enemy:             Someone whom you would love to beat up
    Dislike:           Something feels off about someone, oh yeah, you don't like them
    Stranger:          Rather use my phone then talk to them
    Acquaintance:      Feeling to use phone is less
    Friend:            Nice person to be around
    Romantic interest: More than friends
    Partner:           Boyfriend/Girlfriend
    """
    ENEMY = "enemy"
    DISLIKE  = "dislike"
    STRANGER = "stranger"
    ACQUAINTANCE = "acquaintance"
    FRIEND = "friend"
    ROMANTIC_INTEREST = "romantic_interest"
    PARTNER = "partner"
