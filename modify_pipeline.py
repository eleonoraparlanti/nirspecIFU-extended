import os
import importlib.util
import jwst
spec = importlib.util.find_spec("jwst.assign_wcs.nirspec")

n_lines = 3
marker = 'if detector == "NRS2" and grating.endswith('



if spec is None or not spec.origin:
    raise FileNotFoundError(
        "Cannot find the file jwst/assign_wcs/nirspec.py in your Python environment. "
        "Are you sure you have jwst installed?\n"
        "Try running: 'which jwst'"
    )


filename = spec.origin

with open(filename, 'r') as f:
    lines = f.readlines()

# Search the line and comment that line and the three lines following it
for i, line in enumerate(lines):
    if marker in line:
        print('Line Found!')
        for j in range(i, min(i + n_lines + 1, len(lines))):
            if not lines[j].lstrip().startswith("#"):  ## If already patched is not patching it again
                lines[j] = "# " + lines[j]
        break


# Re-write the file
with open(filename, 'w') as f:
    f.writelines(lines)
    print('Pipeline succesfully patched!')
