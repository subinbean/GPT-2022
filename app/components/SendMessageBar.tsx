"use client";

import React, { useState, use } from "react";
import { Message } from "../types/types";

const SendMessageBar = (props: {
    messages: Message[];
    setMessages: React.Dispatch<React.SetStateAction<Message[]>>;
}) => {
    const [query, setQuery] = useState("");

    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setQuery(event.target.value);
    };

    const generateResponse = async (query) => {
        const res = await fetch("http://localhost:8000/api/generate-response", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(query),
        });
        const response = await res.json();
        console.log(response);
        return response;
    };

    const sendMessage = async () => {
        const userMessage: Message = {
            content: query,
            origin: "user",
        };
        props.setMessages((prevMessages) => [...prevMessages, userMessage]);
        try {
            const response = await generateResponse({
                query: userMessage.content,
            });
            const gptMessage: Message = {
                content: response["result"],
                origin: "gpt",
                citations: response["source_documents"],
            };
            props.setMessages((prevMessages) => [...prevMessages, gptMessage]);
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <div className="flex w-1/2 items-center my-4 mt-16 rounded-lg border">
            <input
                type="text"
                placeholder="Type a question!"
                value={query}
                onChange={handleInputChange}
                className="flex-1 p-3 rounded-l-lg focus:outline-none"
            />
            <button
                onClick={sendMessage}
                className="p-3 text-slate-600 rounded-r-lg focus:outline-none">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    strokeWidth={1.5}
                    stroke="currentColor"
                    className="w-6 h-6">
                    <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        d="M6 12L3.269 3.126A59.768 59.768 0 0121.485 12 59.77 59.77 0 013.27 20.876L5.999 12zm0 0h7.5"
                    />
                </svg>
            </button>
        </div>
    );
};

export default SendMessageBar;
