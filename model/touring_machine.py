# This class will hold all Touring Machine's data
class TouringMachine:
    def __init__(self, blocks=None):
        if blocks is None:
            blocks = list()
        self.blocks = blocks
