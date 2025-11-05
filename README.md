# NIRSpec IFU Medium-Resolution Spectrum Extension Guide

This guide explains how to extend the **NIRSpec/IFU medium-resolution** spectrum to obtain a full spectral coverage and consistent flux calibration to remove the contamination of the second and third order spectra.
If you use this code in your research, please cite: [Parlanti et. al 2025](XXXXXX).



## Requirements
This code has been developed and tested with:

- **JWST pipeline:** `1.8.1`  
- **CRDS context:** `1346`

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

## Usage

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

Then, you need to comment out **lines 281–284** in the file:
```bash
jwst/assign_wcs/nirspec.py
```

You can either do this manually or automatically by running the following command:


```bash
XXX
```


If successful you should see these lines commented:
```python
     #if detector == "NRS2" and grating.endswith("M"):
         # Mid-resolution gratings do not project on NRS2.
        # log.critical(log_message)
        # raise NoDataOnDetectorError(log_message)
```

---








