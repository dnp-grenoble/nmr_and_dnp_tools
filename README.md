---
description: Some small NMR scripts that is useful to develop further programmes.
---

# NMR and DNP Tools

### dipolar\_strength\_calc.py

This script takes inputs in the form atomic num and nucleus name like 1H, 13C, etc. It asks the user for the distance between the two nuclei in Angstrom and outputs the dipolar strength in Hz and kHz. Note that the sign is positive for convenience sake.

### larmor\_freq\_calc.py

This scripts returns you the Larmor frequency in MHz, given a certain magnetic field as input.

### opt\_tb\_twocomponents.py

This script helps you to calculate at what time you should get the maximum sensitivity if you have two components in your build up of magnetisation. It asks for the build up time in seconds, and the component contributions as shown in topspin You can also input the component contributions such that the sum is 1.

### xyztodipole.py

This script takes an amino acid or an xyz file and creates a list of dipolar couplings between the spins with euler angles between the tensors. The euler angles are not important as most of the time we do powder averaging.
