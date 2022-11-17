from enum import Enum

__all__ = ["Notes"]

class NoteStep(Enum):
    HalfTone = 1
    Tone = 2
    ToneHalfTone = Tone + HalfTone
    TwoTone = Tone + Tone

class Notes(Enum):
    A = 1
    A_S = 2
    B = 3
    C = 4
    C_S = 5
    D = 6
    D_S = 7
    E = 8
    F = 9
    F_S = 10
    G = 11
    G_S = 12