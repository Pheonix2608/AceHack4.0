import torch
from models.model import NeuralNet

def load_trained_model(path="saved_models/model.pth"):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    data = torch.load(path, map_location=device)

    model = NeuralNet(data["input_size"], data["hidden_size"], data["output_size"]).to(device)
    model.load_state_dict(data["model_state"])
    model.eval()

    return model, data["all_words"], data["tags"]
