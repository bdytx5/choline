import os
import pickle
import base64
import asyncio
import aiohttp
import requests
import torch
import torch.optim as optim
import torch.nn as nn
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from utils import upload_object, download_object  # Import specific functions
# Define your SimpleNet model
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = torch.flatten(x, 1)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Training Loop
def train(model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = nn.functional.cross_entropy(output, target)
        loss.backward()
        optimizer.step()

        if batch_idx % 10 == 0:
            print(f'Train Epoch: {epoch} [{batch_idx * len(data)}/{len(train_loader.dataset)} ({100. * batch_idx / len(train_loader):.0f}%)]\tLoss: {loss.item():.6f}')

# MNIST Training Demo
def mnist_demo():
    run_name = "mnist_demo_run"

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    train_loader = DataLoader(datasets.MNIST('../data', train=True, download=True, transform=transforms.Compose([transforms.ToTensor()])), batch_size=32, shuffle=True)
    
    model = SimpleNet().to(device)
    model = download_object(run_name, "model3.pkl", model) # use choline ML DB to sync object 

    optimizer = optim.SGD(model.parameters(), lr=0.01)

    # Train the model for one epoch
    train(model, device, train_loader, optimizer, 1)

    # Upload the model and optimizer
    model_upload_response =  upload_object(run_name, "model2.pkl", model, nonblocking=True)
    optimizer_upload_response =  upload_object(run_name, "optimizer2.pkl", optimizer)

    print("Upload Response for Model:", model_upload_response)
    print("Upload Response for Optimizer:", optimizer_upload_response)


if __name__ == "__main__":
    mnist_demo()

