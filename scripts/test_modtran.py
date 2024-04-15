import logging
import os
import numpy as np

logging.basicConfig(level=logging.DEBUG)

from isofit.configs import configs
from isofit.radiative_transfer.modtran import ModtranRT


example = 'examples/20171108_Pasadena'

cf = f"{example}/configs/ang20171108t184227_beckmanlawn.json"
fc = full_config = configs.create_new_config(cf)
ec = engine_config = fc.forward_model.radiative_transfer.radiative_transfer_engines[0]
lg = lut_grid = fc.forward_model.radiative_transfer.lut_grid

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

rte.lut.load()
