import Image from "next/image";
import SendMessageBar from "@/app/components/SendMessageBar";

export default function Page() {
    return (
        <main className="flex min-h-screen flex-col items-center p-24">
            <div className="mx-auto max-w-7xl py-6 sm:px-6 lg:px-8">
                {" "}
                Hello World!
            </div>
            <SendMessageBar />
        </main>
    );
}
