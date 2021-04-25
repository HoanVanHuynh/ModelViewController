# Model: this declares a class to store and manipulate data
# View: this declares a class to build user interfaces and data displays 
# Controller: this declares a class that connects the model and view 
# User: this declares a class that requests for certain results based on certain actions 

class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2,}, 
        'sms':   {'number': 1000, 'price': 10,}, 
        'voice': {'number': 1000, 'price': 15, },
    }

class View(object):
    def list_services(self, services):
        for svc in services:
            print(svc, ' ')

    def list_pricing(self, services):
        for svc in services:
            print('For', Model.services[svc]['number'])
            print(svc, 'message you pay $', Model.services[svc]['price'])            

class Controller(object):
    def __init__(self):
        self.model = Model() 
        self.view = View() 
    
    def get_services(self):
        services = self.model.services.keys() 
        return (self.view.list_services(services))

    def get_pricing(self):
        services = self.model.services.keys() 
        return (self.view.list_pricing(services))

class Client(object):
    controller = Controller()
    print('Services Provided: ')
    controller.get_services()
    print('Pricing for Services: ')
    controller.get_pricing()
    
