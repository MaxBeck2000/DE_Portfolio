-- Russian Equipment Losses V2
-- PostgreSQL relational schema

CREATE TABLE IF NOT EXISTS losses (
    loss_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    equipment_type TEXT NOT NULL,
    model TEXT NOT NULL,
    description TEXT NOT NULL,
    first_scraped_date DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE TABLE IF NOT EXISTS evidence (
    evidence_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    url TEXT NOT NULL UNIQUE,
    source_type TEXT,
    post_date DATE,
    first_scraped_date DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE TABLE IF NOT EXISTS loss_evidence (
    loss_id BIGINT NOT NULL,
    evidence_id BIGINT NOT NULL,

    PRIMARY KEY (loss_id, evidence_id),

    FOREIGN KEY (loss_id)
        REFERENCES losses(loss_id)
        ON DELETE CASCADE,

    FOREIGN KEY (evidence_id)
        REFERENCES evidence(evidence_id)
        ON DELETE CASCADE
);
