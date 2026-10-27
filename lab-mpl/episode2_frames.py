import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.ticker import MultipleLocator

os.makedirs("out_frames", exist_ok=True)

with open("frames.dat") as f:
    lines = [list(map(float, line.split())) for line in f if line.strip()]
frames = [(lines[i], lines[i + 1]) for i in range(0, len(lines), 2)]
n = len(frames)

# общие пределы для всех кадров
xmin = min(min(x) for x, y in frames)
xmax = max(max(x) for x, y in frames)
ymin = min(min(y) for x, y in frames) - 1
ymax = max(max(y) for x, y in frames) + 1


def draw(ax, i):
    ax.cla()
    ax.plot(*frames[i])
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_title(f"Кадр {i + 1} из {n}")
    # основная сетка через 2, бледная дополнительная через 1
    for axis in (ax.xaxis, ax.yaxis):
        axis.set_major_locator(MultipleLocator(2))
        axis.set_minor_locator(MultipleLocator(1))
    ax.grid(which="major", color="0.75")
    ax.grid(which="minor", color="0.92")


# отдельные кадры
for i in range(n):
    fig, ax = plt.subplots(figsize=(6, 4.5))
    draw(ax, i)
    fig.savefig(f"out_frames/frame_{i:03d}.png", bbox_inches="tight")
    plt.close(fig)

# все кадры на одной картинке
fig, axes = plt.subplots((n + 2) // 3, 3, figsize=(13, 3.3 * ((n + 2) // 3)))
for i, ax in enumerate(axes.flat):
    if i < n:
        draw(ax, i)
    else:
        ax.set_visible(False)
fig.tight_layout()
fig.savefig("out_frames/all_frames.png")
plt.close(fig)

# гифка
fig, ax = plt.subplots(figsize=(6, 4.5))
anim = FuncAnimation(fig, lambda i: draw(ax, i), frames=n)
anim.save("out_frames/process.gif", writer=PillowWriter(fps=3))
plt.close(fig)
