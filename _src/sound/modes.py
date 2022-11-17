from enum import Enum
from typing import List

from .notes import NoteStep

__all__ = ["Modes"]

class Modes(Enum):
    Ionian = 1
    Dorian = 2
    Phrygian = 3
    Lydian = 4
    Mixolydian = 5
    Aeolian = 6
    Locrian = 7
    HarmonicMinor = 8
    MelodicMinor = 9

def getModeFormula(scale: NoteStep) -> List[NoteStep]:
    Tone = NoteStep.Tone
    HalfTone = NoteStep.HalfTone
    ToneHalfTone = NoteStep.ToneHalfTone

    if scale == Modes.Ionian:
        return [Tone, Tone, HalfTone, Tone, Tone, Tone, HalfTone]
    if scale == Modes.Dorian:
        return [Tone, HalfTone, Tone, Tone, Tone, HalfTone, Tone]
    if scale == Modes.Phrygian:
        return [HalfTone, Tone, Tone, Tone, HalfTone, Tone, Tone]
    if scale == Modes.Lydian:
        return [Tone, Tone, Tone, HalfTone, Tone, Tone, HalfTone]
    if scale == Modes.Mixolydian:
        return [Tone, Tone, HalfTone, Tone, Tone, HalfTone, Tone]
    if scale == Modes.Aeolian:
        return [Tone, HalfTone, Tone, Tone, HalfTone, Tone, Tone]
    if scale == Modes.Locrian:
        return [HalfTone, Tone, Tone, HalfTone, Tone, Tone, Tone]

    if scale == Modes.HarmonicMinor:
        return [Tone, HalfTone, Tone, Tone, HalfTone, ToneHalfTone, HalfTone]
    if scale == Modes.MelodicMinor:
        return [Tone, HalfTone, Tone, Tone, Tone, Tone, Tone]