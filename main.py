from window import *
import recipe
import list_builder
import molecules
import atoms
import maths
import particle
import itertools

print_events = False
print_debug = True
print_zbug = False

def p(string):
    if print_debug:
        print(str(string))

def e(string):
    if print_events:
        print(str(string))

def z(string):
    if print_zbug:
        print(str(string))



def calculate_leftover_reactants_and_products_made(first_reactant_coefficient, second_reactant_coefficient, first_reactant_name, second_reactant_name, product_coefficients, mols_of_dot, mols_of_other_dot):
    ratio_of_coefficients = first_reactant_coefficient / second_reactant_coefficient
    if mols_of_other_dot == 0:
        mols_of_other_dot = .00000000000000001
    ratio_of_mols = mols_of_dot / mols_of_other_dot
    yeild = []
    mols_of_excess_dot = 0.0
    mols_of_excess_other_dot = 0.0

    if ratio_of_mols < ratio_of_coefficients:
        mols_of_limiting_reactant = mols_of_dot
        limiting_reactant_coefficient = first_reactant_coefficient
        mols_of_excess_other_dot = abs(mols_of_other_dot - (mols_of_dot / limiting_reactant_coefficient))

    elif ratio_of_mols > ratio_of_coefficients:
        mols_of_limiting_reactant = mols_of_other_dot
        limiting_reactant_coefficient = second_reactant_coefficient
        mols_of_excess_dot = abs(mols_of_dot - (mols_of_other_dot / limiting_reactant_coefficient))
    else:
        mols_of_limiting_reactant = mols_of_dot
        limiting_reactant_coefficient = first_reactant_coefficient

    for product in product_coefficients:
        yeild.append((mols_of_limiting_reactant * (product[0] / limiting_reactant_coefficient), product[1]))

    if mols_of_excess_dot != 0.0 and mols_of_excess_other_dot == 0.0:
        return [[(mols_of_excess_dot, first_reactant_name)], yeild]
    elif mols_of_excess_other_dot != 0.0 and mols_of_excess_dot == 0.0:
        return [[(mols_of_excess_other_dot, second_reactant_name)], yeild]
    elif mols_of_excess_dot == 0.0 and mols_of_excess_other_dot == 0.0:
        return [yeild]
    else:
        return [[(mols_of_excess_dot, first_reactant_name), (mols_of_excess_other_dot, second_reactant_name)], yeild]

def get_combinations(lst):
    combinations = list(itertools.combinations(lst, 2))
    return combinations



