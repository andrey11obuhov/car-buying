import json
import kivy   
from kivy.app import App    
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
with open("cars.json", "r") as file:
  data = json.load(file)
carsres={'family':'car #564', 'speed':'car #632',
'off-road': 'car #140'} 
purposes={'family':data.get('car #564'), 'speed':data.get('car #632'),
'off-road': data.get('car #140')}
out={}
class MainWidget(BoxLayout):
    def get_car(self):
        if self.name_input.text in purposes:
            car_info=purposes.get(self.name_input.text)
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
            self.hello_label.text =carsres.get(self.name_input.text)+'\n'+s
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
