import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update_line(num, data, line):
	line.set_data(data[..., :num])
	time_text.set_text("Points: %.0f" % int(num))
	return line


V_d = np.linspace(-309, 0, 50)
f = [((1.68e+36) * (0.6 - i))**(1/4) for i in V_d]
data = np.array([V_d, f])

fig = plt.figure()
ax = fig.add_subplot(111)
l, = ax.plot([], [], 'r-')


ax.set_xlabel("Applied Voltage")
ax.set_ylabel("frequency")
ax.set_xlim(-350, 10)
ax.set_ylim(0, 5e9, 0.5e9)
plt.title("Plot of frequency against Voltage")
time_text = ax.text(0.7, 0.95, "", transform = ax.transAxes, fontsize = 10, color = 'green')


line_ani = animation.FuncAnimation(fig, update_line, frames = 50, fargs = (data, l))
plt.show()