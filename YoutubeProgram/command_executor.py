import asyncio
import inspect
from termcolor import colored
from command_mappings import functions # functions is the entire dictionary that is in command_mappings

def execute_user_command():
    # Call the appropriate function based on user choice
    # Get the user's choice
    help_messages()
    exit_command_received = False
    while not exit_command_received: 

        command = input(colored("Enter a command ('exit' or 'quit' to stop): ", 'green'))
        # faster way to check the membership of many words is to use command.lower() in set 
        # 
        if command.lower() in ['exit', 'quit']: #short hand is called membership testin and its idiomatic for python
            exit_command_received = True

        elif command in functions: # if a command matches the name of a key-function pair in the command_mappings dictionary  
            call_command(command)

        else:
            invalid_command_entered(command)




def invalid_command_entered(command):
    print(colored(f"Invalid command was entered: {colored(f'{command}', 'light_cyan')}", 'red'))
    print('\n')
    help_messages()


def help_messages():
    print(colored("===HERE ARE THE COMMANDS IN CASE YOU FORGOT===", 'light_magenta'))
    call_command('HELP')


def get_input(num_params, command):
        return [input(f"{functions[command]['description']}\nEnter {functions[command]['needed parameters'][parameter_index]}: ") for parameter_index in range(num_params)]


def call_command(command):
    selected_function, user_parameter = find_command(command)
    run_command(selected_function, *user_parameter)


def find_command(command):
    selected_function = functions[command]['function'] # dict[key][subkey] --> command_mappings[command_named_key][run_function_of_command]
    num_params = len(inspect.signature(selected_function).parameters) # get number of parameters dynamically
    #print(num_params)

    user_parameter = get_input(num_params, command)
    #print(user_parameter)
    #print(*user_parameter)
    # https://careerkarma.com/blog/python-return-multiple-values/
    return selected_function, user_parameter


def  run_command(selected_function, *user_parameter):
    # Check if the function is a coroutine function
    if inspect.iscoroutinefunction(selected_function):
        # If it is, use asyncio.run() to call it
        try:
            result = asyncio.run(selected_function(*user_parameter))
        except AttributeError as e:
            print(f"{colored(f'An error occurred: ', 'red')}{colored(f'{e}', 'light_cyan')}")
        except Exception as e:
            print(f"{colored(f'An unknown error occurred: ', 'red')}{colored(f'{e}', 'cyan')}")
    else:
        # If it's not, call it normally
        try:
            result = selected_function(*user_parameter)
        except AttributeError as e:
            print(f"{colored(f'An error occurred: ', 'red')}{colored(f'{e}', 'light_cyan')}")
        except Exception as e:
            print(f"{colored(f'An unknown error occurred: ', 'red')}{colored(f'{e}', 'cyan')}")
    #print(f"Command Executed: Returns - {result}\n")