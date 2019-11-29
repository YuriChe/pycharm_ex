weight_max = {'weight': 0}

class Goose():
    satiety = 'голодный'
    eggs = 0
    voices = 'гагага'
    name = ''
    animal = 'Гусь'
    weight = 0

    def __init__(self, names, weight_):
        self.name = names
        self.weight = weight_

    def feed(self):
        self.satiety = 'сытый'

    def collect_eggs(self):
        self.eggs += int(input('Сколько яиц собрано?'))

    def voice(self):
        print(self.voices)

    def status_an(self):
        print(self.animal, self.name, self.satiety)
        self.voice()
    pass

class Chiсken(Goose):
    voices = 'кукареку'
    animal = 'Курица'
    pass

class Duck(Goose):
    voices = 'кря кря'
    animal = 'Утка'
    pass

class Cow(Goose):
    milk = 'недоена'
    voices = 'муу'
    animal = 'Корова'

    def milk_it(self):
        self.milk = 'подоена'
    pass

class Sheep(Cow):
    cutting = 'нестрижена'
    voices = 'бее'
    animal = 'Овца'

    def Cut(self):
        self.cutting  = 'стрижена'
    pass

class Goat(Cow):
    voices = 'бебееееее'
    animal = 'Коза'
    pass

def who_max(animal_obj):
    p1 = animal_obj.__dict__
    if p1['weight'] > weight_max['weight']:
       weight_max.update(p1)

Sheep1 = Sheep('Барашек', 21)
Sheep2 = Sheep('Кудрявый', 23)
Chiсken1 = Chiсken('Кукареку', 1.3)
Chiсken2 = Chiсken('Ко Ко', 0.9)
Goose1 = Goose('Серый', 2.6)
Goose2 = Goose('Белый', 2.7)
Duck1 = Duck('Кряква', 1.7)
Goat1 = Goat('Рога', 33)
Goat2 = Goat('Копыта', 29)

Sheep2.feed()
Goose1.voice()
print(Sheep1.name)
Sheep1.voice()
Duck1.collect_eggs()
Chiсken2.collect_eggs()
print(Duck1.eggs, Chiсken2.eggs)
Chiсken2.collect_eggs()
print(Duck1.eggs, Chiсken2.eggs)
Sheep2.status_an()
print(Sheep2.name, Sheep2.satiety)
Goat1.milk_it()
print(Goat1.name, Goat1.milk, Goat2.name, Goat2.milk)
print(Goose1.animal)
print(Goose1.name)

who_max(Sheep1)
who_max(Sheep2)
who_max(Chiсken1)
who_max(Chiсken2)
who_max(Goose1)
who_max(Goose2)
who_max(Duck1)
who_max(Goat1)
who_max(Goat2)

print('Самое тяжелое животноу', weight_max['name'], 'с весом', weight_max['weight'])


# Cow1 = Cow()
#
#
# Goose1 = Goose()
# Duck1 = Duck()
# Cow1.voice()
# Cow1.feed()
# print(Cow1.satiety)
# Chiсken1 = Chiсken('milked')
# Chiсken1.voice()
