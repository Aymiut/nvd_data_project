NVD_DATA Project

NVD_DATA Project

## Prérequis
- Docker et Docker Compose installés
- Python 3.x
- Bibliothèques Python : `requests`, `psycopg2-binary`

## Installation des dépendances
```bash
pip install requests psycopg2-binary
```

Lancer conteneur postgres la première fois:
```bash
docker run --name postgres_cve -e POSTGRES_USER=cve_user -e POSTGRES_PASSWORD=cve_pass -e POSTGRES_DB=cve_db -p 5432:5432 -v postgres_data:/var/lib/postgresql/data -d postgres
```

Les prochaines fois:
```bash
docker start postgres_cve
```

Se connecter à la base:
```bash
docker exec -it postgres_cve psql -U cve_user -d cve_db
```

Voici l'explication du schéma de la base de données que je vais utiliser:

Table cve : Contient les informations principales sur chaque vulnérabilité.

Table cpe : Contient les informations sur les produits affectés par les vulnérabilités.

Table cve_cpe : Associe chaque CVE à un ou plusieurs produits (relation plusieurs-à-plusieurs entre cve et cpe).

Table cve_cwe : Relie les vulnérabilités aux failles de sécurité, permettant de classifier chaque vulnérabilité.

Table cve_reference : Contient des liens externes relatifs aux CVE, comme des patches ou des avis de sécurité.

Le MLD associé:

CVE(_id_, description, cvss_score, published_at, modified_at)

CPE(_id_, criteria, vulnerable, product_name)

CVE_CPE(_cve_id_#, _cpe_id_#)
    cve_id → CVE.id
    cpe_id → CPE.id

CVE_CWE(_cve_id_#, _cwe_id_)
    cve_id → CVE.id

CVE_REFERENCE(cve_id#, url)
    cve_id → CVE.id

Le script init_db.py sert à initialiser la base en créant les tables nécessaires.