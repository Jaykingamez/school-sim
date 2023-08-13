from enum import Enum

class Action(Enum):
    """
    Study:          Pay attention to class / Conduct Revision
    Scroll:         Scroll for the dopamine
    Befriend:       Talk with a random person, improve relationship
    Quarrel:        Quarrel with a random person, decrease relationship
    """
    STUDY = "study"
    SCROLL = "look_at_phone"
    BEFRIEND = "befriend"
    QUARREL = "quarrel"
