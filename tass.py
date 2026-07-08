import random 
import pickle
data = []
for i in range(10) : 
    plus= (random.randint(1,6)+(random.randint(1,6)))
    tass = (random.randint(1,6),random.randint(1,6))
    data.append(plus)
    data.append(tass)
    
print(data,tass)