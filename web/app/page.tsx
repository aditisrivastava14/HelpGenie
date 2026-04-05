"use client";
import { useState, useRef, useEffect } from "react";
import "./globals.css";

type Message = {
  id: number;
  text: string;
  sender: "user" | "bot";
};

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([
    { id: 1, text: "Hi there! I'm HelpGenie ✨ How can I assist you today?", sender: "bot" }
  ]);
  const [input, setInput] = useState("");
  const [isTyping, setIsTyping] = useState(false);
  const chatEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isTyping]);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userText = input.trim();
    setInput("");
    
    // Add user message
    setMessages(prev => [...prev, { id: Date.now(), text: userText, sender: "user" }]);
    setIsTyping(true);

    try {
      const response = await fetch("http://localhost:8000/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userText }),
      });
      const data = await response.json();
      
      // Simulate slight delay for natural feeling
      setTimeout(() => {
        setIsTyping(false);
        setMessages(prev => [...prev, { id: Date.now(), text: data.response, sender: "bot" }]);
      }, 600);

    } catch (error) {
      console.error(error);
      setIsTyping(false);
      setMessages(prev => [...prev, { id: Date.now(), text: "Oops! My magic wand is broken. Cannot reach the server! 😥", sender: "bot" }]);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter") handleSend();
  };

  return (
    <main className="main-wrapper">
      <div className="blob blob-1"></div>
      <div className="blob blob-2"></div>
      
      <div className="app-container">
        <div className="header">
          <div className="bot-avatar-large">🧞‍♂️</div>
          <div className="header-text">
            <h2>HelpGenie</h2>
            <p>Always online • Ready to assist</p>
          </div>
        </div>

        <div className="chat-box">
          {messages.map((msg) => (
            <div key={msg.id} className={`message-wrapper ${msg.sender}`}>
              <div className="avatar">{msg.sender === "user" ? "🧑‍💻" : "🧞‍♂️"}</div>
              <div className={`message ${msg.sender}`}>{msg.text}</div>
            </div>
          ))}
          
          {isTyping && (
             <div className="message-wrapper bot">
               <div className="avatar">🧞‍♂️</div>
               <div className="typing-indicator">
                 <div className="dot"></div>
                 <div className="dot"></div>
                 <div className="dot"></div>
               </div>
             </div>
          )}
          <div ref={chatEndRef} />
        </div>

        <div className="input-area">
          <input
            type="text"
            className="input-field"
            placeholder="Type your message..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
          />
          <button className="send-btn" onClick={handleSend} aria-label="Send message">
             <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path d="M3.478 2.404a.75.75 0 0 0-.926.941l2.432 7.905H13.5a.75.75 0 0 1 0 1.5H4.984l-2.432 7.905a.75.75 0 0 0 .926.94 60.519 60.519 0 0 0 18.445-8.986.75.75 0 0 0 0-1.218A60.517 60.517 0 0 0 3.478 2.404Z" />
            </svg>
          </button>
        </div>
      </div>
    </main>
  );
}
