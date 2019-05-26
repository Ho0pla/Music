import math
import sys



notes = {
    "C": 0,
    "C#": 1,
    "Db": 1,
    "D": 2,
    "D#": 3,
    "Eb": 3,
    "E": 4,
    "E#": 5,
    "Fb": 4,
    "F": 5,
    "F#": 6,
    "Gb": 6,
    "G": 7,
    "G#": 8,
    "Ab": 8,
    "A": 9,
    "A#": 10,
    "Bb": 10,
    "B": 11,
    "B#": 0,
    "Cb": 11,
}

naturalValues = {
    "C": 0,
    "D": 1,
    "E": 2,
    "F": 3,
    "G": 4,
    "A": 5,
    "B": 6,
}

valueToNatural = {
    0: "C",
    1: "D",
    2: "E",
    3: "F",
    4: "G",
    5: "A",
    6: "B",
}

valueToName = {
    0: "C",
    1: "C#",
    2: "D",
    3: "D#",
    4: "E",
    5: "F",
    6: "F#",
    7: "G",
    8: "G#",
    9: "A",
    10: "A#",
    11: "B",
}

accidentalValue = {
    "##": 2,
    "#": 1,
    "": 0,
    "b": -1,
    "bb": -2,
}

valueToAccidental = {
    2: "##",
    1: "#",
    0: "",
    -1: "b",
    -2: "bb",
}

scaleTypes = {
    "Major":[2,2,1,2,2,2,1],
    "Natural Minor":[2,1,2,2,1,2,2],
    "Harmonic Minor":[2,1,2,2,1,3,1],
    "Melodic Minor":[2,1,2,2,2,2,1]
}

class Note:
    def __init__(self, noteName): # input notes like C, Bb, G##, etc
        self.name = noteName
        self.letter = self.name[0]
        self.natVal = naturalValues[self.letter]
        self.accidental = self.name[1:]
        """ if len(noteName) == 3:
            self.accidental = self.name[-2:]
        elif len(noteName) == 2:
            self.accidental = self.name[-1:]
        else:
            self.accidental = " " """

        self.accValue = accidentalValue[self.accidental]

        self.pitch = (notes[self.letter] + self.accValue)%12

    def change_accidental(self, accidental):
        self.accidental = accidental
        self.accValue = accidentalValue[self.accidental]
        self.pitch = (notes[self.letter] + self.accValue)%12
        self.name = self.letter + self.accidental

class Scale:
    def __init__(self, key, type):
        self.notes = self.Key_Generator(key, type)

    def Key_Generator(self, key, type):
        n = Note(key)
        scale_steps = scaleTypes[type]
        scale = [Note(key)]
        scaleRef = [n.pitch]
        natStep = n.natVal
        scalePitch = [n.pitch]
        step = n.pitch
        for i in scale_steps:
            step += i
            scalePitch.append((step)%12) #generates pitch values for each scale step
        print (key, type, "Scale")
        #print scalePitch

        for i in range(0, 7):
            natStep += 1
            scale.append(Note(valueToNatural[(natStep)%7]))
            scaleRef.append(notes[valueToNatural[(natStep)%7]])
        for i in range(1,7):
            diff = scalePitch[i] - scaleRef[i]
            if diff > 2:
                diff = diff - 12
                scale[i].change_accidental(valueToAccidental[diff])
            elif diff < -2:
                diff = diff + 12
                scale[i].change_accidental(valueToAccidental[diff])
            else:
                scale[i].change_accidental(valueToAccidental[diff])

        for i in range(0,7):
            print (scale[i].name,)
        print
        return scale

    def getScaleDegree(self, degree):
        return self.notes[(degree - 1) % 7]



my_scale = Scale("A", "Major")
print(my_scale)
print(my_scale.getScaleDegree(4).pitch)
