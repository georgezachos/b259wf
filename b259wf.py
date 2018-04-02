import numpy as np
from plotly import tools
import plotly.offline as py
import plotly.graph_objs as go

R1 = np.array([10, 49.9, 91, 30, 68])
R2 = 100
R3 = np.array([100, 43.2, 56, 68, 33, 240])
fs = 44100
f = 400
T = 0.2
tvec = np.arange(fs * T) / fs
N = len(tvec)
Vin = np.sin(2 * np.pi * tvec * f)  # + np.sin(
# 2 * np.pi * np.arange(fs * T) * 0.22 * f / fs)
A = np.linspace(0, 10, N)
A = 10
Vin *= A
Vk = np.empty((N, 5))
Vs = 6
Vout = np.empty(N)
outC = np.array([-12.0, -27.777, -21.428, 17.647, 36.363])

fig = tools.make_subplots(rows=1, cols=1)

L = Vs * R1 / R2
for k in range(len(R1)):
    flg_n1 = 0
    flg = 0
    Vk_n = 0
    Vk_n1 = 0
    Vin_n1 = 0
    for n in range(N):
        if np.abs(Vin[n]) > L[k]:
            Vk_n = Vin[n]
            flg = 0
        else:
            Vk_n = np.sign(Vin[n]) * R1[k] * Vs / R2
            flg = 1
        if flg - flg_n1 != 0:
            m = Vin[n] - Vin_n1
            d = (np.sign(Vin_n1)*L[k] - Vin_n1)/m
            p1 = (-d**3)/6 + (d**2)/2 - d/2 + 1/6
            p0 = (d**3)/6
            Vk_n1 += np.sign(Vin_n1)*abs(m)*p1
            Vk_n += np.sign(Vin_n1)*abs(m)*p0
        Vk[n, k] = Vk_n1
        Vk_n1 = Vk_n
        Vin_n1 = Vin[n]
        flg_n1 = flg
        Vk[n, k] = (R2*R3[k]/(R1[k]*R3[k]+R2*R3[k]+R1[k]*R2))*(Vk[n, k]-np.sign(Vk[n, k])*Vs*R1[k]/R2)*outC[k]
    Vout += Vk[:, k]
    fig.append_trace(go.Scatter(y=Vk[:, k]), 1, 1)

Vout[1:] += 5*Vin[:-1]
# Vout += 5*Vin
# Vout /= 15
trace1 = go.Scatter(y=Vout)
trace2 = go.Scatter(y=Vin)

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 1)

py.plot(fig, filename='simple-subplot.html')


fig2 = tools.make_subplots(rows=1, cols=1)
VoutFFT = np.fft.rfft(Vin)
trace1 = go.Scatter(y=abs(np.real(VoutFFT)))
fig2['layout']['xaxis'].update(title='xaxis 4 title', type='log')
fig2.append_trace(trace1, 1, 1)
py.plot(fig2, filename='simple-subplot2.html')
