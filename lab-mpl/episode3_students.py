import os
import csv
import matplotlib.pyplot as plt

os.makedirs("out_students", exist_ok=True)

with open("students.csv") as f:
    rows = [(prep, group, int(mark)) for prep, group, mark in csv.reader(f, delimiter=";")]

marks = sorted({mark for _, _, mark in rows})
# оценки упорядочены, поэтому цвета от красного (плохо) к зелёному (хорошо)
colors = plt.cm.RdYlGn([i / (len(marks) - 1) for i in range(len(marks))])

fig, axes = plt.subplots(2, 1, figsize=(9, 8))

for ax, col, title in [(axes[0], 0, "Оценки по преподавателям"),
                       (axes[1], 1, "Оценки по группам")]:
    keys = sorted({r[col] for r in rows})
    bottom = [0] * len(keys)
    for mark, color in zip(marks, colors):
        counts = [sum(1 for r in rows if r[col] == k and r[2] == mark) for k in keys]
        ax.bar(keys, counts, bottom=bottom, color=color, label=mark)
        bottom = [b + c for b, c in zip(bottom, counts)]
    ax.set_title(title)
    ax.set_ylabel("Число студентов")
    ax.legend(title="Оценка", reverse=True, loc="center left", bbox_to_anchor=(1, 0.5))

fig.tight_layout()
fig.savefig("out_students/marks.png")
