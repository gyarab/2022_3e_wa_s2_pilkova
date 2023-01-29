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
        hundred = curr[-3]
        rate = curr[-1]
        rate = rate.replace(",",".")
        rate = float(rate)
        hundred = float(hundred)
        if hundred == 100: 
            rate = rate/100
        if hundred == 1000:
            rate = rate/1000


        data[currency] = rate

        "print(curr)"


"currency = curr[0]"
"currency = float(currency)"

PINK= '\033[95m'
GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
END = '\033[0m'

a = int(input(PINK + "Pro převod z CZK na jinou měnu, stiskněte 1 a pokud chcete převádět z cízí měny na CZK, stiskněte 2: " + END))


if a == 1:
    x = float(input(GREEN +"Zadej castku v CZK " + END))
    y = input(RED +"Zadej cilovou menu " + END)

    result = x/data[y]
    result = round(result,3)
    print(BLUE + f"Vysledek je {result}{y}." + END)

if a == 2:
    z = input(RED + "Zadej menu " + END)
    b = float(input (GREEN + "Zadej Castku " + END))

    res = b*data[z]
    result = round(res,3)
    print(BLUE + f"Vysledek je {res} CZK." + END)





"print(sum)"