import psycopg2

CVE_TABLE = """CREATE TABLE cve (
    id SERIAL PRIMARY KEY,          
    description TEXT NOT NULL,     
    cvss_score DECIMAL(3,2),       
    published_at TIMESTAMPTZ,       
    modified_at TIMESTAMPTZ         
);"""

CPE_TABLE = """CREATE TABLE cpe (
    id SERIAL PRIMARY KEY,          -- Identifiant unique pour chaque produit
    criteria TEXT NOT NULL,         -- Critère CPE du produit
    vulnerable BOOLEAN,             -- Indicateur de vulnérabilité (true/false)
    product_name TEXT NOT NULL      -- Nom du produit affecté
);"""

CVE_CPE_TABLE = """CREATE TABLE cve_cpe (
    cve_id INT REFERENCES cve(id) ON DELETE CASCADE,    -- Référence à cve
    cpe_id INT REFERENCES cpe(id) ON DELETE CASCADE,    -- Référence à cpe
    PRIMARY KEY (cve_id, cpe_id)                         -- Clé primaire composée
);
"""

CVE_CWE_TABLE = """CREATE TABLE cve_cwe (
    cve_id INT REFERENCES cve(id) ON DELETE CASCADE,    -- Référence à cve
    cwe_id INT,                                         -- ID de la faille CWE
    PRIMARY KEY (cve_id, cwe_id)                        -- Clé primaire composée
);

"""
CVE_REFERENCE_TABLE = """CREATE TABLE cve_reference (
    cve_id INT REFERENCES cve(id) ON DELETE CASCADE,    -- Référence à cve
    url TEXT NOT NULL                                    -- URL de la référence
);"""


def init_db():
    conn = psycopg2.connect("dbname=cve_db user=cve_user password=cve_pass host=localhost port=5432")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS cve_cpe, cve_cwe, cve_reference, cpe, cve;")
    cur.execute(CVE_TABLE)
    cur.execute(CPE_TABLE)
    cur.execute(CVE_CPE_TABLE)
    cur.execute(CVE_CWE_TABLE)
    cur.execute(CVE_REFERENCE_TABLE)
    conn.commit()
    
    cur.close()
    conn.close()


if __name__ == '__main__':
    init_db()
    print("Database initialized successfully")
    
    
    
