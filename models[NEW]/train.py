import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from model import NeuralNet
from data.preprocessing import load_data
import json
import os

class ChatDataset(Dataset):
    def __init__(self, X_data, y_data):
        self.n_samples = len(X_data)
        self.x_data = X_data
        self.y_data = y_data

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_samples

def train_model():
    # Load training data
    X_train, y_train, all_words, tags = load_data()

    # Hyperparameters
    batch_size = 8
    input_size = X_train.shape[1]
    hidden_size = 64
    output_size = len(tags)
    learning_rate = 0.001
    num_epochs = 1000

    # Device setup
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    dataset = ChatDataset(X_train, y_train)
    train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True)

    model = NeuralNet(input_size, hidden_size, output_size).to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(num_epochs):
        for (words, labels) in train_loader:
            words = words.to(device)
            labels = labels.to(dtype=torch.long).to(device)

            outputs = model(words)
            loss = criterion(outputs, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        if (epoch + 1) % 100 == 0:
            print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

    print(f'Final loss: {loss.item():.4f}')

    # Save model
    model_data = {
        "model_state": model.state_dict(),
        "input_size": input_size,
        "hidden_size": hidden_size,
        "output_size": output_size,
        "all_words": all_words,
        "tags": tags
    }

    os.makedirs("saved_models", exist_ok=True)
    torch.save(model_data, "saved_models/model.pth")
    print("Model saved to saved_models/model.pth")

if __name__ == '__main__':
    train_model()
