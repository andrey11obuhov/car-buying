import pandas as pd
import json
import kivy   
from kivy.app import App    
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

with open("cars.json", "r") as file:
  data = json.load(file)
  
cars=pd.DataFrame(data)
cars=cars.T
namjes=['hp', 'wd', 'price', 'seats','running', 'dtp', 'type','v_engine', 'engine_type', 'years','fuel_economy','acceleration', 'top_speed', 'v_trunk', 'box']
for i in range(15):

  cars=cars.rename(columns={i:namjes[i]})
cars[['hp','price', 'seats','running', 'dtp', 'years', 'top_speed', 'v_trunk' ]]=cars[['hp','price', 'seats','running', 'dtp', 'years', 'top_speed', 'v_trunk' ]].astype('int')
cars[['v_engine', 'fuel_economy', 'acceleration']]=cars[['v_engine', 'fuel_economy', 'acceleration']].astype('float')
cars=cars.astype({'wd':'string','type':'string', 'box':'string', 'engine_type':'string' })
def select(purpose):
  def hp_ball( hp):
    if purpose=='family':
      return round(hp/100)
    else:
      return 21-round(hp/100)
  
  def price_ball(price):
    return round(price/50000)+1

  def wd_ball(wd):
    p=0
    if purpose=='family':
      if wd=='RWD':
        p=20
      else:
        p=10
    else:
      if wd=='FWD':
        p=30
      elif wd=='RWD':
        p=20
      else:
        p=10
    return p

  def type_ball(type):
    p=0
    if purpose=='family':
      if type=='Minivan':
        p=10
      elif type in ['SUV', 'Crossover', 'Sedan', 'Hatchback']:
        p=20
      elif type in ['Pickup truck', 'gt']:
        p=30
      else:
        p=120
    elif purpose=='speed':
      if type in ['Racecar', 'hypercar', 'muscle car']:
        p=10
      elif type=='gt':
        p=30
      elif type in ['Coupe', 'Sports car']:
        p=20
      elif type in ['Sedan', 'Hatchback']:
          p=60
      elif type in ['Pickup truck', 'SUV', 'Crossover']:
          p=120
      else:
          p=300
    else:
      if type in ['SUV', 'Crossover','Pickup truck']:
        p=10
      elif type=='Minivan':
        p=40
      elif type=='Hatchback':
        p=20
      else:
        p=300
    return p

  def dtp_ball(dtp):
    p=0
    if dtp!=0:
      p= dtp*10
    return p

  def seats_ball(seats):
    p=0
    if purpose=='family':
      if seats==7:
        p=10
      elif seats==5:
        p=20
      else:
        p=500
    else:
      if seats==7:
        p=100
      elif seats==5:
        p=50
      else:
        p=10
    return p
  
  def v_engine_ball( v_engine):
    p=0
    if purpose=='family':
      if v_engine >=1.6 and v_engine<=2.:
        p=10
      elif v_engine>2. and v_engine<=3.5:
        p=30
      elif v_engine>3.5 and v_engine<=5.:
        p=70
      elif v_engine>5.:
        p=int(v_engine*10)
    else:
      if v_engine>=1.6 and v_engine<=2.:
        p=120
      elif v_engine>2. and v_engine<=3.5:
        p=30
      elif v_engine>3.5 and v_engine<=5.:
        p=20
      elif v_engine>5.:
        p=10
    return p
        
  def v_trunk_ball(v_trunk):
    if purpose=='family' and purpose=='off-road':
      return 11-(v_trunk/100)
    else:
      return round(v_trunk/100)
    
  def engine_type_ball(engine_type):
    p=0
    if purpose=='family':
      if engine_type=='electro':
        p=10
      elif engine_type in ['disel', 'hybrid']:
        p=20
      else:
        p=40
    elif purpose=='speed':
      if engine_type=='electro':
        p=20
      elif engine_type=='hybrid':
        p=10
      else:
        p=100
    else:
      if engine_type=='auto':
        p=20
      elif engine_type=='mannual':
        p=10
    return p

  def years_ball(years):
    return years+1

  def fuel_economy_ball(fuel_economy):
    return int(round(fuel_economy))-4

  def acceleration_ball(acceleration):
    p=0
    if purpose=='family':
      if acceleration>=7. and acceleration<=10:
        p=10
      elif acceleration<=3.:
        p=100
      else:
        p=50
    else:
      p=round(acceleration)
    return p
  
  def box_ball(box):
    p=0
    if purpose=='family':
      if box=='auto':
        p=10
      else:
        p=100
    elif purpose=='speed':
      if box=='auto':
        p=200
      else:
        p=10
    else:
      if box=='auto':
        p=50
      else:
        p=10
    return p
      
      
  def top_speed_ball(top_speed):
    p=0
    if purpose=='family':
      if top_speed<250 and top_speed>130:
        p=10
      elif top_speed<130:
        p=500
      else: 
        p=top_speed/10
    else:
      p=51-(top_speed/10)
    return p
    
  def running_ball(running):
    return running/1000 + 1
  
  cars["hp_ball"]=cars.hp.apply(hp_ball)
  cars["price_ball"]=cars.price.apply(price_ball)
  cars["years_ball"]=cars.years.apply(years_ball)
  cars["running_ball"]=cars.running.apply(running_ball)
  cars["v_trunk_ball"]=cars.v_trunk.apply(v_trunk_ball)
  cars["wd_ball"]=cars.wd.apply(wd_ball)
  cars["seats_ball"]=cars.seats.apply(seats_ball)
  cars["dtp_ball"]=cars.dtp.apply(dtp_ball)
  cars["fuel_economy_ball"]=cars.fuel_economy.apply(fuel_economy_ball)
  cars["type_ball"]=cars.type.apply(type_ball)
  cars["v_engine_ball"]=cars.v_engine.apply(v_engine_ball)
  cars["engine_type_ball"]=cars.engine_type.apply(engine_type_ball)
  cars["acceleration_ball"]=cars.acceleration.apply(acceleration_ball)
  cars["box_ball"]=cars.box.apply(box_ball)
  cars["top_speed_ball"]=cars.top_speed.apply(top_speed_ball)

  cars["sum1"]=cars["hp_ball"]+cars["price_ball"]+cars["years_ball"]+cars["running_ball"]+cars["v_trunk_ball"]+cars["wd_ball"]+cars["seats_ball"]+cars["dtp_ball"]+cars["fuel_economy_ball"]+cars["type_ball"]+cars["engine_type_ball"]+cars["acceleration_ball"]+cars["box_ball"]+cars["top_speed_ball"]

  cars["sum2"]=cars.hp_ball+cars.wd_ball+cars.v_trunk_ball+cars.seats_ball+cars.type_ball+cars.v_engine_ball+cars.acceleration_ball+cars.box_ball+cars.top_speed_ball+cars.engine_type_ball


  cars["sum3"]=cars.price_ball+cars.years_ball+cars.running_ball+cars.dtp_ball+cars.fuel_economy_ball
  def calculations():
    auto=''
    res=cars.query('sum2==sum2.min()')
    if res.shape[0]==1:
      auto=res.index[0]
    else:
      res=res.query('sum3==sum3.min()')
      if res.shape[0]==1:
        auto=res.index[0]
      else:
        res=res.query('sum1==sum1.min()')
        auto=res.index[0]
    return auto
  calc=calculations()
  return calc
purposes=['family', 'speed', 'off-road']
class MainWidget(BoxLayout):
    def get_car(self):
        if self.name_input.text in purposes:
            carsres=select(self.name_input.text)
            car_info=data.get(carsres)
            names=['Horse power: ', 'Drivetrain: ', 'Price: ',
             'Number of seats: ','Mileage: ',
             'Accidents or damage: ', 'Class: ',
             'Engine capacity: ', 'Engine: ', 'Age: ',
             'Fuel economy: ','Acceleration 0-100:  ',
             'Top speed: ', 'Trank capacity: ', 'Transmision: ']
            out=dict(zip(names, car_info))
            s=''
            for i in out:
                s=s.__add__(str(i)+str(out.get(i))+'\n')
            self.hello_label.text =carsres+'\n'+s
        else:
            self.hello_label.text='There is no such purpose'
    hello_label = ObjectProperty()
    name_input = ObjectProperty()
    pass


class MainApp(App):

    def build(self):
        return MainWidget()


if __name__ == '__main__':
    app = MainApp()
    app.run()