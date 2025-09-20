import numpy as np
import matplotlib.pyplot as plt

final_steps=[]
for x in range(100):
    path = [0]  
    step=0
    for i in range (100):
        dice = np.random.randint(1, 7)
        if dice <3:
            step = max(0,step-1)
        elif dice <6:
            step+=1
        else:
            step += np.random.randint(1, 7)
        if np.random.rand() <= 0.001:
            step = 0
        path.append(step)
    final_steps.append(path)
np_final_steps = np.array(final_steps)
winninng_steps = np_final_steps[np_final_steps[:,-1]>=60].shape[0]
print(f'The winning percentage is: {winninng_steps}%')
plt.plot(np.transpose(np_final_steps))
plt.show()

