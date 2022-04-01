Welcome to the nmr_and_dnp_tools wiki!

Description of the Scripts.

## T1 Analysis

The main aim of the script is to analyse the build up of polarisation in the saturation recovery experiment.
The build up can be modelled with a monoexponential in the form:

![Figure](https://latex.codecogs.com/svg.image?I(t)&space;=&space;I_0&space;(1-\exp(-t/T_1))&space;)

or a biexponential in the form

![Figure](https://latex.codecogs.com/svg.image?I(t)&space;=&space;I_{0,a}&space;(1-\exp(-t/T_{1,a}))&space;&plus;&space;I_{0,b}&space;(1-\exp(-t/T_{1,b}))&space;&space;)