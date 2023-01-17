import httpx 

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"

res = httpx.get(url)

data = res.text

rows = data.split("\n")

row = ""
for r in rows:
    if "|EUR|" in r:
        row = r


curr = row.split('|')

print(curr)