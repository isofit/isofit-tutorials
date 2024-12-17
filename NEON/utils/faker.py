import logging

from spectral.io import envi


Logger = logging.getLogger(__file__)


def getMetadata(file, remove=['fwhm', 'band names', 'wavelength', 'wavelength units']):
    """
    Retrieves the metadata from an envi header

    Parameters
    ----------
    rdn: str
        Path to the RDN header file containing metadata
    remove: list, default=['fwhm', 'band names', 'wavelength', 'wavelength units']
        Removes keys from the metadata dictionary
    """
    rdn_ds   = envi.open(file)
    metadata = rdn_ds.metadata.copy()
    for key in remove:
        if key in metadata:
            del metadata[key]
        else:
            Logger.warning(f'Key {key!r} not found in the metadata, skipping')

    return metadata


def fakeLOC(rdn, lon, lat, elv, output=None, **kwargs):
    """
    Creates a fake LOC file

    Parameters
    ----------
    rdn: str
        Path to the RDN header file containing metadata
    lon: float
        Longitude value for location
    lat: float
        Latitude value for location
    elv: float
        Elevation in kilometers
    output: str, default=None
        Path to write the LOC file to. If None, will attempt to replace the
        substring 'rdn' in the `rdn` path with `loc`
    **kwargs
        Additional arguments passed to getMetadata()
    """
    if not output:
        if 'rdn' in rdn:
            output = rdn.replace('rdn', 'loc')
        else:
            Logger.error('No ouput file specified and cannot generate a unique name')
            return False

    metadata = getMetadata(rdn, **kwargs)
    metadata['bands'] = 3

    ds  = envi.create_image(output, metadata, ext='', force=True)
    loc = ds.open_memmap(interleave='bip', writable=True)

    loc[..., 0] = lon
    loc[..., 1] = lat
    loc[..., 2] = elv

    del ds, loc

    return output


def fakeOBS(rdn, param0=0, sea=0, sez=0, soa=0, soz=0, phase=0, slope=0, aspect=0, cosi=0, param9=0, param10=0, output=None, **kwargs):
    """
    Creates a fake OBS file

    Parameters
    ----------
    rdn: str
        Path to the RDN file containing metadata
    param0: int, float, default=0
        Parameter 0
    sea: int, float, default=0
        Solar Azimuth
    sez: int, float, default=0
        Sensor Zenith
    soa: int, float, default=0
        Solar Azimuth
    soz: int, float, default=0
        Solar Zenith
    phase: int, float, default=0
        Phase
    slope: int, float, default=0
        Slope
    aspect: int, float, default=0
        Aspect
    cosi: int, float, default=0
        COS(i)
    param9: int, float, default=0
        Parameter 9
    param10: int, float, default=0
        Parameter 10
    output: str, default=None
        Path to write the OBS file to. If None, will attempt to replace the
        substring 'rdn' in the `rdn` path with `obs`
    **kwargs
        Additional arguments passed to getMetadata()
    """
    if not output:
        if 'rdn' in rdn:
            output = rdn.replace('rdn', 'obs')
        else:
            Logger.error('No ouput file specified and cannot generate a unique name')
            return False

    rdn_ds   = envi.open(rdn)
    metadata = getMetadata(rdn, **kwargs)
    metadata['bands'] = 11

    ds  = envi.create_image(output, metadata, ext='', force=True)
    obs = ds.open_memmap(interleave='bip', writable=True)

    obs[...,  0] = param0
    obs[...,  1] = sea
    obs[...,  2] = sez
    obs[...,  3] = soa
    obs[...,  4] = soz
    obs[...,  5] = phase
    obs[...,  6] = slope
    obs[...,  7] = aspect
    obs[...,  8] = cosi
    obs[...,  9] = param9
    obs[..., 10] = param10

    del ds, obs

    return output
