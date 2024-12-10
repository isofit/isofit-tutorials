import sys

print("Executing this file directly is not the intended purpose. Please see the README. Exiting")
sys.exit()

#%%

import logging
import numpy as np
import os

logging.basicConfig(level=logging.DEBUG)

from isofit.configs import configs
from isofit.data    import env
from isofit.radiative_transfer.engines.six_s import SixSRT

env.load()

# Initialize the config
cf = env.path('examples', '20151026_SantaMonica', 'configs', 'run', 'prm20151026t173213_D9W_6s.json')
fc = full_config   = configs.create_new_config(cf)
ec = engine_config = fc.forward_model.radiative_transfer.radiative_transfer_engines[0]
lg = lut_grid      = fc.forward_model.radiative_transfer.lut_grid

# Update config for this test
ec.engine_base_dir = env.path('sixs')
ec.statevector_names = []

#% Remove the LUT file, comment this if testing pre-existing lut
import os
if os.path.exists(ec.lut_path):
    os.remove(ec.lut_path)

# override size instead of using a wavelength_file (this is how sRTMnet uses 6S)
N = 831

#%%

rte = SixSRT(
    engine_config          = ec,
    interpolator_style     = fc.forward_model.radiative_transfer.interpolator_style,
    overwrite_interpolator = fc.forward_model.radiative_transfer.overwrite_interpolator,
    wavelength_file        = env.path('data', '20140221_PRISM_wavelengths_truncated_clip.txt'),
    lut_grid               = lut_grid,
    lut_path               = ec.lut_path,
    # Override
    # wl                     = np.linspace(350, 2500, N),
    # fwhm                   = np.full(N, 2)
)

#%%
# Load the LUT and look around
rte.lut.load()
rte.lut.isel(point=6)
