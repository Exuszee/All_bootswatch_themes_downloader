import requests
from bs4 import BeautifulSoup as soup
import os


def create_project_directory(dir_name):
    if not os.path.exists(dir_name):
        print('Creating directory ... ' + str(dir_name))
        os.makedirs(dir_name)

url = "https://bootswatch.com/"
uht = requests.get(url).text
usp = soup(uht, 'lxml')

cont = usp.find_all('div', {'class':'preview'})
print(len(cont))
try:
    for i in cont:
        title = i.find('div', {'class':'options'}).h3.text.strip()
        desc = i.find('div', {'class':'options'}).p.text.strip()
        link = "https://bootswatch.com/" + i.find('div', {'class':'options'}).find_all('div', {'class':'btn-group'})[1].a['href']
        img = "https://bootswatch.com/" + str(title.lower()) + "/thumbnail.png"
        file_save_name = str(title) + "_bootstrap.min.css"
        img_save_name = str(title) + "_thumbnail.png"
        create_project_directory("Themes_bootswatch/" + str(title))
        dir_name = "Themes_bootswatch/" + str(title) + "/"
        print(title, desc, link)
        dl_url = str(link)
        img_url = str(img)
        r = requests.get(dl_url, allow_redirects=True)
        r2 = requests.get(img_url, allow_redirects=True)

        open(str(dir_name) + str(file_save_name), 'wb').write(r.content)
        open(str(dir_name) + str(img_save_name), 'wb').write(r2.content)
except IndexError as e:
    print("Completed Downloading all available themes with their Previews. :)")
