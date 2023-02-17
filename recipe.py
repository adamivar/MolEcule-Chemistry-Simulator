recipes_unformatted = {
    "2H2 + O2 = 2H2O": {"temp": 570},
    "Li + H2 = LiH": {"temp": 200},
    "4Li + O2 = 2Li2O": {"temp": 100},
    "Li + H2O = LiOH": {"temp": 0},
    "Li2O + CO2 = Li2CO3": {"temp": 0},
    "2Be + O2 = 2BeO": {"temp": 700},
    "BeO + H2O = Be(OH)2": {"temp": 0},
    "4B + 3O2 = 2B2O3": {"temp": 700},
    "12C + 11O2 = 10CO2 + 2CO": {"temp": 500},
    "1O2 + 2CO = 2CO2": {"temp": 500},
    "Li + 4C = Li2C2": {"temp": 1000},
    "10Li + 2CO2 = Li2C2 + 4Li2O": {"temp": 1000},
    "Li2C2 + 2H2O = 2LiOH + C2H2": {"temp": 0},
    "2LiH + 4C = Li2C2 + C2H2": {"temp": 400},
    "2LiH + C2H2 = Li2C2 + 2H2": {"temp": 0},
    "LiH + LiOH = Li2O + H2": {"temp": 300},
    "LiH + H2O = LiOH + H2": {"temp": 0},
    "6Li + N2 = 2Li3N": {"temp": 50},
    "Li3N + 3H2O = 3LiOH + NH3": {"temp": 0},
    "2Li + 2NH3 = 2LiNH2 + H2": {"temp": 400},
    "3Be + N2 = Be3N2": {"temp": 1100},
    "Be3N2 + 6H2O = 3Be(OH)2 + 2NH3": {"temp": 1100},
    






}








# recipes should be this format = [  [{[1,C],[2,O2]},{[1,CO2],[,]}]  ,,]

def convert_string_chemical(string_chemical):
    coefficient = 1
    chemical = string_chemical.strip()
    if chemical[0].isdigit():
        for i in range(len(chemical)):
            if not chemical[i].isdigit():
                coefficient = int(chemical[:i])
                chemical = chemical[i:]
                break
    chemical_data = [coefficient, chemical]
    return chemical_data


def convert_equation(equation):
    # Split the equation into its individual components
    string_products = []
    products = []
    string_reactants = []
    reactants = []


    formulas = equation.split("=")
    string_reactants_formula = [formulas[0].strip()]
    string_products_formula = [formulas[1].strip()]

    for string in string_products_formula:
        string_products = string.split(" + ")
    for string in string_reactants_formula:
        string_reactants = string.split("+")

    for string in string_products:
        products.append(convert_string_chemical(string))
    for string in string_reactants:
        reactants.append(convert_string_chemical(string))

    products = set([tuple(l) for l in products])
    reactants = set( [ tuple(l) for l in reactants] )

    return [reactants, products]

def flatten_list(lst):
    flat_list = []
    for sub_list in lst:
        for item in sub_list:
            flat_list.append(item)
    return flat_list


def adjust_equation(equation):
    result = []
    coefficients = []
    for reaction in equation:
        reactants = list(reaction)
        coefficients.append([float(r[0]) for r in reactants])

    coefficients = flatten_list(coefficients)

    for reaction in equation:
        reactants = list(reaction)
        new_reaction = []
        for r in reactants:
            new_reaction.append((str(round(float(r[0])/max(coefficients), 10)), r[1]))
        result.append(set(new_reaction))
    return equation


# Example usage
