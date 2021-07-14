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