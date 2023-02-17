classes = [value for key, value in globals().items() if type(value) == type and issubclass(value, object)]

class Hydrogen_1:
    name = "H2"
    molarVolume = .086
    color = (200, 200, 200)
    tempLimits = [-259, -253]
    state_STP = "gas"

class Helium_2:
    name = "He"
    molarVolume = 31.25
    color = (217, 255, 255)
    tempLimits = [-100000, -268]
    state_STP = "noble"

class Lithium_3:
    name = "Li"
    molarVolume = 13.02
    color = (204, 128, 255)
    tempLimits = [180, 1342]
    state_STP = "solid"

class Berilium_4:
    name = "Be"
    molarVolume = 4.85
    color = (194, 255, 0)
    tempLimits = [1287, 2471]
    state_STP = "solid"

class Boron_5:
    name = "B"
    molarVolume = 4.39
    color = (255, 181, 181)
    tempLimits = [2075, 3727]
    state_STP = "solid"

class Carbon_6:
    name = "C"
    molarVolume = 5.29
    color = (144, 144, 144)
    tempLimits = [3642, 3642]
    state_STP = "solid"

class Nitrogen_7:
    name = "N2"
    molarVolume = 34
    color = (144, 144, 144)
    tempLimits = [-210, -196]
    state_STP = "gas"

class Oxygen_8:
    name = "O2"
    molarVolume = 11
    color = (200, 0, 0)
    tempLimits = [-218, -183]
    state_STP = "gas"