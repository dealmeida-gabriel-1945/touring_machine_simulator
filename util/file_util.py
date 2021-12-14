import parameters
from model.block import Block
from model.command import Command
from model.turing_machine import TuringMachine


def retrieve_mt_from_file(file_name):
    """
    This function open the given file and take it's content to build the touring machine (MT). The process occurs line by
    line and each line is cleaned to be esier to get the correct information.
    :param file_name the file's absolut path
    :return: the touring machine in a TouringMachine class object
    """
    # The MT object is initialized
    builded_mt = TuringMachine(parameters.steps)
    # The file is open and it's content is taken
    with open(file_name) as f:
        lines = f.readlines()
        # Each line is analyzed to see if it contains useful information
        for line in lines:
            # The line is cleaned
            args = clear_splitted_line(line.split(' '))
            # If the line is empty or is a comment or is a line break or is a command block's closure the line is
            # useless
            if (len(args) == 0) or args[0].startswith(';') or args[0].startswith('\n') or args[0].startswith('fim'):
                continue
            # If the line starts with 'bloco' that means that the line is a creation of a command block
            if args[0] == 'bloco':
                builded_mt.blocks.append(Block(id=args[1], initial_state=args[2]))
            # If not, the line is a creation of a command line
            else:
                # If the command line has 3 parts, that means that the command is a call fot another block
                if len(args) == 3 or len(args) == 4:
                    builded_mt.blocks[
                        len(builded_mt.blocks) - 1
                    ].commands.append(
                        Command(
                            current_state=args[0],
                            block_id=args[1],
                            return_state=args[2],
                            is_breakpoint=is_command_breakpoint(args)
                        )
                    )
                # If not, the command is a normal one
                else:
                    builded_mt.blocks[
                        len(builded_mt.blocks) - 1
                    ].commands.append(
                        Command(
                            current_state=args[0],
                            current_symbol=args[1],
                            new_symbol=args[2],
                            movement=args[3],
                            new_state=args[4],
                            is_breakpoint=is_command_breakpoint(args)
                        )
                    )
        # Close the file
        f.close()
    # Returns the Touring Machine object
    return builded_mt


def is_command_breakpoint(args):
    return ((len(args) == 6) and (args[5] == parameters.breakpoint_char)) or \
           ((len(args) == 4) and (args[3] == parameters.breakpoint_char))


def clear_splitted_line(line):
    """
    This function clears the line passed through parameter
    :param line line splitted by ' ' (space) to be cleaned
    :return: the clear line
    """
    cleared_line_parts = list()

    for part in line:
        # If the part of the line ends with a break line, removes this char ('\n')
        if part.endswith('\n'):
            part = part[:len(part) - 1]
        # If the part of the line is empty or is '--', ignores it
        if part == '' or part == '−−':
            continue
        # Then, only important parts will reach this part
        cleared_line_parts.append(part)
    # Returns a list with the important parts of the line
    return cleared_line_parts
