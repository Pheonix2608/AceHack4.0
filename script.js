// ===================
// Theme Toggle Button
// ===================
const themeToggle = document.querySelector(".theme-toggle");
const themeSwitch = document.getElementById("theme-switch");

themeSwitch.addEventListener("change", () => {
  document.body.classList.toggle("dark");
});

// =========================
// Hover Bubble on Products
// =========================
const productCards = document.querySelectorAll(".carousel-item, .product-item");

productCards.forEach(item => {
  let timeout;

  item.addEventListener("mouseenter", () => {
    timeout = setTimeout(() => {
      const bubble = item.querySelector(".bubble");
      if (bubble) {
        bubble.textContent = item.getAttribute("data-info") || "Product Info";
        bubble.classList.add("show");
      }
    }, 500); // Shorter delay for better UX
  });

  item.addEventListener("mouseleave", () => {
    clearTimeout(timeout);
    const bubble = item.querySelector(".bubble");
    if (bubble) bubble.classList.remove("show");
  });
});

// ====================
// Chatbot Toggle Logic (future use)
// ====================
const chatbotIcon = document.querySelector('.chatbot-icon');
const chatbotWindow = document.querySelector('.chatbot-window');

if (chatbotIcon && chatbotWindow) {
  chatbotIcon.addEventListener('click', () => {
    chatbotWindow.style.display = chatbotWindow.style.display === 'flex' ? 'none' : 'flex';
  });
}

// ======================
// Chatbot Message System (future use)
// ======================
const chatInput = document.querySelector('.chatbot-input-area input');
const chatSendButton = document.querySelector('.chatbot-input-area button');
const chatMessages = document.querySelector('.chatbot-messages');

function appendMessage(sender, message) {
  const msg = document.createElement('div');
  msg.classList.add('chat-message');
  msg.textContent = `${sender}: ${message}`;
  chatMessages.appendChild(msg);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

function sendMessage() {
  const userMessage = chatInput.value.trim();
  if (!userMessage) return;

  appendMessage("You", userMessage);
  chatInput.value = "";

  setTimeout(() => {
    const response = `Bot: I'm here to help you with "${userMessage}"`;
    appendMessage("Bot", response);
  }, 600);
}

if (chatSendButton && chatInput && chatMessages) {
  chatSendButton.addEventListener("click", sendMessage);
  chatInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
  });
}
function toggleChatbot() {
  const box = document.getElementById("chatbox");
  box.style.display = box.style.display === "flex" ? "none" : "flex";
}

function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();
  if (message === "") return;

  const chatMessages = document.getElementById("chat-messages");

  // User message
  const userMsg = document.createElement("div");
  userMsg.className = "user-msg";
  userMsg.innerText = message;
  chatMessages.appendChild(userMsg);

  // Scroll to bottom
  chatMessages.scrollTop = chatMessages.scrollHeight;

  // Clear input
  input.value = "";

  // Simulate bot reply
  setTimeout(() => {
    const botMsg = document.createElement("div");
    botMsg.className = "bot-msg";
    botMsg.innerText = "I'm still learning! Ask me anything about AceLab.";
    chatMessages.appendChild(botMsg);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }, 1000);
}

function handleKey(event) {
  if (event.key === "Enter") {
    sendMessage();
  }
}
