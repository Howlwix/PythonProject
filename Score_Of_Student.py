import numpy as np
import matplotlib.pyplot as plt


scores = np.random.randint(1,1001,1000)
study_hours = np.random.randint(1,100,1000)
plt.figure(figsize=(15,5))
plt.subplot(1,2,1)

plt.hist(scores, bins=31)

plt.title('Histogram of scores of student')
plt.xlabel('Score')
plt.ylabel('Frequency')


plt.subplot(1,2,2)

plt.scatter(x=scores,y=study_hours,c='blue')

plt.title('relationship between scores and study hours')
plt.xlabel('Score')
plt.ylabel('study hours')
plt.grid(True)
plt.show()