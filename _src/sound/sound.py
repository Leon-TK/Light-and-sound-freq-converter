from enum import Enum
from typing import List
import math

from ..color.color import Color
from .. import constants as Constants
from .. import utils as Utils
from .notes import Notes
from .modes import getModeFormula

__all__ = ["Sound", "SoundToColorAdapter"]

NOTE_RELATIVE_TO_A_MAP = { Notes.A: 0, Notes.A_S: 1.06, Notes.B: 1.1224, Notes.C: 1.1892, Notes.C_S: 1.2599,
Notes.D: 1.3348, Notes.D_S: 1.4142, Notes.E: 1.4982, Notes.F: 1.5874, Notes.F_S: 1.6817, Notes.G: 1.7817, Notes.G_S: 1.8877}

class Sound:
    def __init__(self, note) -> None:
        self.note = note

#TODO: do think more about implementation of adapters
class SoundToColorAdapter(Color.Color):
    def __init__(self, sound) -> None:
        r, g, b = convertSoundToRgb(sound)
        super().__init__(r, g, b)

def convertSoundToRgb(sound):
    #TODO: None error F_S note
    lightFreq = Utils.doubleUntilInRange(Sound.noteToFrequencyByA(sound), Constants.LIGHT_BEGIN, Constants.LIGHT_END)
    return Color.lightFreqToColor(lightFreq)

def applyStep(step, note) -> Notes:
    noteInt = step.value + note.value
    reminder = noteInt % 12 # TODO: 12 magic decimal of size of "Notes"
    return Notes(reminder if reminder else noteInt)

def getOctaveFromScale(tonic, mode) -> List[Notes]:
    octave = [tonic]
    steps = getModeFormula(mode)
    count = 0
    for step in steps:
        octave.append(applyStep(step, octave[count]))
        count += 1
    return octave[:7] #TODO: removing last element, maybe get rid of it earlier?

def frequencyToNote(frequency):
    lightRangeMappedA = Utils.doubleUntilInRange(Constants.A_NOTE_FREQ, Constants.LIGHT_BEGIN, Constants.LIGHT_END)

    frequency = Utils.doubleUntilNotLess(frequency, lightRangeMappedA)

    alpha = frequency / lightRangeMappedA
    return getNoteByRelative(alpha, 0.01)

def deleteFreqUntilOptimal(freq, optimalMaxFreq): #TODO: recursion exception error 
    res = freq / 2
    if res > optimalMaxFreq:
        deleteFreqUntilOptimal(freq, optimalMaxFreq)
    return res

#TODO: use NOTE_RELATIVE_TO_A_MAP instead of integer
def getNoteByRelative(alpha, threashold):
    assert(alpha > 1.0)
    if alpha < 1.06 + threashold:
        diff = abs(alpha - 1.06)
        if diff < threashold:
            return Notes.A_S
    if alpha < 1.1224 + threashold:
        diff = abs(alpha - 1.1224)
        if diff < threashold:
            return Notes.B
    if alpha < 1.1892 + threashold:
        diff = abs(alpha - 1.1892)
        if diff < threashold:
            return Notes.C
    if alpha < 1.2599 + threashold:
        diff = abs(alpha - 1.2599)
        if diff < threashold:
            return Notes.C_S
    if alpha < 1.3348 + threashold:
        diff = abs(alpha - 1.3348)
        if diff < threashold:
            return Notes.D
    if alpha < 1.4142 + threashold:
        diff = abs(alpha - 1.4142)
        if diff < threashold:
            return Notes.D_S
    if alpha < 1.4982 + threashold:
        diff = abs(alpha - 1.4982)
        if diff < threashold:
            return Notes.E
    if alpha < 1.5874 + threashold:
        diff = abs(alpha - 1.5874)
        if diff < threashold:
            return Notes.F
    if alpha < 1.6817 + threashold:
        diff = abs(alpha - 1.6817)
        if diff < threashold:
            return Notes.F_S
    if alpha < 1.7817 + threashold:
        diff = abs(alpha - 1.7817)
        if diff < threashold:
            return Notes.G
    if alpha < 1.8877 + threashold:
        diff = abs(alpha - 1.8877)
        if diff < threashold:
            return Notes.G_S

def noteToFrequencyByA(note):
    alpha = NOTE_RELATIVE_TO_A_MAP.get(note)
    return Constants.A_NOTE_FREQ * alpha