import requests

NVD_API_URL = 'https://services.nvd.nist.gov/rest/json/cves/2.0'

def fetch_nvd_data():
    response = requests.get(NVD_API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return "Error fetching data"
    
if __name__ == '__main__':
    vulnerabilities = fetch_nvd_data()
    if vulnerabilities:
        print(vulnerabilities)