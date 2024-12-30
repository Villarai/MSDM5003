from mino import BasicAgent, BasicMinorityGame
from tqdm import trange
import matplotlib.pyplot as plt

N=1001
M=2

g = BasicMinorityGame(num_agent=N, mem=M)

A1 = []
for i in trange(5000):
    utility, behavior = g.forward()
    A1.append(utility)

for a in g.agent_list:
    print(a)


plt.figure(figsize=(10,6), dpi=300)
plt.plot(A1, label='$A_1(t)$')


plt.title(f"Basic Minority Game (N={N}, M={M})")
plt.legend()
plt.show()
