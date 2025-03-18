#population sizes
import numpy as np
import matplotlib.pyplot as plt #import graph drawing package

uk_countries = [57.11, 3.13, 1.91, 5.45]
cn_provinces = [65.77, 41.88, 45.28, 61.27, 85.15]
print(uk_countries)
print(cn_provinces)#print two lists of population

countries = 'England','Wales','Northern Ireland','Scotland'
provinces = 'Zhejiang','Fujian','Jiangxi','Anhui','Jiangsu'

plt.pie(uk_countries, labels=countries, autopct='%1.1f%%',shadow=False, startangle=90)
plt.axis('equal')
plt.show()

plt.pie(cn_provinces, labels=provinces, autopct='%1.1f%%',shadow=False, startangle=90)
plt.axis('equal')
plt.show()