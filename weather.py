import numpy as np
import matplotlib.pyplot as plt
dates=["JUL6","JUL7","JUL8","JUL9","JUL10","JUL11","JUL12","JUL13","JUL14","JUL5"]
temperature=[28,28,28,29,29,29,29,27,28,27]
wind=[23,25,23,18,19,18,21,22,23,21]
ypos=np.arange(len(dates))
plt.bar(ypos-0.2,temperature,color='r',width=.4,label="Temperature(in Celsius)")
plt.bar(ypos+0.2,wind,color='b',width=.4,label="Wind(in km/hr)")
plt.xticks(ypos,dates)
plt.xlabel("Dates---------->")
plt.ylabel("Temperture and Wind---------->")
plt.title("Temperture and Wind For Next 10 Days")
plt.legend()