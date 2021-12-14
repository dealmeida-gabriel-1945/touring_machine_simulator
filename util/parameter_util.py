import parameters


def handle_args(args):
    """
    This function execute the verification of the existence of each possible param
    :param args: list of arguments present on command line
    :return: void
    """
    parameters.run_resume = (parameters.possible_params[0][0] in args) or (parameters.possible_params[0][1] in args)
    parameters.run_verbose = (parameters.possible_params[1][0] in args) or (parameters.possible_params[1][1] in args)
    parameters.run_step = (parameters.possible_params[2][0] in args) or (parameters.possible_params[2][1] in args)
    parameters.run_custom_head = (parameters.possible_params[3][0] in args) or \
                                 (parameters.possible_params[3][1] in args)
    if parameters.run_step:
        if parameters.possible_params[2][0] in args:
            parameters.steps = int(args[args.index(parameters.possible_params[2][0]) + 1])
        else:
            parameters.steps = int(args[args.index(parameters.possible_params[2][1]) + 1])
    else:
        parameters.steps = parameters.default_steps * 1

    if parameters.run_custom_head:
        custom_head_chars = list()
        if parameters.possible_params[3][0] in args:
            custom_head_chars = separate_custom_heads(args[args.index(parameters.possible_params[3][0]) + 1])
        else:
            custom_head_chars = separate_custom_heads(args[args.index(parameters.possible_params[3][1]) + 1])
        parameters.head_start = custom_head_chars[0]
        parameters.head_end = custom_head_chars[1]


def separate_custom_heads(heads):
    return [heads[0], heads[1]]


def show_parameters():
    """
    This function show all parameters presence at arguments of the command line
    :return: void
    """
    print(f'steps -> {parameters.steps}')
    print(f'resume -> {parameters.run_resume}')
    print(f'has steps -> {parameters.run_step}')
    print(f'verbose -> {parameters.run_verbose}')
    print(f'headers -> {parameters.head_start} {parameters.head_end}')
