"use client"; 

import { useState } from "react";
import { fetchChatResponse } from "@/utils/api";

export default function ChatBox() {
  const [messages, setMessages] = useState<
    { text: string; type: "user" | "bot" }[]
  >([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;

    setMessages((prev) => [...prev, { text: input, type: "user" }]);
    setInput("");

    const response = await fetchChatResponse(input);
    setMessages((prev) => [...prev, { text: response, type: "bot" }]);
  };

  return (
    <div className="chat-container">
      {/* 채팅 메시지 영역 */}
      <div className="chat-messages">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`flex ${
              msg.type === "user" ? "justify-end" : "justify-start"
            }`}
          >
            <span
              className={`p-3 rounded-xl text-sm max-w-xs ${
                msg.type === "user"
                  ? "bg-blue-500 text-white"
                  : "bg-gray-300 text-black"
              }`}
            >
              {msg.text}
            </span>
          </div>
        ))}
      </div>

      {/* 입력 필드 */}
      <div className="flex mt-4">
        <input
          className="chat-input"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message..."
        />
        <button className="chat-button" onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
}
