import requests
import json  # Pour afficher un JSON bien formaté

NVD_API_URL = 'https://services.nvd.nist.gov/rest/json/cves/2.0'

def fetch_nvd_data():
    response = requests.get(NVD_API_URL)
    if response.status_code == 200:
        return response.json()  # Retourne les données JSON
    else:
        return "Error fetching data"

if __name__ == '__main__':
    vulnerabilities = fetch_nvd_data()
    
    if isinstance(vulnerabilities, dict):  # Vérifie que c'est bien un dictionnaire JSON
        print(json.dumps(vulnerabilities, indent=4))  # Affiche le JSON formaté
