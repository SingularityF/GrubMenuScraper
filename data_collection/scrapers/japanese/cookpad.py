import requests
import re
from bs4 import BeautifulSoup

##### User config #####
page_lower = 1
# page_upper = 'max' to scrape all the pages
page_upper = 'max'
category_list = [1607]
output_file = 'cookpad_pot.txt'


##### Main logic #####
recipe_titles = []

for category in category_list:
    url = f'https://cookpad.com/category/{category}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    page_display = soup.find("span", {"class": "page_num"})
    page_text = page_display.getText()
    re_part = re.search(r'[0-9]+ / ([0-9]+)ページ',page_text)
    max_page = int(re_part.group(1))
    if page_upper == 'max':
        page_upper = max_page
    for page in range(page_lower,page_upper+1):
        url = f'https://cookpad.com/category/{category}?page={page}'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        all_titles = soup.find_all("a", {"class": "recipe-title"})
        for title in all_titles:
            recipe_titles.append(title.getText())

with open(output_file,'w',encoding="utf-8") as f:
    for title in recipe_titles:
        f.write(title+'\n')