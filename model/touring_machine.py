# This class will hold all Touring Machine's data
import parameters


class TuringMachine:
    def __init__(self, blocks=None):
        if blocks is None:
            blocks = list()
        self.blocks = blocks
        self.index = 0

    def accept(self, original_tape):
        main_block = list(filter(
            lambda block: block.id == 'main',
            self.blocks
        ))[0]
        self._accept(
            [char for char in original_tape],
            main_block
        )

    def _accept(
            self, tape, current_block
    ):
        current_state = current_block.initial_state

        while current_state != 'pare' and current_state != 'retorne':

            # verbose
            self._check_verbose(current_block, current_state, tape)

            symbol_read = tape[self.index]
            commands_from_state = list(
                filter(
                    lambda watched_command: watched_command.current_state == current_state,
                    current_block.commands
                )
            )

            if len(commands_from_state) == 1 and commands_from_state[0].is_another_block_call:
                self._accept(
                    tape,
                    list(filter(
                        lambda block: block.id == commands_from_state[0].block_id,
                        self.blocks
                    ))[0]
                )
                current_state = commands_from_state[0].return_state

            else:

                star_commands = list(
                    filter(
                        lambda watched_command:
                        watched_command.current_symbol == '*',
                        commands_from_state
                    )
                )

                non_star_commands = list(
                    filter(
                        lambda watched_command:
                        watched_command.current_symbol == symbol_read,
                        commands_from_state
                    )
                )
                command = None
                try:
                    command = star_commands[0] if len(non_star_commands) == 0 else non_star_commands[0]
                except:
                    print(f'An error appeared at index {self.index} while whatching symbol {symbol_read} at'
                          f' state {current_state} on block {current_block.id}')

                tape[self.index] = command.new_symbol if command.new_symbol != '*' else tape[self.index]
                current_state = command.new_state if command.new_state != '*' else current_state

                if command.movement != 'i':
                    if self.index == 0 and command.movement == 'e':
                        aux = [parameters.blank_char]
                        aux.extend(tape)
                        tape = aux
                        self.index += 1
                    if self.index == (len(tape) - 1) and command.movement == 'd':
                        tape.append(parameters.blank_char)
                    self.index += 1 if command.movement == 'd' else -1

        self._check_verbose(current_block, current_state, tape)

    def _check_verbose(self, current_block, current_state, tape):
        if current_state != 'retorne':
            self._print_verbose(current_block, current_state, tape)

    def _print_verbose(self, current_block, current_state, original_tape):
        bloco = '.' * (16 - len(current_block.id)) + current_block.id
        estado = '0' * (4 - len(current_state)) + current_state

        print(f'{bloco}.{estado}: {self._generate_right_and_left_queues(original_tape)}')

    def _generate_right_and_left_queues(self, original_tape):
        tape_with_max_blank_chars = f'{parameters.blank_char * (parameters.max_left_blank_sequence - 1)}' \
                     + ''.join(original_tape) + \
                     f'{parameters.blank_char * (parameters.max_right_blank_sequence - 1)}'
        left_index = self.index
        center_index = self.index + parameters.max_right_blank_sequence
        right_index = self.index + ((2 * parameters.max_right_blank_sequence) - 1)

        result_str = ''
        current_index = left_index
        while current_index < right_index:
            if current_index + 1 == center_index:
                result_str = f'{result_str}({tape_with_max_blank_chars[current_index]})'
            else:
                result_str = f'{result_str}{tape_with_max_blank_chars[current_index]}'
            current_index += 1

        return result_str

