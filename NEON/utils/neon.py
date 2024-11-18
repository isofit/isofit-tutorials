import numpy as np

# Extract the image locations of each point of interest (POI)
# These are defined in the NEON report as pixel locations, so we round here to convert to indices
report = {}
report['173647'] = {           # Upp L Y  | Low R Y  | Upp L X | Low R X
    'WhiteTarp': np.round([2224.9626, 2230.9771, 316.0078, 324.9385,]).astype(int),
    'BlackTarp': np.round([2224.9626, 2231.0032, 328.0086, 333.9731,]).astype(int),
    'Veg'      : np.round([2245.0381, 2258.8103, 343.9006, 346.9423,]).astype(int),
    'RoadEW'   : np.round([2214.9905, 2216.9978, 348.9902, 373.0080,]).astype(int),
    'RoadNS'   : np.round([2205.9580, 2225.9612, 357.9536, 359.9608,]).astype(int)
}
report['174150'] = {           # Upp L Y | Low R Y | Upp L X  | Low R X
    'WhiteTarp': np.round([653.9626, 659.9771, 3143.0078, 3151.9385]).astype(int),
    'BlackTarp': np.round([653.9626, 660.0032, 3155.0086, 3160.9731]).astype(int),
    'Veg'      : np.round([674.0381, 687.8103, 3170.9006, 3173.9423]).astype(int),
    'RoadEW'   : np.round([643.9905, 645.9978, 3175.9902, 3200.0080]).astype(int),
    'RoadNS'   : np.round([634.9580, 654.9612, 3184.9536, 3186.9608]).astype(int)
}
# Converts numpy array to comma-separated string for ISOFIT
toString = lambda array: ', '.join(str(v) for v in array)
