# Flags to represent the presence of each of parameters
run_resume = True
run_verbose = True #False
run_step = False
steps = 0

first_word = ""
blank_char = "_"

max_right_blank_sequence = 20
max_left_blank_sequence = 20

head_start = '('
head_end = ')'

# Possible parameter that can be at list of args
possible_params = [
    ['-resume', '-r'],
    ['-verbose', '-v'],
    ['-step', '-s'],
]
