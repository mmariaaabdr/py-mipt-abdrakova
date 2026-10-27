import os
import matplotlib.pyplot as plt

os.makedirs("out_points", exist_ok=True)

for name in sorted(os.listdir("dead_moroz")):
    with open(os.path.join("dead_moroz", name)) as f:
        n = int(f.readline())
        xs, ys = [], []
        for _ in range(n):
            x, y = map(float, f.readline().split())
            xs.append(x)
            ys.append(y)

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.scatter(xs, ys, s=10 if n > 100 else 40)
    ax.set_aspect("equal")  # одинаковый масштаб по осям 
    ax.set_title(f"{name}: количество точек {n}")
    fig.savefig(os.path.join("out_points", name.replace(".dat", ".png")),
                bbox_inches="tight")
    plt.close(fig)
