class parent:
    def myMethod (self):
        print ('calling parent method')
class child(parent):
    def myMethod (self):
        print('calling child method')
c = child()
c.myMethod()