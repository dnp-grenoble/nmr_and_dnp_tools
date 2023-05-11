import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
from lmfit.models import ExponentialModel
#sns.set_theme(style="darkgrid")

colspecs=[(0, 10),(10, 21), (22, 35), (36, 48), (48, 61)]
df=pd.read_fwf('C:/Bruker/TopSpin3.2/data/Paul/2023-04-Obelix-PAVLOT_Michellin_Silica_D3/7/pdata/1/ct1t2.txt', skiprows=21, nrows = 30, colspecs=colspecs, names=['Points','Tau','Expt','Calc','Difference'])

spinning_freq = 8000.0
tau_r = 1/spinning_freq
steps = 30
p180 = 8e-6
tau_int = 15.0*tau_r-p180/2
final_time = steps*tau_int

xdata = np.linspace(tau_r, final_time, steps)*2
ydata = df['Expt'].to_numpy()
plt.plot(xdata,ydata)

e1=ExponentialModel(prefix='e1_')
pars=e1.guess(ydata,x=xdata)
pars.update(e1.make_params())

pars['e1_amplitude'].set(value=1.0,min=0.0)
pars['e1_decay'].set(value=50e-3)

mod=e1
init=mod.eval(pars, x=xdata)
out=mod.fit(ydata, pars, x=xdata)
comps=out.eval_components(x=xdata)

plt.plot(xdata,ydata,'o',linestyle = 'None')
plt.plot(xdata,out.best_fit)

print(out.fit_report())