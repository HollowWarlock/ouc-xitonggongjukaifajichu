import torch
a = torch.ones(5)
print(a)

b = a.numpy()
print(b)

a.add_(1)
print(a)
print(b)

import numpy as np
a = np.ones(5)
b = torch.from_numpy(a)
print(a)
print(b)

np.add(a, 1, out=a)
print(a)
print(b)