import httpx

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"

res = httpx.get(url)

text = res.text

rows = text.split("\n")
rows = rows[2:-1]

data = {}

row = ""
for r in rows:
        row = r
        curr = row.split('|')
        "del curr [0:3]"
        currency = curr[-2]
        rate = curr[-1]
        rate = rate.replace(",",".")
        rate = float(rate)
        data[currency] = rate

        "print(curr)"


"currency = curr[0]"
"currency = float(currency)"

x = float(input("Zadej castku v CZK "))
y = input("Zadej cilovou menu ")

result = x/data[y]
result = round(result,3)
print(f"Vysledek je {result}{y}.")

"print(sum)"
