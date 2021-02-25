"""
a collection of all the messages and strings for different errors
and conditions to use globally in the library

feel free to edit them according to your preference
"""


# a message for when the player exits the game
exit_message = "exiting..."

# the user_input that the player enters to quit the game
exit_user_input = "quit"

# a message presenting the player with the command to exit the game
exit_user_input_request = f"to exit the game enter: {exit_user_input}"

# a message for when the player reaches the end of the plot line
end_message = "you reached the end - game over"

# a message that tells the player he entered a invalid user_input
invalid_user_input_message = "this is an invalid choice. please try again"

# a message that tells the player he entered an invalid trait name
invalid_trait_name = "couldn't find the specified trait name to use: \
{trait_name}"

# the value at a next_scene field isn't a NextScene instance
invalid_next_scene_value = "next scene field in scene must be\
NextScene object or the next scene name"

# a message requesting the player for user_input, goes before the input
input_prompt = "your choice: "

# a string used in input.ask_for_user_inputs to present the user_inputs
user_inputs_request_format = "to {option_title} enter one of the \
following {option_user_inputs}\n"

# trait names
power_trait_name = "Skill"
health_trait_name = "Stamina"
luck_trait_name = "Luck"
