# NMR and DNP Tools

### Description: Some small NMR scripts which can be used for analysis or to develop other codes.

Welcome to the nmr_and_dnp_tools wiki!
All the scripts can be found in \
[https://github.com/dnp-grenoble/nmr_and_dnp_tools.git](https://github.com/dnp-grenoble/nmr_and_dnp_tools.git)

Description of the Scripts.

## T1 Analysis
> ### Script Name: t1analysis.ipynb & opt_tb_twocomponents.py

The main aim of the script is to analyse the build up of polarisation in the saturation recovery experiment.
The build up can be modelled with a monoexponential in the form:

![Figure](https://latex.codecogs.com/svg.image?I(t)&space;=&space;I_0&space;(1-\exp(-t/T_1))&space;)

Bi-exponential in the form

![Figure](https://latex.codecogs.com/svg.image?I(t)&space;=&space;I_{0,a}&space;(1-\exp(-t/T_{1,a}))&space;&plus;&space;I_{0,b}&space;(1-\exp(-t/T_{1,b}))&space;&space;)

If there is no spin-diffusion the buildup can also be a stretched exponential as described in the paper:
D. Tse, S.R. Hartmann, Nuclear Spin-Lattice Relaxation via Paramagnetic Centers, Phys. Rev. 166 (1968) 279–291. [Link](https://doi.org/10.1103/PhysRev.166.279)

For stretched exponential the build up takes the form:

![Figure](https://latex.codecogs.com/svg.image?I(t)&space;=&space;I_0(1-\exp(-t/T_1)^\beta))

The script reads the file ct1t2.txt from Topspin processed data and then fits the experimental data with the lmfit module.

It gives statistics such as Bayesian Criterion. The lower the value the better the fit will be:
[Bayesian](https://en.wikipedia.org/wiki/Bayesian_information_criterion)

The script then calculates the optimum build-up time for the best sensitivity and reports it.
To calculate the maximum sensitivity it calculates the differential:

![Figure](https://latex.codecogs.com/svg.image?\frac{dI(t)}{dt}) 
and finds the minimum (zero) in the absolute scale


## Dipole Calculator
> ### Script Name: dipolar_strength_calc.py

The script asks the user to input two nuclei.
The input should be in the form: 1H, 13C, etc.

It takes distance between the two nuclei in Angstrom, and calculates the dipolar coupling in Hz and kHz

![Figure](https://latex.codecogs.com/svg.image?|\frac{\mu_0}{4\pi}\frac{\gamma_1\gamma_2h}{r^3}|)


## Biradical weight calculator

The script is to calculate the weight of biradical needed in milligrams to prepare solution for impregnation of samples.

It asks the user for input of biradical. **Please use the short names from the dataframe/csv file.**
e.g. use amu for AMUPol

Then it asks for the concentration, say x mM

It asks for the volume to br prepared in microlitres say y $\mu$l.

It calculates the weight in mg based on the molecular weight (say z g/mol):

Weight of biradical needed in mg = ![Figure](https://latex.codecogs.com/svg.image?\frac{xyz}{1e6})

If you have suggestions for adding other biradicals, please let me know.
