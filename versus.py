import random

class anime_hercule:
    def __init__(self,name,health,goal,):
        self.name= name
        self.health = health
        self.goal = goal

    def is_alive(self):
        return self.health > 0  

    def attack(self,opponent):
        damage = random.randit(1, self.strength)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name}and deals{damage} damage.")


class anime_goku:
    def __init__(self,name,health,)


    



        





    



pass