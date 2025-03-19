__all__,__version__=(lambda x:(x,x.pop()))('__main__ install uninstall conf 0.0.1'.split())

try: import builtins as __builtin__
except: import __builtin__

__builtin__.conf = None
from conf import img as __img
__builtin__.default_img = __img
del __builtin__.conf, __img