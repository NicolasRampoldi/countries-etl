CREATE TABLE countries
(
    id SERIAL PRIMARY KEY,
    name       VARCHAR(255),
    capital    VARCHAR(255),
    currency   VARCHAR(255),
    continent  VARCHAR(255),
    language   VARCHAR(255),
    population INT,
    flag       VARCHAR(255)
);