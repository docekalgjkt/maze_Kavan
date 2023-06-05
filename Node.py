from typing import Any


class Node:
    def __init__(self, val):
        self.value = val
        self.way_top = None
        self.way_down = None
        self.way_left = None
        self.way_right = None   

