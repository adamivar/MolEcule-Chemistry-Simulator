class CarbonMonoxide:
    name = "CO"
    molarVolume = 44.6
    color = (235, 245, 255)
    tempLimits = [-205, -191]
    state_STP = "gas"
    decomposition_temperature = 100000
    decomposition_products = {"C": 1, "O2": 0.5}

class CarbonDioxide:
    name = "CO2"
    molarVolume = 22.4
    color = (200, 200, 200)
    tempLimits = [-78, -78]
    state_STP = "gas"
    decomposition_temperature = 100000
    decomposition_products = {"C": 1, "O2": 1}

class BoronTrioxide:
    name = "B2O3"
    molarVolume = 8.31
    color = (255, 255, 255)
    tempLimits = [450, 1860]
    state_STP = "solid"
    decomposition_temperature = 1750
    decomposition_products = {"B":1,"O2":1.5}

class BeriliumOxide:
    name = "BeO"
    molarVolume = 8.31
    color = (255, 255, 255)
    tempLimits = [2507, 3900]
    state_STP = "solid"
    decomposition_temperature = 2250
    decomposition_products = {"Be": 1, "O2": 0.5}

class BeriliumHydroxide:
    name = "Be(OH)2"
    molarVolume = 22.41
    color = (255, 255, 255)
    tempLimits = [900, 900]
    state_STP = "solid"
    decomposition_temperature = 400
    decomposition_products = {"BeO": 1, "H2O": 1}

class LithiumHydride:
    name = "LiH"
    molarVolume = 7.5
    color = (60, 140, 120)
    tempLimits = [692, 950]
    state_STP = "solid"
    decomposition_temperature = 100000
    decomposition_products = {"Li": 1, "H": 1}

class LithiumOxide:
    name = "Li2O"
    molarVolume = 11.9
    color = (255, 255, 255)
    tempLimits = [1438, 2600]
    state_STP = "solid"
    decomposition_temperature = 100000
    decomposition_products = {"Li": 2, "O2": 0.5}

class LithiumHydroxide:
    name = "LiOH"
    molarVolume = 11.1
    color = (255, 255, 155)
    tempLimits = [462, 924]
    state_STP = "solid"
    decomposition_temperature = 900
    decomposition_products = {"Li2O": 0.5, "H2O": 0.5}

class LithiumCarbide:
    name = "Li2C2"
    molarVolume = 35.02
    color = (255, 255, 155)
    tempLimits = [452, 100000]
    state_STP = "solid"
    decomposition_temperature = 100000
    decomposition_products = {"Li": 2, "C": 2}

class Acetylene:
    name = "C2H2"
    molarVolume = 120
    color = (255, 100, 100)
    tempLimits = [-80, -84]
    state_STP = "gas"
    decomposition_temperature = 400
    decomposition_products = {"C": 2, "H2": 1}

class LithiumCarbonate:
    name = "Li2CO3"
    molarVolume = 37.5
    color = (255, 255, 255)
    tempLimits = [723, 1310]
    state_STP = "solid"
    decomposition_temperature = 100000
    decomposition_products = {"Li": 2, "C": 1, "O2": 1.5}

class LithiumNitride:
    name = "Li3N"
    molarVolume = 27.5
    color = (200, 80, 60)
    tempLimits = [813, 100000]
    state_STP = "solid"
    decomposition_temperature = 100000
    decomposition_products = {"Li": 3, "N2": 1.5}


class Ammonia:
    name = "NH3"
    molarVolume = 24.85
    color = (250, 255, 250)
    tempLimits = [-77, -33]
    state_STP = "gas"
    decomposition_temperature = 400
    decomposition_products = {"N2": 0.5, "H2": 1.5}

class BerylliumNitride:
    name = "Be3N2"
    molarVolume = 20.25
    color = (240, 240, 230)
    tempLimits = [2200, 2240]
    state_STP = "solid"
    decomposition_temperature = 10000
    decomposition_products = {"Be": 3, "N2": 1}

class NitricOxide:
    name = "Be3N2"
    molarVolume = 20.25
    color = (240, 240, 230)
    tempLimits = [2200, 2240]
    state_STP = "solid"
    decomposition_temperature = 10000
    decomposition_products = {"Be": 3, "N2": 1}

    

class Water:
    name = "H2O"
    molarVolume = 18.02
    color = (0, 100, 200)
    tempLimits = [0, 100]
    state_STP = "liquid"
    decomposition_temperature = 2000
    decomposition_products = {"H2": 1, "O2": 0.5}