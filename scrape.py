from icecream import ic
import requests
from mylib.pedal import Pedal
from bs4 import BeautifulSoup, re

from pathlib import Path
import jsonpickle # pip install jsonpickle
import json
import yaml # pip install pyyaml

html_doc = Path('pedals.html').read_text()

soup = BeautifulSoup(html_doc, 'html.parser')
modules = soup.find_all("div", class_="box-module")

for m in modules:

    modulehref = m.find('div', attrs={'class' : 'lnk-thumb-img'}).find('a', href=True)['href']
    name = m.find("h3", class_="module-name").get_text().strip()
    manufacturer = m.find("h4", class_="module-name").get_text().strip()
    id = m["data-module-id"]

    ic(modulehref)

    r = requests.get(modulehref)
    current_soup = BeautifulSoup(r.content , 'html.parser')

    c = current_soup.contents
    functs = current_soup.find('div', class_='module-tags').find_all("span")
    funct = list(map(lambda i: i.get_text().strip(), functs))

    box_specs = current_soup.find('div', class_='box-specs')

    dimensions = box_specs.find("dt", text="Dimensions")
    dimensions = dimensions.parent.find_all("dd") if dimensions is not None else ''

    current = box_specs.find("dt", text=re.compile('Current'))
    current = ' / '.join(list(map(lambda i: i.get_text().strip(), current.parent.find_all("span")))) if current is not None else ''

    cost = box_specs.find("dt", text="Price")
    cost = ''.join(list(map(lambda i: i.get_text().strip(), cost.parent.find_all("dd")))) if cost is not None else ''

    div_module_details = current_soup.find("div", id="module-details").get_text().strip()
       
    t = Pedal(id, name, funct, manufacturer, dimensions, current, cost, div_module_details)

    serialized = jsonpickle.encode(t, max_depth=2) # max_depth is optional
    # ic( json.dumps(json.loads(serialized), indent=4))
    with open(f'out/{t.hrid}.json', 'w', encoding='utf-8') as f:
        json.dump(json.loads(serialized), f, ensure_ascii=False, indent=4)


    # print( yaml.dump(yaml.load(serialized), indent=4))