import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8, 5), subplot_kw=dict(aspect="equal"))

recipe = ["371 Larrea_tridentata",
          "760 Ambrosia_dumosa",
          "2086 Prosopis_juliflora",
          "579 Olneya",
          "991 Hilaria_rigida"]

data = [float(x.split()[0]) for x in recipe]
ingredients = [x.split()[-1] for x in recipe]

colors = ['#e74645', '#fb7756', '#facd60', '#fdfa66', '#1ac0c6']

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} )"


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"), colors=colors,
                                  wedgeprops=dict(linewidth=2, edgecolor='w'))

ax.legend(wedges, ingredients,
          title="Species",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("The Initial Proportion of each Species in the Community")

plt.show()
