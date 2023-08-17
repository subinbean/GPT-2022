import Image from "next/image";
import SendMessageBar from "@/app/components/SendMessageBar";
import GPTMessage from "./components/GPTMessage";
import UserMessage from "./components/UserMessage";

export default function Page() {
    return (
        <main className="flex h-screen flex-col items-center p-16">
            <div className="w-full h-3/4 bg-white rounded-lg shadow-md">
                <UserMessage message="User message goes here" />
                <GPTMessage message="System response goes here" />
            </div>
            <SendMessageBar />
        </main>
    );
}
