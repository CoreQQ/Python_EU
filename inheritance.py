class Object:
    def __init__(self, name, race):
        self.name = name
        self.level = 1
        self.exp = 0
        self.race = race

    def global_info(self):
        print(f"""
        Name: {self.name}
        Level: {self.level}
        Exp: {self.exp}
        Race: {self.race}
        """)

    def arch():
        return 0


class Human(Object):
    def __init__(self, name, classhero):
        race = "Human"
        super().__init__(name, race)
        self.classhero = classhero
        if classhero == "Warrior":
            self.hp = 100
            self.sp = 120
            self.power = 10
            self.mana = 0
        elif classhero == "Mage":
            self.hp = 70
            self.sp = 50
            self.power = 15
            self.mana = 100

    def stats(self):
        print("""
        You stats:
        HP: {self.hp}
        SP: {self.sp}
        DP: {self.power}
        MP: {self.mana}
        """)
    
    def levelup(self, cout):
        if self.level >= 100:
            print("You have max level")
        self.level += cout
        self.hp = 70 * self.level
        self.sp = 50 * self.level
        self.power = 15 * self.level
        self.mana = 100 * self.level


    def punch(self):
        return self.power

    def magepunch(self):
        if self.mana >= 20:
            self.mana -= 20
            return self.power * 1.5
        else:
            print("Mana low ")
            return self.power * 0.5 

class Demon(Object):
    def __init__(self, name):
        race = "Demon"
        super().__init__(name, race)
        self.hp = 40
        self.blood = 100
        self.power = 20
        self.mana = 300


    def levelup(self, cout):
        if self.level >= 80:
            print("You have max level. Make evolution")
        self.level += cout
        self.hp = 40 * self.level
        self.blood = 100 * self.level
        self.power = 20 * self.level
        self.mana = 300 * self.level

    def stats(self):
            print(f"""
        You stats:
        HP: {self.hp}
        BP: {self.blood}
        DP: {self.power}
        MP: {self.mana}
        """)


    def punch(self):
        return self.power

class Archdemon(Demon):
    def __init__(self, name):
        race = "ArchDemon"
        super().__init__(name)
        self.hp = 40
        self.blood = 100
        self.power = 20
        self.mana = 300
        self.level = 79
        self.ulitmate = 3

    def archlevelup(self, cout):
        if self.level >= 120:
            print("You have max level")
        self.level += cout
        self.hp = 85 * self.level
        self.blood = 300 * self.level
        self.power = 30 * self.level
        self.mana = 550 * self.level
    

    def recover_blood():
        if self.mana >= 40:
            self.mana -= 40
            self.blood += 50

    def buy_exp():
        if self.blood >= 100:
            self.exp += 1000
            self.blood -=100

    def buy_ulitmate():
        if self.blood >=1000:
            self.ulitmate +=1
            self.blood -= 1000

    def ulitmate():
        if self.ulitmate >= 1:
            self.ulitmate -=1
            return self.power * 3


def creatname():
    banlist = "!@#$%^&*()_+}{'/.,<>?|=-`~"
    name = str(input("Enter you name: "))
    for i in name:
        if i in banlist:
            print("You make error")
            return creatname()
    return name

def choiseclass():
    print("""
    1 - Warrior
    2 - Mage
    """)
    choise = int(input("choise you race: "))
    if choise == 1:
        return "Warrior"
    elif choise == 2:
        return "Mage"
    else:
        print("You make error!")
        return choiseclass()



if __name__ == "__main__":
    
    name = creatname()
    classhero = choiseclass()
    #player = Human(name, classhero)
    player = Archdemon(name)
    
    player.levelup(1)
    while True:
        print("What next? help to see command")
        choise = input()
        if choise == "help":
            print("""
            info - info to player
            stat - player stats
            end - Exit


            ONLY Race Archdemon:
            recoverblood - recover you blood, price 40 mana
            buyexp - buy exp point, price 100 blood
            buyulitmate - Add ulitmate skill, price 1000 blood
            """)
        elif choise == "info":
            player.global_info()
        elif choise == "stat":
            player.stats()
        elif choise == "recoverblood":
            player.recover_blood()
        elif choise == "buyexp":
            player.buy_exp()
        elif choise == "buyulitmate":
            player.buy_ulitmate()
        if choise == "end":
            break


   
