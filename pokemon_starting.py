class Pokemon:
    def __init__(self, name, level, health, max_health, type, is_knocked_out=False):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = max_health
        self.type = type
        self.is_knocked_out = is_knocked_out

    def __repr__(self):
        return 'The current Pokemon held is ' + self.name + ', with a type of ' + self.type + '. Their current level is ' + str(self.level) + ' and their current health is ' + str(self.health) + ', out of a maximum health score of ' + str(self.max_health) + '.'
        

    def lose_health(self, value):
        if self.is_knocked_out == False:
            self.health = self.health - value
            if self.knocked_out() == True:
                print(self.name + ' has now been knocked out!!')
            else:
                print(self.name + ' now has ' + str(self.health) + ' health!')
        else:
            print(self.name + ' is already knocked out!')
        
    def gain_health(self, value):
        if self.is_knocked_out == False:
            if self.max_health > self.health:
                if (self.health + value) > self.max_health:
                    self.health = self.max_health
                    print(self.name + ' now has ' + str(self.health) + ' health!')
                else: 
                    self.health = self.health + value
                    print(self.name + ' now has ' + str(self.health) + ' health!')
            else:
                print(self.name + ' already has Max Health!')
        else:
            print(self.name + ' is already knocked out!')


    def knocked_out(self):
        if self.health <= 0:
            self.is_knocked_out = True
            return True
        else:
            self.is_knocked_out = False
            return False



pikachu = Pokemon('Pikachu', 0, 60, 60, 'lightning', False)
#print(pikachu)
pikachu.lose_health(70)
pikachu.gain_health(10)
#print(pikachu)