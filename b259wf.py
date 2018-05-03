import numpy as np
from plotly import tools
import plotly.offline as py
import plotly.graph_objs as go


R1 = np.array([10, 49.9, 91, 30, 68])
R2 = 100
R3 = np.array([100, 43.2, 56, 68, 33, 240])
fs = 44100
f = 5000
T = 0.1
tvec = np.arange(fs * T) / fs
N = len(tvec)
Vin = np.sin(2 * np.pi * tvec * f)  # + np.sin(
# 2 * np.pi * np.arange(fs * T) * 0.22 * f / fs)
A = np.linspace(0, 10.0, N)
# A = 10
Vin *= A
Vk = np.empty((N, 5))
Vn1 = np.empty((N))
d = np.zeros((N, 5))
p1 = np.zeros((N, 5))
p0 = np.zeros((N, 5))
s = np.zeros((N, 5))
Vs = 6
Vout = np.empty(N)
outC = np.array([-12.0, -27.777, -21.428, 17.647, 36.363])
Vsigns = [-1, -1, -1, 1, 1]
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
            Vk_n = np.sign(Vin[n]) * L[k]
            flg = 1
        Vn1[n] = Vin_n1
        m = Vin[n] - Vin_n1
        if flg - flg_n1 != 0:
            # d = (np.sign(Vin_n1)*L[k] - Vin_n1)/m
            d[n, k] = (np.sign(Vin[n])*L[k] - Vin[n] + m)/m
            p1[n, k] = (-d[n, k]**3)/6 + (d[n, k]**2)/2 - d[n, k]/2 + 1/6
            d[n, k] = (np.sign(Vin_n1)*L[k] - Vin_n1)/m
            p0[n, k] = (d[n, k]**3)/6
            Vk_n1 += np.sign(Vin[n])*abs(m)*p1[n, k]
            Vk_n += np.sign(Vin_n1)*abs(m)*p0[n, k]
        s[n, k] = m
        Vk[n, k] = Vk_n1
        Vk_n1 = Vk_n
        Vin_n1 = Vin[n]
        flg_n1 = flg

        Vk[n, k] = (R2*R3[k]/(R1[k]*R3[k]+R2*R3[k]+R1[k]*R2))\
            * (Vk[n, k]-np.sign(Vk[n, k])*Vs*R1[k]/R2)*outC[k]
    Vout += Vk[:, k]
    fig.append_trace(go.Scatter(y=Vk[:, k], name='b '+str(k), legendgroup='branches'), 1, 1)
k = 0
fig.append_trace(go.Scatter(y=d[:, k], name='d'+str(k), legendgroup='debug'), 1, 1)
fig.append_trace(go.Scatter(y=p1[:, k], name='p1'+str(k), legendgroup='debug'), 1, 1)
fig.append_trace(go.Scatter(y=p0[:, k], name='p0'+str(k), legendgroup='debug'), 1, 1)
fig.append_trace(go.Scatter(y=s[:, k], name='s'+str(k), legendgroup='debug'), 1, 1)

Vout = np.nan_to_num(Vout)
Vout[1:] += 5*Vin[:-1]

fig.append_trace(go.Scatter(y=Vout[:], name='final'), 1, 1)
fig.append_trace(go.Scatter(y=Vn1, name='in1'), 1, 1)
fig.append_trace(go.Scatter(y=Vin, name='in'), 1, 1)

for _, l in enumerate(L):
    fig.append_trace(go.Scatter(x=[0, len(Vout)], y=[l, l], marker=dict(color='black'), name='L '+str(k), legendgroup='threshold'), 1, 1)
    fig.append_trace(go.Scatter(x=[0, len(Vout)], y=[-l, -l], marker=dict(color='black'), name='-L '+str(k), legendgroup='threshold'), 1, 1)
# fig.append_trace(trace1, 1, 1)
# fig.append_trace(trace2, 1, 1)

py.plot(fig, filename='simple-subplot.html')


# fig2 = tools.make_subplots(rows=1, cols=1)
# VoutFFT = np.fft.rfft(Vout*np.hanning(N))

# trace1 = go.Scatter(
    # y=20*np.log10(np.abs(VoutFFT)/max(np.abs(VoutFFT))),
    # x=np.fft.rfftfreq(len(Vout), 1/fs))

# fig2['layout']['xaxis'].update(title='title', type='lin')
# fig2.append_trace(trace1, 1, 1)
# py.plot(fig2, filename='simple-subplot2.html')
