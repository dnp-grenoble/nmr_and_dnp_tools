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

### temp\_calc\_KBr.py

This script is to calculate the temperature of the sample when the t1 for 79Br is provided from KBr measurements.$$\frac{1}{T_1} = 0.0145 + 5330T^{-2 }+1.42*10^7T^{-4}+2.48*10^9T^{-6}$$

### t1analysis.py

The script takes a $$T_1$$analysis file from topspin replaxation measurements and then fits it with the one component, two components, or stretched exponential. It also calculates the optimum d1 for the best sensitivity. $$(S/N)/\sqrt{T_b}$$
