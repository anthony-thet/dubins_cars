import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle

v, w, x, y, theta = 0, 0, 0, 0, 0
delta_t = 0.1
xdata, ydata = [x], [y]


def on_press(event):
    global v, w

    print("pressed:", event.key)

    if event.key == "up":
        v = 18
    if event.key == "down":
        v = -18
    if event.key == "left":
        w = 3*math.pi/2
    if event.key == "right":
        w = -3*math.pi/2


def on_release(event):
    global v, w

    if event.key == "up":
        v = 0.0
    elif event.key in ("left", "right"):
        w = 0.0


fig = plt.figure()
ax  = plt.axes(xlim=(-50,50), ylim=(-50,50))
line, = ax.plot([], [], lw=2)
velocity_line, = ax.plot([], [], lw=2)

car = Rectangle((x, y), 2, 1)
ax.add_patch(car)

def init():
    line.set_data([], [])
    velocity_line.set_data([], [])
    return line, velocity_line, car


def update_state(frame):
    global x, y, theta, v, w

    x1 = x + v * math.cos(theta) * delta_t
    y1 = y + v * math.sin(theta) * delta_t
    theta1 = theta + w * delta_t

    x = x1
    y = y1
    theta = theta1

    xdata.append(x1)
    ydata.append(y1)

    line.set_data(xdata, ydata)

    line_length = 3

    x_end = x + line_length * math.cos(theta)
    y_end = y + line_length * math.sin(theta)

    velocity_line.set_data(
        [x, x_end],
        [y, y_end]
    )

    car.set_xy((x, y))
    car.angle = math.degrees(theta)

    return line, velocity_line, car


anim = (animation.FuncAnimation
    (
    fig,
    update_state,
    init_func=init,
    frames = 500,
    blit=True
))

fig.canvas.mpl_connect("key_press_event", on_press)
fig.canvas.mpl_connect("key_release_event", on_release)

plt.show()
