from interface import *

#TODO: get rid of using of constans in some functions. Instead create function's arguments and the pass constants
if __name__ == "__main__":

    #TODO: pending test
    color = Color(255, 0, 0)
    pallete = applyColorScheme(color, ColorScheme.Triadic)
    print(pallete)

    note = Notes.E
    gamma = getOctaveFromScale(note, Scales.Aeolian)

    """ for note in gamma:
        print(SoundToColorAdapter(note)) """

    rNote = ColorToSoundAdapter(Color(255, 0, 0))
    gNote = ColorToSoundAdapter(Color(0, 255, 0))
    bNote = ColorToSoundAdapter(Color(0, 0, 255)) #TODO: same as red note, the G note! fix this. I think yhis is due to intersection of comparation values
    enumerate
    print("")


