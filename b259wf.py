import numpy as np
from plotly import tools
import plotly.offline as py
import plotly.graph_objs as go

R1 = [10, 49.9, 91, 30, 68]
R2 = 100
R3 = [100, 43.2, 56, 68, 33, 240]
fs = 44100
f = 2000
T = 0.2
tvec = np.arange(fs*T)/fs
N = len(tvec)
Vin = np.sin(2*np.pi*tvec*f) + np.sin(2*np.pi*np.arange(fs*T)*0.22*f/fs)
A = np.linspace(0, 10, N)
Vin *= A
Vk = np.empty((N, 5))
Vs = 6
Vout = np.empty(N)
outC = np.array([-12.0, -27.777, -21.428, 17.647, 36.363])

fig = tools.make_subplots(rows=1, cols=1)

for k in range(len(R1)):
    for n in range(N):
        if np.abs(Vin[n]) > Vs*R1[k]/R2:
            Vk[n, k] = Vin[n]
        else:
            Vk[n, k] = np.sign(Vin[n])*R1[k]*Vs/R2
        Vk[n, k] = (R2*R3[k]/(R1[k]*R3[k] + R2*R3[k] + R1[k]*R2))*(Vk[n, k] - np.sign(Vk[n, k])*Vs*R1[k]/R2)
    Vout += outC[k]*Vk[:, k]
    fig.append_trace(go.Scatter(y=Vk[:, k]), 1, 1)

Vout += 5*Vin


trace1 = go.Scatter(
    y=Vout
)
trace2 = go.Scatter(
    y=Vin
)

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 1)
# fig.append_trace(trace3, 1, 1)

# fig['layout'].update(height=600, width=600, title='i <3 subplots')
py.plot(fig, filename='simple-subplot')
# # print(Vout)
# plt.plot(Vk)
# plt.plot(Vin)
# plt.plot(Vout)
# plt.show()
