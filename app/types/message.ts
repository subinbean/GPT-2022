export type message = {
    content: string;
    origin: "user" | "gpt";
    citations: [];
};
