# NIRSpec IFU Medium-Resolution Spectrum Extension Guide

This guide explains how to apply all the changes to the pipeline to extend the **NIRSpec/IFU medium-resolution** spectrum, thereby obtaining full spectral coverage and consistent flux calibration to remove contamination from the second and third order spectra.
If you use this products in your research, please cite: [Parlanti et. al 2025](XXXXXX).



## Requirements
This code has been developed and tested with:

- **JWST pipeline:** `1.18.1`, `1.19.1`    
- **CRDS context:** `1364`

Support for different pipeline versions and contexts will be added as they are released.  
If you need a specific implementation for another context or pipeline version, please contact:  
📧 [eleonora.parlanti@sns.it](mailto:eleonora.parlanti@sns.it)

---

## Overview

The extended reduction recovers and calibrates the non-nominal region of the NIRSpec/IFU **medium-resolution grating/filters G140M/F100LP and G235M/F170LP**.  
It provides the following improvements:

- **Extended wavelength coverage:** up to 3.5 μm for G140M/F100LP and up to 5.27 μm G235M/F170LP
- **Increased spectral resolution:** up to *R* ≈ 2500 (≈×2 compared to the nominal range).  
- **Flux calibration and suppression of 2nd- and 3rd-order contamination** through custom reference and calibration files.  

All required **reference and calibration files** are provided as machine-readable files, enabling the community to apply the extension directly to their data.

---

## How to use it

### Installation of the pipeline:

You can install the required pipeline version using `pip`.  
It is recommended to create a **dedicated environment** separate from your main data-reduction setup.  

From a **bash/zsh** shell:

```bash
conda create -n <env_name> python=3.13
conda activate <env_name>
pip install jwst==1.18.1
```

If you have problems with the installation of the JWST pipeline, please refer to: [jwst](https://github.com/spacetelescope/jwst).

---

### Modification of the pipeline:

We need to modify one pipeline file to extend the nominal wavelength range of the **NIRSpec IFU medium-resolution** data.
You can locate the folder containing the installed `jwst` package with:

```bash
cd $(python -c "import site; print(site.getsitepackages()[0])")
```

Then, you need to comment out in the file:
```bash
jwst/assign_wcs/nirspec.py
```

The lines containing:

```python
     if detector == "NRS2" and grating.endswith('M'):
        # Mid-resolution gratings do not project on NRS2.
        log.critical(log_message)
        raise NoDataOnDetectorError(log_message)
```


You can either do this manually or automatically by running the script `modify_pipeline.py`.
If successful, you should see these lines commented:
```python
     #if detector == "NRS2" and grating.endswith("M"):
         # Mid-resolution gratings do not project on NRS2.
        # log.critical(log_message)
        # raise NoDataOnDetectorError(log_message)
```

These lines raise errors when attempting to run the JWST pipeline for IFU data using the second detector (NRS2).
Commenting them allows the reduction to proceed and access the extended wavelength range.

---

### Adding the modified reference files

Before running the reduction, make sure to modify the required **reference and calibration files**.  
You should *add or replace the existing ones* in the folder defined as your `CRDS_PATH` in the Python script.

For example, if in your script you set:

```python
os.environ["CRDS_PATH"] = "/path/to/my/folder/"
```

The folder where you must place or update the reference files needed for the extended reduction is `/path/to/my/folder/references/jwst/nirspec/`.


> 💡 **Tip:**  
> It is recommended to create a **separate `CRDS_PATH` folder** for the extended pipeline, distinct from the one you use for the nominal JWST pipeline.  
> This will prevent conflicts or overwriting of official calibration files.


Calibration files for different contexts can be found in the `CTX_XXXX` folder, where XXXX is the number of contexts.



#### Reference File Structures

Below is a summary of the calibration files required for different **grating/filter** combinations and **contexts**.

#### Common to all extensions

| File Type | Context |  Filename Pattern |
|------------|--|-----------------|
| Wavelength Range | 1364 | `jwst_nirspec_wavelengthrange_0008.asdf` |
| Cube Parameters | 1364 | `jwst_nirspec_cubepar_0009.fits` |

You will find the corresponding files for each CTX in the **CTX folder**.

#### Specific Files by Configuration

| Grating/Filter | Context | Required Files |
|----------------|----------|----------------|
| G140M/F100LP | 1364 | `jwst_nirspec_fflat_0105.fits`<br>`jwst_nirspec_sflat_0208.fits`<br>`jwst_nirspec_sflat_0191.fits` |
| G235M/F170LP | 1364 | `jwst_nirspec_fflat_0091.fits`<br>`jwst_nirspec_sflat_0211.fits`<br>`jwst_nirspec_sflat_0192.fits` |

---


With the new reference files and the patched pipeline, please run your code for data reduction. You will end up with the extended, **yet not flux-calibrated**, cube.



## Applying the flux calibration to the reduced cube








