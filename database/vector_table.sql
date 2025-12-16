CREATE TABLE document_vectors (
    doc_id NUMBER GENERATED ALWAYS AS IDENTITY,
    content CLOB,
    embedding VECTOR(1024),
    CONSTRAINT document_vectors_pk PRIMARY KEY (doc_id)
);

