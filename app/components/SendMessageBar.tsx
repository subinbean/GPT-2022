"use client";

import React, { useState } from "react";
import { Message } from "../types/message";

const SendMessageBar = (props: {
    setMessages: React.Dispatch<React.SetStateAction<Message[]>>;
}) => {
    const [query, setQuery] = useState("");

    console.log(query);
    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setQuery(event.target.value);
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
            <button className="p-3 text-slate-600 rounded-r-lg focus:outline-none">
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
