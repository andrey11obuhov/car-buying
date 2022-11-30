def hp_ball(purpose, hp):
  if purpose== 'family':
    return round(hp/100)
  else:
    return 21- round(hp/100)
 
def price_ball(price):
  return round(price/50000)+1

def wd_ball(purpose, wd):
  if purpose=='family':
    if wd=='RWD':
      return 2
    elif wd in ['FWD','AWD']:
      return 1
   elif purpose in ['speed','off-road']:
    if wd=='FWD':
      return 3
    elif wd=='RWD':
      return 2
    elif wd=='AWD'
      return 1

def type_ball(purpose, type):
  if purpose=='family':
    if type=='Minivan':
      return 1
    elif type in ['SUV', 'Crossover', 'Sedan', 'Hatchback']:
      return 2
    elif type in ['Pickup truck', 'gt']:
      return 3
    elif type in ['Coupe', 'Sports car', 'Racecar', 'hypercar', 'muscle car']:
      return 12
  elif purpose=='speed':
    if type in ['Racecar', 'hypercar', 'muscle car']:
      return 1
    elif type=='gt':
      return 3
    elif type in ['Coupe', 'Sports car']:
      return 2
    elif type in ['Sedan', 'Hatchback']:
      return 4
    elif type in ['Pickup truck', 'SUV', 'Crossover']:
      return 6
    elif type=='Minivan':
      return 12
   elif purpose=='off-road':
    if type in ['SUV', 'Crossover',]'Pickup truck']:
      return 1
    elif type=='Minivan':
      return 4
    elif type=='Hatchback':
      return 2
    else:
      return 12

def dtp_ball(dtp):
    if dtp==0:
      return 0
    else:
      return dtp*10

def seats_ball(purpose, seats):
    if purpose=='family':
      if seats==7:
        return 1
      if seats==5:
        return 2
      if seats==2:
        return 5
    elif purpose=='speed' or purpose=='off-road':
      if seats==7:
        return 10
      if seats==5:
        return 5
      if seats==2:
        return 1
 
def v_engine_ball(purpose, v_engine):
  if purpose=='family':
    if v_engine=>1.6 and v_engine<=2.:
      return 1
    elif v_engine>2. and v_engine<=3.5:
      return 3
    elif v_engine>3.5 and v_engine<=5.:
      return 7
    elif v_engine>5.:
      return int(v_engine*10)
   elif purpose=='speed' or purpose=='off-road':
     if v_engine=>1.6 and v_engine<=2.:
        return 12
      elif v_engine>2. and v_engine<=3.5:
        return 3
      elif v_engine>3.5 and v_engine<=5.:
        return 2
      elif v_engine>5.:
        return 1
      
def v_trunk_ball(purpose, v_trunk):
  if purpose=='family':
    return 11-(v_trunk/100)
  else:
    return v_trunk/100
  
def engine_type_ball(purpose, engine_type):
  if purpose=='family':
    if engine_type=='electro':
      return 1
    elif engine_type in ['disel', 'hybrid']:
      return 2
    elif engine_type=='gasoline':
      return 4
  else:
    if engine_type=='electro':
      return 4
    elif engine_type=='hybrid':
      return 3
    elif engine_type in ['gasoline', 'hybrid']:
      return 1

def years_ball(years):
  return years+1

def fuel_economy_ball(fuel_economy):
  return int(round(fuel_economy))-4

def acceleration_ball(purpose, acceleration):
  if purpose=='family':
    if acceleration=>7. and acceleration<=10:
      return 1
    elif acceleration<=3.:
      return 10
    else:
      return 5
   else:
    return round(acceleration)
 
def box_ball(purpose, box):
  if purpose=='family':
    if box=='auto':
      return 1
    else:
      return 10
  else:
     if box=='auto':
      return 10
    else:
      return 1
    
    
def top_speed_ball(purpose, top_speed):
  if purpose=='family':
    if top_speed<250:
      return 1
    else: 
      return top_speed/10
   else:
    return 51-(top_speed/10)
  
def running_ball(running):
  return running/1000 + 1
