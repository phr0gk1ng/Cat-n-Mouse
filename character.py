class Character():
    def __init__(self, char_name, char_description, conversation):
        self.name = char_name
        self.description = char_description
        self.conversation = conversation

    def describe(self):
        print("\nCharacter: " + self.name + " is here!")
        print(self.description)

    def get_conversation(self):
        return self.conversation

    def talk(self):
        if self.conversation is not None:
            print("\n[" + self.name + " says]: "+ self.get_conversation())
        else:
            print(self.name + "doesn't want to talk to you")

    def fight(self, combat_item):
        print(self.name + "doesn't want to fight with you")
        return True
    
    def get_char_name(self):
        return self.char_name
    
class Enemy(Character):
    def __init__(self, char_name, char_description, conversation, char_weakness):
        super().__init__(char_name, char_description, conversation)
        self.char_weakness = char_weakness
    
    def get_char_weakness(self):
        return self.char_weakness

    def fight(self, combat_item):
        if combat_item == self.get_char_weakness():
            print("You fend " + self.name + " off with the " + combat_item )
            return True
        else:
            return False