from mylib.pedal_function import  PedalFunction

class Pedal:
    def __init__(self, id, name, function, manufacturer, dimensions, current, cost, details):
         self.id = id
         self.name = name
         self.image = f'{id}.b.jpg'
         self.function = function
         self.manufacturer = manufacturer
         self.current = current
         self.cost = cost
         self.width = int(dimensions[0].text.strip().replace('mm wide', '').strip())
         self.height = int(dimensions[1].text.strip().replace('mm high', '').strip())
         self.details = details
         self.hrid = f'{manufacturer}-{name}'.replace(' ', '-').replace('/', '').replace(':', '').lower()
         self.weight = 99

    def setWeight(self, functions):
        my_functions = [i for i in functions if i.function in self.function] 
        try:
            my_functions = sorted(my_functions, key=lambda f: f.weight)
            self.weight = my_functions[0].weight
        except:
            self.weight = 99