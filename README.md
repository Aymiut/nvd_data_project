NVD_DATA Project

Lancer conteneur postgres:
docker run --name postgres_cve -e POSTGRES_USER=cve_user -e POSTGRES_PASSWORD=cve_pass -e POSTGRES_DB=cve_db -p 5432:5432 -v postgres_data:/var/lib/postgresql/data -d postgres
Se connecter à la base:
docker exec -it postgres_cve psql -U cve_user -d cve_db

script création table:
-- Table cve
CREATE TABLE cve (
    id SERIAL PRIMARY KEY,          -- Identifiant unique pour chaque CVE
    description TEXT NOT NULL,      -- Description de la vulnérabilité
    cvss_score DECIMAL(3,2),        -- Score CVSS de la vulnérabilité
    published_at TIMESTAMPTZ,       -- Date de publication
    modified_at TIMESTAMPTZ         -- Date de dernière modification
);

-- Table cpe
CREATE TABLE cpe (
    id SERIAL PRIMARY KEY,          -- Identifiant unique pour chaque produit
    criteria TEXT NOT NULL,         -- Critère CPE du produit
    vulnerable BOOLEAN,             -- Indicateur de vulnérabilité (true/false)
    product_name TEXT NOT NULL      -- Nom du produit affecté
);

-- Table cve_cpe (Relation plusieurs-à-plusieurs)
CREATE TABLE cve_cpe (
    cve_id INT REFERENCES cve(id) ON DELETE CASCADE,    -- Référence à cve
    cpe_id INT REFERENCES cpe(id) ON DELETE CASCADE,    -- Référence à cpe
    PRIMARY KEY (cve_id, cpe_id)                         -- Clé primaire composée
);

-- Table cve_cwe (Relation entre CVE et CWE)
CREATE TABLE cve_cwe (
    cve_id INT REFERENCES cve(id) ON DELETE CASCADE,    -- Référence à cve
    cwe_id INT,                                         -- ID de la faille CWE
    PRIMARY KEY (cve_id, cwe_id)                        -- Clé primaire composée
);

-- Table cve_reference (Références externes)
CREATE TABLE cve_reference (
    cve_id INT REFERENCES cve(id) ON DELETE CASCADE,    -- Référence à cve
    url TEXT NOT NULL                                    -- URL de la référence
);
