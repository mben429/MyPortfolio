from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
import re
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.style as style


rank_years_range = [i for i in range(2004, 2020)]

usa = [15, 16, 14, 14, 19, 19, 16, 16, 17, 16, 18, 16, 16, 17, 17, 13]
france = [4, 5, 3, 2, 6, 7, 5, 6, 3, 4, 5, 7, 7, 8, 9, 7]
diff_list = []

for i in range(len(usa)):
    diff_list.append(usa[i] - france[i])

fig, ax = plt.subplots()

ax.plot(rank_years_range, usa, label="USA", color="red")
ax.plot(rank_years_range, france, label="FRANCE", color="blue")
ax.plot(rank_years_range, diff_list, label="Difference in rank", color="purple")
ax.legend()
plt.title("IRB World ranking comparison - France vs USA")
plt.xlabel("Year")
plt.ylabel("IRB World Rank")
plt.gca().invert_yaxis()
plt.show()







