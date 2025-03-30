# utils/text_utils.py

import re

def clean_text(text):
    """Clean up bot responses if needed."""
    text = re.sub(r"\s+", " ", text).strip()
    return text.capitalize()

def truncate_conversation(conversation, max_turns=10):
    """Limit context size for long chats (if needed)."""
    return conversation[-max_turns:] if len(conversation) > max_turns else conversation
