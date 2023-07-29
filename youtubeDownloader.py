import inspect

import youtubeDownloaderFunctions as YTD


# This is the dictionary that maps commands to functions, descriptions, and parameters
functions = {
    'MP': {
        'function': YTD.download_multiple_playlists, 
        'description': "This function downloads multiple playlists",
        'default parameters': ['None'],
        'needed parameters': ['While Loop -will need to type multiple playlist urls']
    },
    'SP': {
        'function': YTD.download_playlist_webm_to_mp3, 
        'description': "This function downloads a single playlist",
        'default parameters': ['None'],
        'needed parameters': ['single playlist url']
    },
    'S': {
        'function': YTD.single_videoURL_webm_to_mp3_stream_Download, 
        'description': "This function downloads a single video",
        'default parameters': ['None'],
        'needed parameters': ['single video url', "two commands", "three commands"]
    }
}

def get_input(n):
        return [input(f"{functions[command]['description']}\nEnter {functions[command]['needed parameters'][i]}: ") for i in range(num_params)]


# Call the appropriate function based on user choice
# Get the user's choice
exit_command_received = False
while not exit_command_received: 
    command = input("Enter a command (or 'exit' to quit): ")
    if command.lower() == 'exit':
        exit_command_received = True

    elif command in functions:
        func = functions[command]['function']
        num_params = len(inspect.signature(func).parameters) # get number of parameters dynamically
        print(num_params)

        user_parameter = get_input(num_params)
        print(user_parameter)
        print(*user_parameter)

        result = functions[command]['function'](*user_parameter)
        print(result)

    else:
        print("Invalid command")




# #Check for command in dictionary using if statements vs the try:catch
# if command in command_dict:
#     result = command_dict[command](x, y)
#     print("The result is {}".format(result))
# else:
#     print("Invalid command")

# try:
#     function_info = functions[userchoice]
#     print(f"\nYou have selected: {function_info['description']}")

#     # Get the default parameters from the user
#     default_parameters = function_info['default parameters']

#     # if function has defaults but needs user input --> override function defaults with user parameters where needed
#     # if function has no defaults but needs user input --> ask user for input
#     # if funtion has defaults and user inputs parameters --> override function defaults with user parameters
#     # if function doesn't have default and user inputs parameters --> use user parameters in the function 
#     # if funtion has defaults and user inputs no parameters --> use default parameters in function
#     # if function doesn't have default and user inputs no parameters --> run function if function doesn't require parameters else say error
   
#     #============================
#     # If a function does not require user input: The function will run as is, without needing any parameters.
#     # If a function has default parameters and the user provides input: The user's input will replace the default parameters. This means that the function will use the values provided by the user instead of the default ones.
#     # If a function has default parameters and the user does not provide input: The function will use the default parameters. This means that if the user doesn't specify any values, the function will use the pre-set default values.
#     # If a function does not have default parameters and the user provides input: The function will use the user's input. This means that the function will use the values provided by the user.
#     # If a function does not have default parameters and the user does not provide input:
#     # If the function does not require any parameters, it will run without any issues (as per rule 1).
#     # If the function does require parameters, an error will occur because the required values are missing.
#     # In summary, if a function doesn't require user input, it will run without any parameters. For functions that do require input, user input always takes precedence over default parameters. If no user input is provided, the function will attempt to use default parameters if they exist. If no default parameters exist and the function requires parameters, an error will occur.
#     #============================
#     if None not in default_parameters: # If default parameters list does not have None
#         print(f"\nParamters neeed: {function_info['needed parameters']}")
#         # If parameter needed is 0 say Nothing and start doing the thing
#         # If parameter needed is 1 say Enter a parameter
#         # If parameter needed is 2 or mroe Enter parameter seperated by

#         # Or we could have it dynamically asks for the parameters since we have them stored as values in the function dictionary:
#         # EX: for num of parameter in command-paramerter list -> ("Enter the dict[i]. Leave empty to use default parameters: defaultOption[i]") 
#         # --> This could also give us the ability to have user options for default vs user




#     # while not exit_command_received: 
#     #     command = input("Enter a command (or 'exit' to quit): ")
#     #     if command.lower() == 'exit':
#     #         exit_command_received = True
#     #     elif command in command_dict:
#     #         if command in ["add_subtract", "add_multiply"]:
#     #             numbers = get_input(3)
#     #         else:
#     #             numbers = get_input(2)
#     #         result = command_dict[command](*numbers)
#     #         print("The result is {}".format(result))
#     #     else:
#     #         print("Invalid command")


#         userinput = input("Enter the parameters (separated by comma). Leave empty to use default parameters: ")
#         if userinput: # if the user input is not empty, use the user's default parameters
#             userparameters = userinput.split(',')
    
#     function_info['function'](*userparameters)


# except KeyError:
#     print("Invalid choice. Please enter MP, SP, or S.")



