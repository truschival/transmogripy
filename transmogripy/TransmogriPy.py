
class TransmogriPy(object):
  
    _TRANSMOG_MAGIC=27
    
    def __init__(self, transmogrification_factor=23):
        self._TRANSMOG_MAGIC=transmogrification_factor;
    
    def transmogrify(self, a):
        return a*a+self._TRANSMOG_MAGIC

    def banner(self):
        return "Transmogrification constant = %d"%(self._TRANSMOG_MAGIC)
