from enum import Enum

class Personality(Enum):
    """
    The personalities that affects the decision making of NPC

    Studious      : More likely to pay attention in class
    Lazy          : Less Likely to pay attention in class
    Argumentative : More likely to quarrel
    Friendly      : Less Likely to friend
    """
    STUDIOUS = "studious"
    LAZY = "lazy"
    ARGUMENTATIVE = "argumentative"
    FRIENDLY = "friendly"

