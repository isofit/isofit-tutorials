import numpy as np
from spectral import envi

from isofit.core.common import envi_header

path = '/Users/bgreenbe/.isofit/examples/20231110_Prism_Multisurface/output/prm20231110t071521_multi_surface_state'
ds = envi.open(envi_header(path))
im = ds.load()
