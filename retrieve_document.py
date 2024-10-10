import requests
from bs4 import BeautifulSoup

url = "https://www.lille.fr/Votre-Mairie/Le-conseil-municipal/Les-arretes-et-deliberations"



def get_list_of_files(url):
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

        return pdf_list
    else:
        return None


get_list_of_files(url)


def download_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        filename = url.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(response.content)
        return filename


download_file('https://www.lille.fr/content/download/305071/3409672/file/BO+VDL+du+03+janvier+2024.pdf')