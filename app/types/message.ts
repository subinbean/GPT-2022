export type Message = {
    content: string;
    origin: "user" | "gpt";
    citations?: string[];
};
