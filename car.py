import random
import json
class car(object):
    def __init__(self,  hp, wd, price, seats,
    running, dtp, type, v_engine, 
    engine_type, years, fuel_economy, acceleration, top_speed, 
     v_trunk, box):
        self.hp=hp
        self.wd=wd
        self.price=price
        self.seats=seats
        self.running=running
        self.dtp=dtp
        self.type=type
        self.v_engine=v_engine
        self.v_trunk=v_trunk
        self.engine_type=engine_type
        self.years=years
        self.fuel_economy=fuel_economy
        self.acceleration=acceleration
        self.box=box
        self.top_speed=top_speed
def how_many_seats(type):
    if type in ['SUV', 'Sedan', 'Hatcback', 'Crossover', 'Pickup truck']:
        return 5
    elif type in ['Coupe', 'Sports car', 'Racecar', 'hypercar', 'muscle car', 'gt']:
        return 2
    elif type=='Minivan':
        return 7

def generate_car():
    hp=random.randint(50, 2000)
    wd=random.choice(['AWD', 'FWD', 'RWD'])
    price=random.randint(50, 100000)*1000
    running=random.randint(1, 500)*1000*random.choice([0, 1])
    dtp=random.randint(0, 10)*random.choice([0, 0, 0, 0, 0, 0, 1, 1, 0])
    type=random.choice(['SUV', 'Sedan', 'Hatcback', 'Crossover', 'Coupe', 'Minivan', 'Sports car', 'Racecar', 'Pickup truck', 'hypercar', 'muscle car', 'gt'])
    seats = how_many_seats(type)
    v_engine=round(random.uniform(1.6, 10.), 1)
    v_trunk=random.randint(100, 1000)
    engine_type=random.choice(['disel', 'gasoline', 'electro', 'hybrid'])
    years=random.randint(0, 40)
    fuel_economy=round(random.uniform(5., 20.), 1)
    acceleration=round(random.uniform(1.9,10.), 1)
    box=random.choice(['auto', 'robot', 'mannual'])
    top_speed=random.randint(150, 500)
    return car( hp, wd, price, seats,
    running, dtp, type, v_engine, 
    engine_type, years, fuel_economy, acceleration, top_speed, 
     v_trunk, box)
lists_of_cars={}
v=generate_car()
lis=[]
for i in range(1000):
    v=generate_car()
    lis=[v.hp, v.wd, v.price, v.seats,
    v.running, v.dtp, v.type, v.v_engine, 
    v.engine_type, v.years, v.fuel_economy, v.acceleration, v.top_speed, 
     v.v_trunk, v.box]
    lists_of_cars.update({'car #'+str(i) : lis})

print (lists_of_cars)

with open("cars.json", "w") as ile:
     json.dump(lists_of_cars, ile)