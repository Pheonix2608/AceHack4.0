import tkinter as tk
from tkinter import scrolledtext
from models.generate_response import generate_reply
from models.load_mode import load_dialo_model

class ChatBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DialoGPT Chatbot")

        self.chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', width=60, height=25, font=("Helvetica", 12))
        self.chat_log.pack(padx=10, pady=10)

        self.entry = tk.Entry(root, font=("Helvetica", 14))
        self.entry.pack(padx=10, pady=(0, 10), fill=tk.X)
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(root, text="Send", command=self.send_message, font=("Helvetica", 12))
        self.send_button.pack(pady=(0, 10))

        self.tokenizer, self.model, self.device = load_dialo_model()
        self.chat_history = None

    def send_message(self, event=None):
        user_input = self.entry.get().strip()
        if not user_input:
            return

        self.update_chat_log(f"You: {user_input}")
        self.entry.delete(0, tk.END)

        response, self.chat_history = generate_reply(user_input, self.chat_history)
        self.update_chat_log(f"Bot: {response}")

    def update_chat_log(self, message):
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, message + "\n")
        self.chat_log.config(state='disabled')
        self.chat_log.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotGUI(root)
    root.mainloop()
