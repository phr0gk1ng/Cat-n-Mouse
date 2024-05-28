class Character:
    def __init__(self, can_move):
        self.can_move = can_move
    
    

class Mouse:
    def __init__(self, inventory, can_move):
        super().__init__(can_move)
        self.inventory = inventory

class Cat: 
    def __init__(self, can_attack, can_move):
        super().__init__(can_move)
        self.can_attack = can_attack
