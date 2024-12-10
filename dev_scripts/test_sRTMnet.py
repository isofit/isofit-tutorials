import sys

print("Executing this file directly is not the intended purpose. Please see the README. Exiting")
sys.exit()

#%%

import os
import logging

logging.basicConfig(level=logging.INFO)

from isofit.configs import configs
from isofit.data    import env
from isofit.radiative_transfer.engines.sRTMnet import SimulatedModtranRT

env.load()

cf = env.path('examples', '20171108_Pasadena', 'configs', 'modtran', 'ang20171108t184227_beckmanlawn.json')
fc = full_config   = configs.create_new_config(cf)
ec = engine_config = fc.forward_model.radiative_transfer.radiative_transfer_engines[0]
lg = lut_grid      = fc.forward_model.radiative_transfer.lut_grid

#% Update config params for this test
ec.wavelength_range  = None
ec.irradiance_file   = env.path('examples', '20151026_SantaMonica', 'data', 'prism_optimized_irr.dat')
ec.engine_base_dir   = env.path('sixs')

# Path to emulator
ec.emulator_aux_file = env.path('srtmnet', 'sRTMnet_v120_aux.npz')
ec.emulator_file     = env.path('srtmnet', 'sRTMnet_v120.h5')

#% Remove LUT files
files = [
    ec.lut_path,
    '6S.' + ec.lut_path,
    ec.sim_path + '/sRTMnet.predicts.nc'
]

for file in files:
    if os.path.exists(file):
        print(f'Removing {file}')
        os.remove(file)

#%%

rte = SimulatedModtranRT(
    engine_config          = ec,
    interpolator_style     = fc.forward_model.radiative_transfer.interpolator_style,
    overwrite_interpolator = fc.forward_model.radiative_transfer.overwrite_interpolator,
    wavelength_file        = fc.forward_model.instrument.wavelength_file,
    lut_grid               = lut_grid,
    lut_path               = ec.lut_path
)

#%%
# Load the LUT and look around
rte.lut.load()
