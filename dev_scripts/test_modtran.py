import sys

print("Executing this file directly is not the intended purpose. Please see the README. Exiting")
sys.exit()

#%%

import os
import logging

logging.basicConfig(level=logging.INFO)

from isofit.configs import configs
from isofit.data    import env
from isofit.radiative_transfer.modtran import ModtranRT

env.load()

cf = env.path('examples', '20171108_Pasadena', 'configs', 'modtran', 'ang20171108t184227_beckmanlawn.json')
fc = full_config   = configs.create_new_config(cf)
ec = engine_config = fc.forward_model.radiative_transfer.radiative_transfer_engines[0]
lg = lut_grid      = fc.forward_model.radiative_transfer.lut_grid

# Update config for this test
...

#% Remove the LUT file, comment this if testing pre-existing lut
import os
if os.path.exists(ec.lut_path):
    os.remove(ec.lut_path)

# Disable Modtran's makeSim for local testing
ModtranRT.makeSim = lambda *_: ...

# Build the RTE
rte = ModtranRT(
    engine_config          = engine_config,
    lut_grid               = lut_grid,
    lut_path               = engine_config.lut_path,
    wavelength_file        = fc.forward_model.instrument.wavelength_file,
    interpolator_style     = fc.forward_model.radiative_transfer.interpolator_style,
    overwrite_interpolator = fc.forward_model.radiative_transfer.overwrite_interpolator,
    cache_size             = fc.forward_model.radiative_transfer.cache_size
)

#%%
# Load the LUT and look around
rte.lut.load()
