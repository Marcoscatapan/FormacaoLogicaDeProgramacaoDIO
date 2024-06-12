class Hero:
    def __init__(self, name, age, hero_type):
        self.name = name
        self.age = age

        self.types = ["mago", "guerreiro", "monge", "ninja"]
        self.attacks = ["spell", "corteFulminante", "meditacao", "katana"]
        self.type = hero_type % len(self.types)

    def get_type(self):
        return self.types[self.type]

    def get_attack(self):
        return self.attacks[self.type]

    def attack(self):
        print(f"O {self.get_type()} atacou usando {self.get_attack()}")

    def info(self):
        print(f"Nome: {self.name}, idade: {self.age}, Tipo: {self.get_type()}")


for i in range(4):
    marquinho = Hero("marquinho", 0, i)
    marquinho.attack()