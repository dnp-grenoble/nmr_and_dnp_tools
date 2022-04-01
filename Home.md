Welcome to the nmr_and_dnp_tools wiki!

Description of the Scripts.

## T1 Analysis

The main aim of the script is to analyse the build up of polarisation in the saturation recovery experiment.
The build up can be modelled with a monoexponential in the form:

<img src="https://render.githubusercontent.com/render/math?math=e^{i \pi} = -1">

or a biexponential in the form

![f2]

[f2]: https://chart.apis.google.com/chart?cht=tx&chl=I(t)=I_{0,a}(1-\exp(-t/T_{1,a}))+I_{0,b}(1-\exp(-t/T_{1,b}))
