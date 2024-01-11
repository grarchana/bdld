"""Import all submodules"""
# when doing `import bdld.potential`
from . import dualchannel_doublewell
from . import temperature_switch
from . import entropic_double_well
from . import mueller_brown
from . import polynomial
from . import potential

# when doing `from bdld.potential import *` (not recommended)
__all__ = ["dualchannel_doublewell","temperature_switch","entropic_double_well", "mueller_brown", "polynomial", "potential"]
