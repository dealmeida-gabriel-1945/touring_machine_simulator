# Flags to represent the presence of each of parameters
run_resume = True
run_verbose = True #False
run_step = False
run_custom_head = False
steps = 0

first_word = ""
blank_char = "_"

max_right_blank_sequence = 20
max_left_blank_sequence = 20

default_steps = 500
last_new_instructions = ''

head_start = '('
head_end = ')'

breakpoint_char = '!'

# Possible parameter that can be at list of args
possible_params = [
    ['-resume', '-r'],
    ['-verbose', '-v'],
    ['-step', '-s'],
    ['-head', '-h'],
]