def main():


    # Create classes for molecules and atoms
    molecule_classes_list = [cls for name, cls in molecules.__dict__.items() if isinstance(cls, type) and name != "__builtins__"]
    atom_classes_list = [cls for name, cls in atoms.__dict__.items() if isinstance(cls, type) and name != "__builtins__"]
    partical_classes_list = atom_classes_list + molecule_classes_list

    molecule_classes_dict = list_builder.build_particles_name_dictionary(molecules)
    atom_classes_dict = list_builder.build_particles_name_dictionary(atoms)
    partical_classes_dict = {**atom_classes_dict, **molecule_classes_dict}

    # Initialize Pygame and set the display window
    pygame.init()
    frame = 0
    screen_width = 1900
    screen_hight = 1000
    window = pygame.display.set_mode((screen_width, screen_hight))
    pygame.display.set_caption("Pygame Template")

    # Variables for the dot objects
    dots = []
    current_dot_index = 0
    id = 0
    selected_atom = atom_classes_list[current_dot_index]

    # Variables for temperature range
    min_temperature = -273
    max_temperature = 4000
    room_temperature = 20
    temperature = room_temperature

    # Variables for the slider object
    slider_rect = pygame.Rect(50, 50, 500, 50)
    thumb_size = (20, 50)
    thumb_color = (100, 100, 100)
    slider_position = (temperature - min_temperature) / (max_temperature - min_temperature) * slider_rect.width
    thumb_x = slider_rect.left + slider_position - thumb_size[0] / 2
    thumb_y = slider_rect.top
    thumb_pos = pygame.Rect(thumb_x, thumb_y, thumb_size[0], thumb_size[1])
    dragging_slider = False
    offset = 0

    font = pygame.font.Font(None, 30)


    # Variables for the mouse position
    left_mouse_down = False

    # Convert and adjust chemical equation recipes
    recipes = {r:recipe.adjust_equation(recipe.convert_equation(r)) for r in list(recipe.recipes_unformatted.keys())}

    # Running loop for Pygame
    running = True


    while running:
        if len(dots) > 200:
            p("dots list is longer than 200")
            dots.remove(dots[0])

        mouse_pos = pygame.mouse.get_pos()
        frame += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                e("preparing to quit")
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                e("a mouse button has been pressed")
                if event.button == 1:
                    e("it was the left mouse button")
                    left_mouse_down = True
                    if slider_rect.collidepoint(mouse_pos):
                        dragging_slider = True
                        offset = event.pos[0] - thumb_pos.x
                elif event.button == 3:
                    e("it was the right mouse button")
                    current_dot_index = (current_dot_index + 1) % len(atom_classes_list)
                    selected_atom = atom_classes_list[current_dot_index]
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_pos = event.pos
                e("the left mouse button is no longer being pressed")
                left_mouse_down = False
                dragging_slider = False
            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
                if dragging_slider:
                    e("mouse is down and IS over a UI element")
                    thumb_pos.x = mouse_pos[0] - offset
                    if thumb_pos.x < slider_rect.left:
                        thumb_pos.x = slider_rect.left
                    elif thumb_pos.x > slider_rect.right - thumb_size[0]:
                        thumb_pos.x = slider_rect.right - thumb_size[0]
                    temperature = min_temperature + (thumb_pos.x - slider_rect.left) / (
                                slider_rect.width - thumb_size[0]) * (max_temperature - min_temperature)

        if left_mouse_down and not dragging_slider:
            e("mouse is down and NOT over a UI element so adding new dot")
            new_dot = particle.Particle(mouse_pos[0], mouse_pos[1], id, 1, selected_atom, temperature)
            dots.append(new_dot)
            id += 1


            # Calculate the temperature based on mouse position

        if temperature < 0:
            window.fill((0, 0, abs(temperature/3)))
        else:
            window.fill((temperature/32, temperature/200, 0))

        pygame.draw.rect(window, (255, 255, 255), slider_rect, 1)
        pygame.draw.rect(window, thumb_color, thumb_pos)

        celcius = str(round(temperature)) + " °C  |  "
        kelvin = str(round(maths.celsius_to_kelvin_fahrenheit(temperature)[0])) + " °K  |  "
        fahrenheit = str(round(maths.celsius_to_kelvin_fahrenheit(temperature)[1])) + " °F "

        temperature_text = font.render( kelvin + celcius + fahrenheit , True, (255, 255, 255))
        text_rect = temperature_text.get_rect()
        text_rect.center = slider_rect.center
        window.blit(temperature_text, text_rect)




        element_text = font.render(selected_atom.__name__, True, (255, 255, 100))
        window.blit(element_text, (10, 10))

        for i, dot in enumerate(dots):  # for every dot on the screen

            dot.update(screen_width, screen_hight, temperature)
            dot.draw(window)

            if dot in dots:
                if dot.y > screen_hight or dot.x > screen_width:
                    dots.remove(dot)

            if temperature < dot.chemical.tempLimits[0]:
                dot.state = "solid"
            elif temperature > dot.chemical.tempLimits[1]:
                dot.state = "gas"
            else:
                dot.state = "liquid"

            if hasattr(dot.chemical, "decomposition_temperature"):
                if temperature > dot.chemical.decomposition_temperature:
                    p(str(dot.name) + " can decompose at temperature " + str(temperature))
                    dots.remove(dot)
                    for product in dot.chemical.decomposition_products.keys():
                        p(str(product) + " is result of decomposition")
                        new_dot = particle.Particle(dot.x, dot.y, id, dot.mols * dot.chemical.decomposition_products[product], partical_classes_dict[product], temperature)
                        dots.append(new_dot)




        reacting = False
        formula = None
        dot = None
        other_dot = None
        distance = None
        pairs_list = get_combinations(dots)
        required_temperature = None
        dot_pair_string = None

        for dot_pair in pairs_list:  # for every dot pair on the screen



            p("testing new dot pair")

            dot = dot_pair[0]
            other_dot = dot_pair[1]
            dot_pair_string = str(((dot.mols, dot.name), (other_dot.mols, other_dot.name)))
            distance = maths.find_distance_between_two_points(dot.x, dot.y, other_dot.x, other_dot.y)

            if distance <= (dot.radius + other_dot.radius):  # if Dots are colliding
                p(dot_pair_string + " are collinding")
                if dot.state != "solid" or other_dot.state != "solid":
                    p("at least one isnt a solid")
                    if dot.name == other_dot.name:  # if dots are the SAME type (START REACTION)
                        p(dot_pair_string + " are the same chemical")
                        formula = None
                        reacting = True
                        break
                    else:
                        p(dot_pair_string + " are NOT the same chemical")
                        for formulas in recipes.keys():
                            if {dot.name, other_dot.name} == set(item[1] for item in recipes[formulas][0]):
                                p(dot_pair_string + " matches " + formulas)
                                formula = formulas
                                required_temperature = recipe.recipes_unformatted[formulas]["temp"]
                        if required_temperature != None:
                            p("required temp for reaction is: " + str(required_temperature))
                            if temperature >= required_temperature:  # if the temperature is right (START REACTION)
                                p(str(temperature) + " partical temp is greater than required temp for reaction of " + str(required_temperature) )

                                products = [item[1] for item in recipes[formula][1]]
                                list_of_decomposition_temperatures = [partical_classes_dict[name].decomposition_temperature for name in products if hasattr(partical_classes_dict[name], 'decomposition_temperature')]

                                if temperature < max(list_of_decomposition_temperatures):
                                    p(str(temperature) + "is less than the hottest decomp temp")

                                    reacting = True
                                    break




        if reacting:

            p("reacting: " + dot_pair_string)
            dots.remove(dot)
            dots.remove(other_dot)
            collision_point = maths.find_colliding_point_between_two_circles(dot.x, dot.y, dot.radius, other_dot.x,other_dot.y, other_dot.radius)

            if formula:
                p(dot_pair_string + " can react with " + formula)
                reactants = [reactant for reactant in recipes[formula][0]]
                products = [product for product in recipes[formula][1]]
                first_reactant, second_reactant = reactants[0], reactants[1]
                if dot.name == second_reactant[1]:
                    p("reordering reactents")
                    first_reactant, second_reactant = second_reactant, first_reactant
                first_reactant_coefficient, first_reactant_name = first_reactant
                second_reactant_coefficient, second_reactant_name = second_reactant

                reaction_results = calculate_leftover_reactants_and_products_made(first_reactant_coefficient,second_reactant_coefficient,first_reactant_name,second_reactant_name, products,dot.mols, other_dot.mols)
                reaction_results = recipe.flatten_list(reaction_results)

                dot_is_leftover = False
                other_dot_is_leftover = False
                for result in reaction_results:
                    p("for the result: " + str(result))
                    result_amount, result_name = result
                    chemical = partical_classes_dict[result_name]
                    if result_name == dot.name:
                        dot_is_leftover = True
                        other_dot_is_leftover = False
                    elif result_name == other_dot.name:
                        dot_is_leftover = False
                        other_dot_is_leftover = True

                    if result_name == dot.name:  # if leftover particle a
                        p(dot.name + "is leftover")
                        p("20 " + "creating a leftover particle " + result_name + " at previous " + dot.name)
                        new_dot = particle.Particle(dot.x, dot.y, id, result_amount, chemical, temperature)
                        new_dot.speed_x = dot.speed_x
                        new_dot.speed_y = dot.speed_y

                    elif result_name == other_dot.name:  # if leftover particle b
                        p(other_dot.name + "is leftover")
                        p("21 " + "creating a leftover particle " + result_name + " at previous " + other_dot.name)
                        new_dot = particle.Particle(other_dot.x, other_dot.y, id, result_amount, chemical, temperature)
                        new_dot.speed_x = other_dot.speed_x
                        new_dot.speed_y = other_dot.speed_y

                    else:  # if new particle
                        p("22 " + result_name + " is not one of the composite chemicals")
                        if dot_is_leftover:  # and other_dot was used up entirely
                            p("IF dot_is_leftover")
                            if distance < dot.radius:  # if other_dot was inside dot, new dot is placed at other dot
                                p("24 " + str(distance) + " (the distance) is less than the radius of" + dot.name)
                                p("25 " + "creating a NEW particle " + result_name + " at previous " + other_dot.name)
                                new_dot = particle.Particle(other_dot.x, other_dot.y, id, result_amount, chemical,temperature)
                            else:  # if other_dot is outside of dot
                                p("26 " + "composites are outside eachother")
                                if dot.state == "solid":  # if leftover dot is a solid
                                    p("27 " + dot.name + " is a solid")
                                    p("28 " + "creating a NEW particle " + result_name + " at previous " + other_dot.name)
                                    new_dot = particle.Particle(other_dot.x, other_dot.y, id, result_amount, chemical,temperature)  # new dot is spawned at border of excess dot
                                else:
                                    p("29 " + dot.name + " is NOT solid")
                                    p("30 " + "creating a NEW particle " + result_name + " at previous " + other_dot.name)
                                    new_dot = particle.Particle(other_dot.x, other_dot.y, id, result_amount, chemical,temperature)  # new dot is spawned at used up element

                        elif other_dot_is_leftover:
                            p("IF other_dot_is_leftover")
                            if distance < other_dot.radius:
                                p("32 " + str(distance) + " (the distance) is less than the radius of " + other_dot.name)
                                p("33 " + "creating a NEW particle " + result_name + " at previous " + dot.name)
                                new_dot = particle.Particle(dot.x, dot.y, id, result_amount, chemical, temperature)
                            else:
                                p("34 " + "composites are outside eachother")
                                if other_dot.state == "solid":
                                    p("35 " + other_dot.name + " is a solid")
                                    p("36 " + "creating a NEW particle " + result_name + " at the collision point")
                                    new_dot = particle.Particle(collision_point[0], collision_point[1], id,result_amount, chemical, temperature)
                                else:
                                    p("37 " + other_dot.name + " is NOT solid")
                                    p("38 " + "creating a NEW particle " + result_name + " at previous " + dot.name)
                                    new_dot = particle.Particle(dot.x, dot.y, id, result_amount, chemical, temperature)

                        else:  # both dots used up
                            p("39 " + "BOTH reactants were consumed")
                            if other_dot.state == "solid":
                                p("40 " + other_dot.name + " is a solid")
                                p("41 " + "creating a NEW particle " + result_name + " at previous " + other_dot.name)
                                new_dot = particle.Particle(other_dot.x, other_dot.y, id, result_amount, chemical,temperature)
                            elif dot.state == "solid":
                                p("42 " + dot.name + " is a solid")
                                p("43 " + "creating a NEW particle " + result_name + " at previous " + dot.name)
                                new_dot = particle.Particle(dot.x, dot.y, id, result_amount, chemical, temperature)
                            else:
                                p("44 " + "NIETHER dot is solid")
                                p("45 " + "creating a NEW particle " + result_name + " at the collision point")
                                new_dot = particle.Particle(collision_point[0], collision_point[1], id, result_amount,chemical, temperature)
                    p("47 " + "adding " + str(new_dot.name) + "to dots list")
                    dots.append(new_dot)
                # END OF REACTANTS LOOP
            else:  # dots are the same and just need to merge
                p("colliding dots are the same and need to merge")

                if dot.mols > other_dot.mols:
                    new_dot = particle.Particle(dot.x, dot.y, id, dot.mols + other_dot.mols, dot.chemical, temperature)
                    new_dot.speed_x = dot.speed_x
                    new_dot.speed_y = dot.speed_y
                    dots.append(new_dot)
                else:
                    new_dot = particle.Particle(other_dot.x, other_dot.y, id, dot.mols + other_dot.mols,
                                                other_dot.chemical, temperature)
                    new_dot.speed_x = other_dot.speed_x
                    new_dot.speed_y = other_dot.speed_y
                    dots.append(new_dot)


        pygame.display.update()
    pygame.quit()


# If the script is being run as the main module, call the main() function
if __name__ == "__main__":
    main()
