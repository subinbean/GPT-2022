"use client";

import SendMessageBar from "@/app/components/SendMessageBar";
import GPTMessage from "./components/GPTMessage";
import UserMessage from "./components/UserMessage";
import { useState, useEffect, use } from "react";
import { Message } from "./types/types";

export default function Page() {
    const [messages, setMessages] = useState<Message[]>([]);

    return (
        <main className="flex h-screen flex-col items-center p-4">
            <div className="w-full h-4/5 bg-white rounded-lg shadow-md overflow-y-auto">
                {messages.map((message, index) =>
                    message.origin == "user" ? (
                        <UserMessage message={message.content} key={index} />
                    ) : (
                        <GPTMessage
                            message={message.content}
                            citations={message.citations}
                            key={index}
                        />
                    )
                )}
            </div>
            <SendMessageBar setMessages={setMessages} />
        </main>
    );
}
