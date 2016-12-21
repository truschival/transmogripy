from transmogripy import __TMG_CONSTANT__ 

class Basic(object):
    '''
    Basic Transmogrification class
    '''
    
    _TRANSMOG_MAGIC=0
    
    def __init__(self, transmogrification_factor=__TMG_CONSTANT__):
        self._TRANSMOG_MAGIC=transmogrification_factor;
    
    def transmogrify(self, a):
        return a*a+self._TRANSMOG_MAGIC

    def banner(self):
        return "Transmogrification constant = %d"%(self._TRANSMOG_MAGIC)


