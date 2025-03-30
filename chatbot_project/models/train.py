import os
import json
import torch
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    Trainer,
    TrainingArguments,
    DataCollatorForLanguageModeling,
    EarlyStoppingCallback,
)
from datasets import Dataset

# ====== CONFIG ======
MODEL_NAME = "F:/Essentials/Models/DialoGPT-small"
INTENTS_FILE = "data/intents.json"
OUTPUT_DIR = "models/fine_tuned_dialoGPT_intents"
EPOCHS = 2
BATCH_SIZE = 4
USE_FP16 = torch.cuda.is_available()

# ====== Load Intents Dataset ======
def load_intents_as_dataset(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    samples = []
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            for response in intent["responses"]:
                input_text = f"User: {pattern}\nBot:"
                response_text = response
                samples.append({
                    "input_text": input_text,
                    "response_text": response_text
                })
    return Dataset.from_list(samples)

# ====== Tokenizer & Model ======
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.pad_token = tokenizer.eos_token  # ✅ FIX: required for padding
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# ====== Tokenization ======
def tokenize(sample):
    return tokenizer(
        sample["input_text"],
        text_pair=sample["response_text"],
        truncation=True,
        padding="max_length",
        max_length=512
    )

# ====== Dataset Prep ======
dataset = load_intents_as_dataset(INTENTS_FILE)
tokenized_dataset = dataset.map(tokenize, batched=True, remove_columns=dataset.column_names)

# ====== Training Setup ======
# training_args = TrainingArguments(
#     output_dir=OUTPUT_DIR,
#     per_device_train_batch_size=BATCH_SIZE,
#     num_train_epochs=EPOCHS,
#     save_strategy="epoch",
#     logging_dir="logs",
#     logging_steps=100,
#     evaluation_strategy="no",
#     fp16=USE_FP16,
#     push_to_hub=False
# )


training_args = TrainingArguments(
    output_dir="./results",
    overwrite_output_dir=True,
    num_train_epochs=2,  # ✅ Fewer epochs
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,

    logging_dir="./logs",
    logging_steps=400,
    fp16=True,  # ✅ Mixed precision for speed (if GPU supports it)
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    tokenizer=tokenizer,
    data_collator=DataCollatorForLanguageModeling(tokenizer, mlm=False),
)


# ====== Train ======
print("🚀 Starting fine-tuning...")
trainer.train()

# ====== Save Model ======
trainer.save_model(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)

print(f"✅ Fine-tuning complete! Model saved at: {OUTPUT_DIR}")
print("🔄 Reloading model for inference...")
