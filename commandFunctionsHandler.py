def print_function_descriptions(functions_dict):
    for key, value in functions_dict.items():
        print(f"{key} - {value['description']}")