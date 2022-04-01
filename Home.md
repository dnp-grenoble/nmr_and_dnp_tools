Welcome to the nmr_and_dnp_tools wiki!

Description of the Scripts.

## T1 Analysis

The main aim of the script is to analyse the build up of polarisation in the saturation recovery experiment.
The build up can be modelled with a monoexponential in the form:

![Figure](https://latex.codecogs.com/svg.image?I(t)&space;=&space;I_0&space;(1-\exp(-t/T_1))&space;)

Bi-exponential in the form

![Figure](https://latex.codecogs.com/svg.image?I(t)&space;=&space;I_{0,a}&space;(1-\exp(-t/T_{1,a}))&space;&plus;&space;I_{0,b}&space;(1-\exp(-t/T_{1,b}))&space;&space;)

If there is no spin-diffusion the buildup can also be a stretched exponential as described in the paper:
D. Tse, S.R. Hartmann, Nuclear Spin-Lattice Relaxation via Paramagnetic Centers, Phys. Rev. 166 (1968) 279–291. [Link](https://doi.org/10.1103/PhysRev.166.279.)

For stretched exponential the build up takes the form:

![Figure](https://latex.codecogs.com/svg.image?I(t)&space;=&space;I_0(1-\exp(-t/T_1)^\beta))

The script reads the file ct1t2.txt from Topspin processed data and then fits the experimental data with the lmfit module.

It gives statistics such as Bayesian Criterion. The lower the value the better the fit will be:
[Bayesian](https://en.wikipedia.org/wiki/Bayesian_information_criterion)

The script then calculates the optimum build-up time for the best sensitivity and reports it.
To calculate the maximum sensitivity it calculates the differential:

![Figure](https://latex.codecogs.com/svg.image?\frac{dI(t)}{dt}) 
and finds the minimum (zero) in the absolute scale




The python file for the analysis is:
https://github.com/dnp-grenoble/nmr_and_dnp_tools/blob/3f4e44ff697b1f476bdad88bdd76a4ca2d7627d9/t1analysis.py
