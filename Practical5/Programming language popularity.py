import numpy as np
import matplotlib.pyplot as plt #import graph drawing package

languages = {'Javascript':62.3, 'HTML':52.9, 'Python':51, 'SQL':52, 'TypeScript':38.5}
print(languages) #print the whole dictionary

language_names = list(languages.keys())
popularity = list(languages.values())

# make a bar graph
plt.figure(figsize=(10, 6))  # set the size of this figure
bars = plt.bar(language_names, popularity, color='skyblue')
    
# set the title and label of this plot
plt.title('the popularity of programme language')
plt.xlabel('programming languages')
plt.ylabel('Users (percentage)')
plt.ylim(0, 100)  # set the range of Y axis
    
#show detailed data in each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 1, f'{height}%', ha='center', va='bottom')
    
plt.tight_layout() 
plt.show()