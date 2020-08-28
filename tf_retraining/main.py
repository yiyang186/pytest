import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

bit = 4.
n = 0.
p = 2. ** bit - 1
origin_bins = 500
max_step = 20
lr_s = 0.0005
lr_z = 20

def fake_quant(x, s, z):
  return s * (np.clip(np.round(x / s) + z, n, p) - z)


def loss(x, q):
  return np.mean(np.square(q - x) / 2.)


def dlds(x, q, s, z):
  dldq = q - x
  
  t = np.round(x / s) + z
  dqds = np.round(x / s) - x / s
  dqds[t < n] = s * (n - z)
  dqds[t > p] = dqds = s * (p - z)

  return dldq * dqds


def dldz(x, q, s, z):
  dldq = q - x
  
  t = np.round(x / s) + z
  dqdz = np.zeros_like(t)
  dqdz[t < n] = -1.
  dqdz[t > p] = -1.
  
  return dldq * dqdz

def init_quant(x):
  x_min = x.min() + random.random() * 0.5
  x_max = x.max() + random.random() * 0.5
  scale = (x_max - x_min) / (2. ** bit)
  zero_point = np.clip(np.round(-x_min / scale), n, p)
  return scale, zero_point

mu, sigma = 0, 0.1
x = np.random.normal(mu, sigma, 5000)

scale, zero_point = init_quant(x)
q = fake_quant(x, scale, zero_point)

step = 0
# while step < max_step:


xhist, xbin_edges = np.histogram(x, bins=origin_bins)
xwidth = xbin_edges[1] - xbin_edges[0]
plt.bar(xbin_edges[:-1] + xwidth / 2, height=xhist, width=xwidth, color='blue',
    alpha=0.5)

qhist, qbin_edges = np.histogram(q, bins=int(2**bit))
qwidth = qbin_edges[1] - qbin_edges[0]
qhist = qhist / (origin_bins / 2 ** bit)
plt.bar(qbin_edges[:-1] + qwidth / 2, height=qhist, width=qwidth, color='red',
    alpha=0.5)

plt.show()

'''

G = 9.8  # acceleration due to gravity, in m/s^2
L1 = 1.0  # length of pendulum 1 in m
L2 = 1.0  # length of pendulum 2 in m
M1 = 1.0  # mass of pendulum 1 in kg
M2 = 1.0  # mass of pendulum 2 in kg


def derivs(state, t):

    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    delta = state[2] - state[0]
    den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
    dydx[1] = ((M2 * L1 * state[1] * state[1] * sin(delta) * cos(delta)
                + M2 * G * sin(state[2]) * cos(delta)
                + M2 * L2 * state[3] * state[3] * sin(delta)
                - (M1+M2) * G * sin(state[0]))
               / den1)

    dydx[2] = state[3]

    den2 = (L2/L1) * den1
    dydx[3] = ((- M2 * L2 * state[3] * state[3] * sin(delta) * cos(delta)
                + (M1+M2) * G * sin(state[0]) * cos(delta)
                - (M1+M2) * L1 * state[1] * state[1] * sin(delta)
                - (M1+M2) * G * sin(state[2]))
               / den2)

    return dydx

# create a time array from 0..100 sampled at 0.05 second steps
dt = 0.05
t = np.arange(0, 20, dt)

# th1 and th2 are the initial angles (degrees)
# w10 and w20 are the initial angular velocities (degrees per second)
th1 = 120.0
w1 = 0.0
th2 = -10.0
w2 = 0.0

# initial state
state = np.radians([th1, w1, th2, w2])

# integrate your ODE using scipy.integrate.
y = integrate.odeint(derivs, state, t)

x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])

x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text


def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*dt))
    return line, time_text


ani = animation.FuncAnimation(fig, animate, range(1, len(y)),
                              interval=dt*1000, blit=True, init_func=init)
plt.show()
'''
