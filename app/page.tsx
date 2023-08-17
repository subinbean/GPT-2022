import Image from "next/image";
import SendMessageBar from "@/app/components/SendMessageBar";
import GPTMessage from "./components/GPTMessage";

export default function Page() {
    return (
        <main className="flex h-screen flex-col items-center p-16">
            <div className="w-full h-3/4 bg-white rounded-lg shadow-md">
                <div className="text-white bg-cyan-800 h-auto p-10 flex">
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        strokeWidth={1.5}
                        stroke="currentColor"
                        className="w-6 h-6 mr-3">
                        <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z"
                        />
                    </svg>
                    User message goes here.
                </div>
                <GPTMessage message="System response goes here" />
            </div>
            <SendMessageBar />
        </main>
    );
}
