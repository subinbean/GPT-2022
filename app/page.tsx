import Image from "next/image";
import SendMessageBar from "@/app/components/SendMessageBar";

export default function Page() {
    return (
        <main className="flex min-h-screen flex-col items-center p-24">
            <div className="w-full min-h-full mx-auto bg-white p-4 rounded-lg shadow-md">
                <div className="space-y-4">
                    <div className="bg-gray-300 text-gray-700 p-3 rounded-lg">
                        User message goes here.
                    </div>
                    <div className=" text-white p-3 rounded-lg bg-emerald-700">
                        System response goes here.
                    </div>
                </div>
            </div>
            <div className="flex w-full items-center my-4">
                <input
                    type="text"
                    placeholder="Type a question!"
                    className="flex-1 p-2 rounded-l-lg border focus:outline-none"
                />
                <button className="bg-blue-500 text-white p-2 rounded-r-lg hover:bg-blue-600 focus:outline-none">
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        className="h-6 w-6"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor">
                        <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            strokeWidth={2}
                            d="M12 6v6m0 0v6m0-6h6m-6 0H6"
                        />
                    </svg>
                </button>
            </div>
        </main>
    );
}
