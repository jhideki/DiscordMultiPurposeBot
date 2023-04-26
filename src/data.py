from enum import Enum
import random
import os

class ValorantCharacter(Enum):
    BREACH = 'Breach'
    BRIMSTONE = 'Brimstone'
    CYBER_CAGE = 'Cypher'
    JETT = 'Jett'
    KAY_O = 'KAY/O'
    KILLJOY = 'Killjoy'
    OMEN = 'Omen'
    PHOENIX = 'Phoenix'
    RAZE = 'Raze'
    REYNA = 'Reyna'
    SAGE = 'Sage'
    SKYE = 'Skye'
    SOVA = 'Sova'
    VIPER = 'Viper'
    YORU = 'Yoru'

def pick_random_character() -> ValorantCharacter:
    return random.choice(list(ValorantCharacter))

class MessageStore:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                pass
        self.messages = self.read_file()

    def read_file(self):
        with open(self.filename, 'r') as file:
            messages = [line.strip() for line in file]
        return messages

    def add_message(self, message):
        content = message.content[6:].replace(" ", "")
        with open(self.filename, 'a') as file:
            file.write(content + "\n")
        self.messages.append(content)

