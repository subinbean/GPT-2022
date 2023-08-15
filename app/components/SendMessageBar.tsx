import React from "react";

const SendMessageBar = () => {
    return (
        <div>
            <div className="relative mt-2 rounded-md shadow-sm">
                <input
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
