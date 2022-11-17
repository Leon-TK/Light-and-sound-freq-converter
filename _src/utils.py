from ctypes import sizeof
from enum import Enum
from typing import List

from . import constants as Constants

def doubleUntilInRange(value, rangeStart, rangeEnd):
    value = value * 2
    if rangeStart < value and value < rangeEnd:
        return value
    elif value > rangeEnd:
        return None
    else:
        return doubleUntilInRange(value, rangeStart, rangeEnd)

def doOnAWhileConditionWithB(a, b, conditionAB, operationOnA):
    if conditionAB(a,b):
        return doOnAWhileConditionWithB(operationOnA(a), b, conditionAB, operationOnA)
    else:
        return a

def doubleUntilNotLess(value, peakValue):
    return doOnAWhileConditionWithB(value, peakValue, lambda a, b: a < b, lambda a : a * 2)