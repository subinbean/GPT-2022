export type DocumentMetadata = {
    page: number;
    source: string;
};

export type Document = {
    metadata: DocumentMetadata;
    page_content: string;
};

export type Message = {
    content: string;
    origin: "user" | "gpt";
    citations?: Document[];
};
