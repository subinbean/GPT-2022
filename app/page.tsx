"use client";

import SendMessageBar from "@/app/components/SendMessageBar";
import GPTMessage from "./components/GPTMessage";
import UserMessage from "./components/UserMessage";
import { useState } from "react";
import { Message } from "./types/types";
import Loading from "./components/Loading";

export default function Page() {
    const [messages, setMessages] = useState<Message[]>([]);
    const [loading, setLoading] = useState(false);

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
                {loading && <Loading />}
            </div>
            <SendMessageBar
                messages={messages}
                setMessages={setMessages}
                loading={loading}
                setLoading={setLoading}
            />
        </main>
    );
}
