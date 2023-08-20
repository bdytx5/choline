import torch
import torch.nn as nn

##### tasks 
#### should be able to send copy of model to the backend at any frequency desired 
#### 





class MyCustomFunction:
    @staticmethod
    def backward_hook(*args):
        print("Backward hook called!")

class CholineModel(nn.Module):
    def __init__(self, module):
        super(CholineModel, self).__init__()
        self.module = module
        self.module.register_backward_hook(MyCustomFunction.backward_hook)

    def forward(self, *input):
        return self.module(*input)





# Example usage with a simple linear layer
original_module = nn.Linear(10, 5)
wrapped_module = CholineModel(original_module)

x = torch.rand(1, 10)
y = wrapped_module(x)
loss = y.sum()
loss.backward()  # This will print "Backward hook called!" during the backward pass