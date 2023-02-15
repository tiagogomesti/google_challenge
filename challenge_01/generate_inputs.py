import random

def generate_inputs(id_min_value, id_max_value, n_max_elements_by_input, n_inputs_to_generate):
    input_tests = [([],0)] * 0
    for i in range(0, n_inputs_to_generate):
        data = []
        n_items = random.randint(0, n_max_elements_by_input)
        for j in range(0, n_items):
            data.append(random.randint(id_min_value, id_max_value))

        for k in range(0,4):
            input_tests.append((data, k))
    return input_tests