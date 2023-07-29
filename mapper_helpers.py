# For this file since we are touching the command function mappings specficically, we just have to pass
# the dictionary in as a parameter call it as a lamda function



def print_function_descriptions(function_dictionary):
    for key, value in function_dictionary.items():
        print(f"{key} - {value['description']}")
