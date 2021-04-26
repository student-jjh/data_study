import numpy as np
import numpy_financial as npf
loss=[-750,250]
profit=[100]*18
cashflow=loss+profit

cashflows=np.array(cashflow)

npv=npf.npv(0.045,cashflows)
irr=npf.irr(cashflows)

print(npv)
print(irr)
