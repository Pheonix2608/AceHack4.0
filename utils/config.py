# utils/config.py

import os

# Path to the local DialoGPT model
MODEL_PATH = os.path.join("models", "dialoGPT-small")

# Generation settings (you can tweak this)
GENERATION_CONFIG = {
    "max_length": 1000,
    "pad_token_id": 50256,  # EOS token for DialoGPT
    "do_sample": True,
    "top_k": 50,
    "top_p": 0.95,
}
