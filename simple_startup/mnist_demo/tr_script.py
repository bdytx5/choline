import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import os


#### opening local file 
###### when synced, the file will go to /root/mnist_demo_external_file.txt 
##### path will change on remote 

###### eg we will need to replace the "/Users/brettyoung/Desktop/dev/choline/simple_startup/" with "/root/"


####### could just go through all files 
############ check if a path is in external upload paths list  
######### if outside, replace base (/Users/brettyoung/Desktop/dev/choline/simple_startup/) path with /root/ 

# yaml contains 
# upload_locations:
# - /Users/brettyoung/Desktop/dev/choline/simple_startup/mnist_demo
# - /Users/brettyoung/Desktop/dev/choline/simple_startup/mnist_demo_external_file.txt
# - /Users/brettyoung/Desktop/dev/choline/simple_startup/mnist_demo_external_data_folder/1
# - /Users/brettyoung/Desktop/dev/choline/simple_startup/mnist_demo_external_data_folder/



import os


# temporary solution until i connect the right neurons 
def cholinePath(local_path, remote_path):
    is_remote = os.environ.get('cholineremote')
    if is_remote:
        return remote_path
    else:
        return local_path


with open(cholinePath('/Users/brettyoung/Desktop/dev/choline/simple_startup/mnist_demo_external_file.txt', 'root/mnist_demo_external_file.txt'), 'r') as f:
    content = f.read()
    print(content)

#### several cases 

######## individual files that match those listed in the yaml --> just replace base path with /root/ 

###### folders that match one listed in yaml ---> just replace all with root 



# above would be 

# with open('root/mnist_demo_external_file.txt', 'r') as f:
#     content = f.read()
#     print(content)



# above would be 
##### 

# directory_path = "root/mnist_demo_external_data_folder/"


## ......




# Dataset
transform = transforms.Compose([transforms.ToTensor()])
train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)
test_dataset = datasets.MNIST(root='./data', train=False, transform=transform)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

# Model
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(28*28, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = x.view(-1, 28*28)
        x = self.fc1(x)
        x = nn.functional.relu(x)
        x = self.fc2(x)
        return nn.functional.log_softmax(x, dim=1)

model = SimpleNN()

# Loss and Optimizer
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

# Training Loop
epochs = 5
for epoch in range(epochs):
    for i, (images, labels) in enumerate(train_loader):
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        if (i+1) % 100 == 0:
            print(f'Epoch [{epoch+1}/{epochs}], Step [{i+1}], Loss: {loss.item():.4f}')

print('Training complete.')