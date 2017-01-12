# RPG Character Sheet Generator
import random

class sheet:
    def __init__(self, name, hp, mp, strength, magic, dexterity):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.strength = strength
        self.magic = magic
        self.dexterity = dexterity
    # based on what class you choose, the stats change.
    def warrior(self):
        self.hp = self.hp + 10
        self.strength = self.strength + 5
        self.magic = self.magic - 10
        self.dexterity = self.dexterity + 3
    def mage(self):
        self.hp = self.hp - 5
        self.mp = self.mp + 15
        self.strength = self.strength - 10
        self.magic = self.magic + 15


def main():
    name = raw_input('Greetings traveller, what is your name? > ' )
    i = 0
    stats = []
    while i < 5:
        # chooses a random number between 10 and 20 by steps of 1.
        randStat = random.randrange(10,20,1)
        # adds these numbers to the stats list
        stats.append(randStat)
        i += 1
    #assigns random numbers to stats for character
    #character = sheet(name,stats[0],stats[1],stats[2],stats[3],stats[4])
    # arguments in sheet (name, hp, mp, strength, magic, dexterity)
    dude = sheet(name, stats[0],stats[1],stats[2],stats[3],stats[4])

    dudeClass = raw_input("Do you want to be a warrior or mage? > ")
    # Makes the text lower case just in case.
    dudeClass = dudeClass.lower()
    # stats are changed on the character based on what class they choose
    if dudeClass == "warrior":
        dude.warrior()
    elif dudeClass == "mage":
        dude.mage()
    else:
        # if they misspell the class or whatever it sends them to the start of the function
        print "That's not a class."
        return main()
    # prints out stats, %s is for strings, %d is for ints
    print '''
    name: %s
    hp: %d
    mp: %d
    strength: %d
    magic: %d
    dexterity: %d
    ''' % (dude.name, dude.hp, dude.mp, dude.strength, dude.magic, dude.dexterity)
main()
