class Character():
    def __init__(self, char_name, char_description, conversation):
        self.name = char_name
        self.description = char_description
        self.conversation = conversation

# Describe this character
    def describe(self):
        print(self.name + " is here!")
        print(self.description)
# Set what this character will say when talked to
    def get_conversation(self):
        return self.conversation
# Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: "+ self.get_conversation())
        else:
            print(self.name + "doesn't want to talk to you")
# Fight with this character
    def fight(self, combat_item):
        print(self.name + "doesn't want to fight with you")
        return True
    
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
            print(self.name + " swallows you, little wimp")
            return False
