from selectolax.parser import HTMLParser
import httpx
import json

url = "https://www.apple.com/shop/iphone/accessories"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
}

resp = httpx.get(url, headers=headers)
html = HTMLParser(resp.text)

products = html.css("div.as-pinwheel-infosection")

prod_dict = {}
for num, product in enumerate(products):
    price = product.css_first("span.as-pinwheel-pricecurrent").text().strip()

    if not price:
        price = None
    
    entry = {
        "title": product.css_first("a.as-pinwheel-tilelink").text().strip(),
        "price": price
    }
    prod_dict[num] = entry

with open("my_json.json", "w", encoding='utf-8') as file:
    json.dump(prod_dict, file, ensure_ascii=False, indent=4)

