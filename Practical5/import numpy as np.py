import numpy as np
import matplotlib.pyplot as plt #import graph drawing package

languages = {'Javascript':62.3, 'HTML':52.9, 'Python':51, 'SQL':52, 'TypeScript':38.5}
print(languages) #print the whole dictionary

N = 5
users = (62.3, 52.9, 51, 52, 38.5)
ind = np.arange(N)
width = 0.35
p1 = plt.bar(ind, users, width,)
plt.ylabel("users percentage")
plt.title("the percentage of developers who use the top 5 programming languages")
plt.xticks(ind,('Javascript', 'HTML', 'Python', 'SQL', 'Typescript'))
plt.yticks(np.arange(0,70,5))
plt.show()