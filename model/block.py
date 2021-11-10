# This class will hold the data of every single command block
class Block:
    def __init__(self, id='', initial_state='', commands=None):
        if commands is None:
            commands = list()
        self.id = id
        self.initial_state = initial_state
        self.commands = commands

    def __str__(self):
        return f'{self.id} ({len(self.commands)} commands)'
