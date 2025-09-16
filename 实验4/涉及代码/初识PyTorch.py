import torch
x = torch.rand(5, 3)
print(x)

x = torch.zeros(5, 3, dtype=torch.long)
print(x)

x = torch.tensor([5.5, 3])
print(x)

print(x.size())

x = torch.randn(1)
print(x)
print(x.item())