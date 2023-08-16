import React from "react";

const SendMessageBar = () => {
    return (
        <div>
            <div className="flex flex-col w-full">
                <input
                    className=""
                    type="text"
                    name="message"
                    id="message"
                    placeholder="Try asking a question!"
                />
            </div>
        </div>
    );
};

export default SendMessageBar;
