import requests
import bs4

# Get number of pages 7286/50 = 145.72
total_pages = 146
# Generate World University URL list
root_url = 'http://univ.cc/search.php?dom=world&key=&start='
url_list = [root_url + "1"]
j = 50
for i in range(1, 146):
    url_list.append(root_url + str(j + 1))
    j += 50

names = []
for link in url_list:
    response = requests.get(link)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    new_names = [a.get_text() for a in soup.select('li a')]
    names.extend(new_names)

with open('world_univ_names.txt', 'w') as f:
    for s in names:
        f.write((s.encode('unicode-escape') + u'\n'))
