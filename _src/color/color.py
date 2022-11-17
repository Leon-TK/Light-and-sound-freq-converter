from enum import Enum
from typing import List

from ..sound.sound import Sound
from .. import constants as Constants

__all__ = ["Color", "ColorScheme", "ColorToSoundAdapter", "applyColorScheme"]

class Color:
    def __init__(self, r, g, b) -> None:
        self.r = r
        self.g = g
        self.b = b

class ColorScheme(Enum):
    Monochromatic = 1
    Analogous = 2
    Complementary = 3
    SplitComplementary = 4
    Triadic = 5
    Tetradic = 6
    Square = 7

class ColorToSoundAdapter(Sound.Sound):
    def __init__(self, color) -> None:
        note = _convertColorToNote(color)
        super().__init__(note)
def _convertColorToNote(color):
    hue = Color.rgbToHue_Limited(color.r, color.g, color.b)
    alpha = hue / 360
    return Sound.frequencyToNote(Constants.RED_LIGHT_FREQ + alpha * (Constants.LIGHT_BEGIN - Constants.LIGHT_END))

#TODO: implement this applyColorScheme
def applyColorScheme(color, scheme) -> List[Color]:
    colors = [color]
    return colors

def _lightFreqToColor(frequency):
    alpha = (frequency - Constants.LIGHT_BEGIN) / (Constants.LIGHT_END - Constants.LIGHT_BEGIN)
    hueAngle = alpha * Constants.HUE_ANGLE
    return _hueToRgb_SV(hueAngle)

def _hueToRgb_SV(angle):
    if angle < 61:
        r = 255
        g = 255 * angle / 60
        b = 0
        return r, g, b
    if angle < 121:
        angle = angle - 60
        r = 255 * (1 - angle / 60)
        g = 255
        b = 0
        return r, g, b
    if angle < 181:
        angle = angle - 120
        r = 0
        g = 255
        b = 255 * angle / 60
        return r, g, b
    if angle < 241:
        angle = angle - 180
        r = 0
        g = 255 * (1 - angle / 60)
        b = 255
        return r, g, b
    if angle < 301:
        angle = angle - 240
        r = 255 * angle / 60
        g = 0
        b = 255
        return r, g, b
    if angle < 361:
        angle = angle - 300
        r = 255 * angle / 60
        g = 0
        b = 255 * (1 - angle / 60)
        return r, g, b
    return None

#
#I have no time for searching another aproach.
def _rgbToHue_Limited(r, g, b):
    assert(not (r > 0 and g > 0 and b > 0))

    #<60
    if r > g and b == 0:
        return 60 * g / r
    #<120
    if g > r and b == 0:
        return 60 + (60 * (1 - r / g))
    #<180
    if g > b and r == 0:
        return 120 + 60 * b / g
    #<240
    if b > g and r == 0:
        return 180 + (60 * (1 - g / b))
    #<300
    if b > r and g == 0:
        return 240 + 60 * r / b
    #<360
    if r > b and g == 0:
        return 300 + 60 * b / r
    return None

def _colorToLightFreq(color):
    return 0