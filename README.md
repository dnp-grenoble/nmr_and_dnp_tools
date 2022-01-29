# nmr_and_dnp_tools
Some small NMR scripts that is useful to develop further programmes.

## dipolar_strength_calc.py
This script takes inputs in the form atomic num and nucleus name like 1H, 13C, etc.
It asks the user for the distance between the two nuclei in Angstrom
and outputs the dipolar strength in Hz and kHz.
Note that the sign is positive for convenience sake.

## larmor_freq_calc.py

This scripts returns you the Larmor frequency in MHz, given a certain magnetic field as input.


## opt_tb_twocomponents.py
This script helps you to calculate at what time you should get the maximum sensitivity
if you have two components in your build up of magnetisation.
It asks for the build up time in seconds, and the component contributions as shown in topspin
You can also input the component contributions such that the sum is 1.
