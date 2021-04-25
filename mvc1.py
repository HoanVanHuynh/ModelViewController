# https://www.djangospin.com/design-patterns-python/model-view-controller-mvc/
# Model-View-Controller is the most popular Architectural Pattern practised in the industry. 
#
# It is widely used to design web applications and desktip GUIs i.e. Graphical User Interfaces.
# It is based on the idea of dividing the application into three parst i.e. Model, View and Controller. 
# 
# 

class FamousQuotation(object):
    '''Model: houses two attributes of every Famous Quotation: speaker and the quote.'''
    def __init__(self, speaker, famousQuotation):
        self.speaker = speaker
        self.famousQuotation = famousQuotation

# render: to express or present something in a particular way

class FamousQuotationGUI(object):
    '''View: responsible for rendering information to the front-end of the application.
    For this demonstration, let's just print the information on the console.'''
    def printQuotationDetails(self, speaker, famousQuotation):
        print('{} _ {}'.format(famousQuotation, speaker))        

class FamousQuotationController(object):
    '''Controller: creates objects of the model,
    is capable of manipulating its atrributes, and sends commands to the
    associated view to render the information on the front-end.''' 

    def __init__(self, model, view):
        self.model = model 
        self.view = view 

    def setFamousQuotationSpeaker(self, speaker):
        self.model.speaker = speaker 

    def getFamousQuotationSpeaker(self):
        return self.model.speaker 

    def setFamousQuotationQuotation(self, famousQuotation):
        self.model.famousQuotation = famousQuotation 

    def getFamousQuotationQuotation(self):
        return self.model.famousQuotation 

    def renderInformationOnFrontEnd(self):
        self.view.printQuotationDetails(self.model.speaker, self.model.famousQuotation)        

famousQuotationOne = FamousQuotation('M k Gandhi', 'An eye for an eye ends up making up the whole world blind.')        
famousQuotationGUI = FamousQuotationGUI()
controllerOne = FamousQuotationController(famousQuotationOne, famousQuotationGUI)

controllerOne.renderInformationOnFrontEnd()
controllerOne.setFamousQuotationSpeaker('Mohandas K Gandhi')
controllerOne.renderInformationOnFrontEnd()
