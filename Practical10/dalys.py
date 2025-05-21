#import some libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/Users/wangermi/Desktop/note/IBI1 8011/IBI1_2024-25/Practical10")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print(dalys_data.head(5))

# check the woking directory
print(os.getcwd())
print(os.listdir())

# read the data
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# look up the first 5 rows
print(dalys_data.head(5))

# check the infor of data frame
dalys_data.info()
print(dalys_data.describe())

# show specific data
print(dalys_data.iloc[9, 2])

# Afghanistan
afghanistan_dalys = dalys_data.loc[dalys_data.Entity == "Afghanistan", "Year"]
print("Afghanistan 1990 is " + str(afghanistan_dalys.iloc[9]))
#should be 1999

# use boolean value
is_1990 = dalys_data.Year == 1990
dalys_1990 = dalys_data.loc[is_1990, "DALYs"]
print(dalys_1990)

# compare UK and france  sDALYs
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", "DALYs"]
france = dalys_data.loc[dalys_data.Entity == "France", "DALYs"]
uk_mean = uk.mean()
france_mean = france.mean()
print(f"the average DALYs of United Kindom: {uk_mean}")
print(f"the average DALYs of France: {france_mean}")
if uk_mean > france_mean:
    print("the average of UK is higgher than france")
else:
    print("the average of UK is lower than france")

# draw the picture of UK
uk_data = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["Year", "DALYs"]]
plt.plot(uk_data.Year, uk_data.DALYs, 'b+')
plt.xticks(uk_data.Year, rotation=-90)
plt.xlabel('years')
plt.ylabel('DALYs')
plt.title('the change of DALYs of the United Kingdom ')
plt.savefig("uk_dalys_plot.png")
plt.show()

# How has the DALYs changed in China and the UK over time?
china_uk_data = dalys_data.loc[dalys_data.Entity.isin(["China", "United Kingdom"]), ["Year", "Entity", "DALYs"]]
china_data = china_uk_data.loc[china_uk_data.Entity == "China", ["Year", "DALYs"]]
uk_data = china_uk_data.loc[china_uk_data.Entity == "United Kingdom", ["Year", "DALYs"]]
plt.plot(china_data.Year, china_data.DALYs, label='China')
plt.plot(uk_data.Year, uk_data.DALYs, label='United Kingdom')
plt.xticks(china_data.Year, rotation=-90)
plt.xlabel('Years')
plt.ylabel('DALYs')
plt.title('the change of DALYs of china and UK')
plt.legend()
plt.savefig("china_uk_dalys_plot.png")
plt.show()