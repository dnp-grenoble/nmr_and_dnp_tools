Welcome to the nmr_and_dnp_tools wiki!

Description of the Scripts.

## T1 Analysis

The main aim of the script is to analyse the build up of polarisation in the saturation recovery experiment.
The build up can be modelled with a monoexponential in the form:

![f1]

[f1]: https://chart.apis.google.com/chart?cht=tx&chl=I(t)=I_0(1-\exp(-t/T_1))

or a biexponential in the form

![f2]
[f2]: https://chart.apis.google.com/chart?cht=tx&chl=I(t)=I_{0,a}(1-\exp(-t/T_{1,a})+I_{0,b}(1-\exp(-t/T_{1,b}))
