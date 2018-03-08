import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


R1 = [10, 49.9, 91, 30, 68]
R2 = 100
R3 = [100, 43.2, 56, 68, 33, 240]
fs = 44100
f = 100
T = 0.2
Vin = np.sin(2*np.pi*np.arange(fs*T)*f/fs) #+ np.sin(2*np.pi*np.arange(fs*T)*0.22*f/fs)
A = np.linspace(0, 10, len(Vin))
Vin *= A
Vk = np.empty((len(Vin), 5))
Vs = 6
Vout = np.empty(len(Vin))
outC = np.array([-12.0, -27.777, -21.428, 17.647, 36.363])

for k in range(len(R1)):
    for n in range(len(Vin)):
        if np.abs(Vin[n]) > Vs*R1[k]/R2:
            Vk[n, k] = Vin[n]
        else:
            Vk[n, k] = np.sign(Vin[n])*R1[k]*Vs/R2
        Vk[n, k] = (R2*R3[k]/(R1[k]*R3[k] + R2*R3[k] + R1[k]*R2))*(Vk[n, k] - np.sign(Vk[n, k])*Vs*R1[k]/R2)
    Vout += outC[k]*Vk[:, k]
Vout += 5*Vin

# print(Vout)
plt.plot(Vk)
plt.plot(Vin)
plt.plot(Vout)
plt.show()

N = 175
widths = np.arange(1, N)
cwtmatr = signal.cwt(Vout, signal.ricker, widths)

plt.imshow(cwtmatr, extent=[-1, 1, widths[-1], widths[0]], cmap='bone',
           aspect='auto', vmax=abs(cwtmatr).max(), vmin=-abs(cwtmatr).max())
plt.show()
