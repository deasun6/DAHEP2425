import matplotlib.pyplot as plt
import numpy as np
import uproot

def theoretical_pdf(t, tau):
    return (1/tau)*np.exp(-t/tau)
    

xdata = np.linspace(0.1, 8, 100)
ydata = []
i=0

while i<len(xdata):
    ydata.append(theoretical_pdf(1, xdata[i]))
    i+=1

plt.plot(xdata, ydata, label="t=1")
plt.xlabel("\tau")
plt.ylabel("theor. pdf")
plt.title("PDF funkcije")
plt.legend()
plt.savefig('theor_pdft.png')