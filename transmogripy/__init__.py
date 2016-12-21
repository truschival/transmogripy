__all__ = ["transmog"]
__version__ = '1.0'
__TMG_CONSTANT__=4

from transmog import Basic

def print_banner():
    d = Basic()
    print(d.banner())

if __name__ == '__main__':
    print_banner();
