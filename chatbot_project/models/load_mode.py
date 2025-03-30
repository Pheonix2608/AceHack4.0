from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# def load_dialo_model(model_path=r"F:\Essentials\Models\dialoGPT-small"):
def load_dialo_model(model_path=r"F:/Projects/NLP/chatbot_project/models/fine_tuned_dialoGPT_intents"):
    """
    Load the DialoGPT model and tokenizer from the specified path.
    If the model is not found, it will raise an error.
    """
    # Load the tokenizer
    # Check if the model path exists and is valid
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
    except Exception as e:
        print(f"Error loading tokenizer: {e}")
        raise FileNotFoundError(f"Tokenizer not found at {model_path}. Please check the path.")
    
    # Load the model
    model = AutoModelForCausalLM.from_pretrained(model_path, local_files_only=True, torch_dtype=torch.float32)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    return tokenizer, model, device
