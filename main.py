class Warrior:
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} лёг спать")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} сел кушать")
        self.power += 1

    def hit(self):
        print(f"{self.name} бьет кого-то")
        self.endurance -= 6

    def walk(self):
        print(f"{self.name} гуляет")

    def show_info(self):
        print(f"имя воина - {self.name}")
        print(f"цвет волос воина - {self.hair_color}")
        print(f"сила воина - {self.power}")
        print(f"выносливость воина - {self.endurance}")

    def __str__(self):
        return f"Warrior(name={self.name}, power={self.power}, endurance={self.endurance}, hair_color={self.hair_color})"

war1 = Warrior(name="Степа", power=77, endurance=54, hair_color="коричневый")
war2 = Warrior(name="Егор", power=45, endurance=23, hair_color="блонд")

war1.sleep()
war1.eat()
war1.hit()
war1.walk()
war1.show_info()

war2.sleep()
war2.eat()
war2.hit()
war2.walk()
war2.show_info()