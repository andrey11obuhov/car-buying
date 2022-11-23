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
    elif type=='SUV'
    ortype=='Crossover' or type=='Sedan' or type=='Hatchback':
      return 2
    elif type
'SUV', 'Sedan', 'Hatcback', 'Crossover', 'Coupe', 'Minivan', 'Sports car', 'Racecar', 'Pickup truck', 'hypercar', 'muscle car', 'gt'
