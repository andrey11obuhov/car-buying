def hp_ball(purpose, hp):
  if purpose== 'family':
    return round(hp/100)
  else:
    return 21- round(hp/100)
 
def price_ball(purpose, price):
  return round(price/50000)+1

def wd_ball(purpose, wd):
  if purpose=='family':
    if wd=='RWD':
      return 2
    elif wd=='FWD' or wd=='AWD':
      return 1
   elif purpose=='speed' or purpose=='off-road':
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
    elif type=='SUV' or type=='Crossover' or type=='Sedan' or type=='Hatchback':
      return 2
    elif type=='Pickup truck' or type=='gt':
      return 3
    elif type=='Coupe' or type=='Sports car' or type=='Racecar' or type=='hypercar' or type=='muscle car':
      return 12
  elif purpose=='speed':
    if type=='Racecar' or type=='hypercar' or type=='muscle car':
      return 1
    elif type=='gt':
      return 3
    elif type=='Coupe' or type=='Sports car':
      return 2
    elif type=='Sedan' or type=='Hatchback':
      return 4
    elif type=='Pickup truck' or type=='SUV' or type=='Crossover':
      return 6
    elif type=='Minivan':
      return 12
   elif purpose=='off-road':
    if type=='SUV' or type=='Crossover' or type=='Pickup truck':
      return 1
    elif type=='Minivan':
      return 4
    elif type=='Hatchback':
      return 2
    else:
      return 12
  
