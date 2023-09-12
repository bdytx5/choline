import torch
import torch.nn as nn
import pickle



# sometimes simplicity trumps all else 



input_data = torch.randn(1, 10)

# Define a simple model
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 5)

    def forward(self, x):
        return self.fc(x)

# Create an instance of the model
model = SimpleModel()

output = model(input_data)
print(output)


# Save the model using pickle
with open('simple_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Load the saved model using pickle
with open('simple_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Set the loaded model to evaluation mode
loaded_model.eval()

# Test the loaded model with dummy input
output = loaded_model(input_data)
print(output)



import os

file_path = 'simple_model.pkl'
file_size = os.path.getsize(file_path)

print(f"The size of the pickle file '{file_path}' is {file_size} bytes.")
