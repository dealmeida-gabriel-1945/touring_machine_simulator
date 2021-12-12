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
    if parameters.run_step:
        if parameters.possible_params[2][0] in args:
            parameters.steps = int(args[args.index(parameters.possible_params[2][0]) + 1])
        else:
            parameters.steps = int(args[args.index(parameters.possible_params[2][1]) + 1])
    else:
        parameters.steps = parameters.default_steps * 1


def show_parameters():
    """
    This function show all parameters presence at arguments of the command line
    :return: void
    """
    print(f'steps -> {parameters.steps}')
    print(f'resume -> {parameters.run_resume}')
    print(f'has steps -> {parameters.run_step}')
    print(f'verbose -> {parameters.run_verbose}')
