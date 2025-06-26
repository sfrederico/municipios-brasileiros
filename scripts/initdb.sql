CREATE TABLE public.municipios (
    id SERIAL PRIMARY KEY,
    uf CHAR(2) NOT NULL,
    cod_uf INTEGER NOT NULL,
    cod_municipio INTEGER NOT NULL,
    nome_municipio VARCHAR(255) NOT NULL,
    capital_estado VARCHAR(10) NOT NULL,
    populacao BIGINT NOT NULL
);

COPY public.municipios (uf, cod_uf, cod_municipio, nome_municipio, capital_estado, populacao)
FROM '/data/municipios.csv'
DELIMITER ';'
CSV HEADER;