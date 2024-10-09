import requests
from bs4 import BeautifulSoup

url = "https://www.lille.fr/Votre-Mairie/Le-conseil-municipal/Les-arretes-et-deliberations"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    pdf_list = []
    
    a_tags = soup.find_all('a', href=True)
    for a in a_tags:
        href = a['href']
        if href.endswith('.pdf'):
            pdf_list.append(href)
    
    print(pdf_list)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")