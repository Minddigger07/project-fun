

import matplotlib.pyplot as plt
from scipy.stats import norm,uniform
x=np.arange(0,10,0.1)
pdf=norm.pdf(x,loc=5,scale=1)
plt.figure()
plt.title("Normal Distribution")
plt.xlabel("Data Points")
plt.ylabel("Probability Distribution")
plt.plot(x,pdf)
plt.figure()
pdf=uniform.pdf(x,loc=5,scale=1)
plt.title("Uniform Distribution")
plt.xlabel("Data Points")
plt.ylabel("Probability Distribution")
plt.plot(x,pdf)
plt.show()

