"use client";

import SendMessageBar from "@/app/components/SendMessageBar";
import GPTMessage from "./components/GPTMessage";
import UserMessage from "./components/UserMessage";
import { useState, useEffect, use } from "react";
import { Message } from "./types/message";

export default function Page() {
    const [messages, setMessages] = useState<Message[]>([]);

    return (
        <main className="flex h-screen flex-col items-center p-16">
            <div className="w-full h-3/4 bg-white rounded-lg shadow-md">
                {messages.map((message, index) =>
                    message.origin == "user" ? (
                        <UserMessage message={message.content} key={index} />
                    ) : (
                        <GPTMessage message={message.content} key={index} />
                    )
                )}
            </div>
            <SendMessageBar setMessages={setMessages} />
        </main>
    );
}
