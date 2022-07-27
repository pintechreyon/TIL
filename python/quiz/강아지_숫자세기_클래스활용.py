class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    @classmethod
    def get_status(cls):
        print(f'지금 살아있는 강아지: {cls.num_of_dogs}마리')

    def __init__(self,name,species):
        self.name = name
        self.species = species
        print(f'{species}종 {name}가 태어났습니다')
        Doggy.num_of_dogs +=1
        Doggy.birth_of_dogs +=1
            

    def bark(self):
        print(f'{self.name}가 멍멍!')

    def died(self):
        Doggy.num_of_dogs -= 1
        print(f'{self.name}가 무지개 다리를 건넜습니다.')
    
dog1 = Doggy('똘똘이','똥개')
dog2 = Doggy('개똥이','잡종')
dog1.bark()
dog1.died()
Doggy.get_status()

