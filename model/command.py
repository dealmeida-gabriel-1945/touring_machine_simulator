# This class will hold the data of every single command
class Command:
    def __init__(
        self,
        current_state='', current_symbol='', new_symbol='', movement='', new_state='',
        block_id='', return_state='', is_breakpoint=False
    ):
        self.current_state = current_state
        self.current_symbol = current_symbol
        self.new_symbol = new_symbol
        self.movement = movement
        self.new_state = new_state
        self.block_id = block_id
        self.return_state = return_state
        self.is_breakpoint = is_breakpoint
        # To check if the command line is a call to another block, we will use this flag
        self.is_another_block_call = block_id != '' and return_state != ''

    def __str__(self):
        if self.is_another_block_call:
            return f'-> {self.current_state} {self.block_id} {self.return_state}'
        return f'-> {self.current_state} {self.current_symbol} -- {self.new_symbol} {self.movement} {self.new_state}'
