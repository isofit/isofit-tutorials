import os
import logging

logging.basicConfig(level=logging.INFO)

from isofit.configs                    import configs
from isofit.radiative_transfer.sRTMnet import SimulatedModtranRT


example = 'examples/20171108_Pasadena'

cf = f"{example}/configs/ang20171108t184227_beckmanlawn.json"
fc = full_config = configs.create_new_config(cf)
ec = engine_config = fc.forward_model.radiative_transfer.radiative_transfer_engines[0]
lg = lut_grid = fc.forward_model.radiative_transfer.lut_grid

#% Update config params for this test
ec.wavelength_range  = None
ec.irradiance_file   = f"{example}/../20151026_SantaMonica/data/prism_optimized_irr.dat"
ec.engine_base_dir   = os.environ['SIXS_DIR']

# Path to emulator
ec.emulator_aux_file = os.environ['EMULATOR_PATH'] + '/sRTMnet_v100_aux.npz'
ec.emulator_file     = os.environ['EMULATOR_PATH'] + '/sRTMnet_v100'

#% Remove LUT files
files = [
    ec.lut_path,
    ec.lut_path + '.6S',
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

rte.lut.load()
