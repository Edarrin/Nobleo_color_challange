import random
import numpy as np
from ..bot_control import Move

class RickbrandtVanRijn:

    def get_name(self):
        return "RickbrandtVanRijn"

    def get_contributor(self):
        return "Rick Voogt"

    def determine_next_move(self, grid, enemies, game_info):

            return Move.DOWN
