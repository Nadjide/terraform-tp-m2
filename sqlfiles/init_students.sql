CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    promo VARCHAR(50) NOT NULL
);

INSERT INTO students (nom, promo) VALUES 
('Alice DuPont', 'M2 DevOps'),
('Bob Martin', 'M2 DevOps'),
('Charlie OConnor', 'M2 Cyber');
