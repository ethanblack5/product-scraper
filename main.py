from selectolax.parser import HTMLParser
import httpx

url = "https://www.apple.com/shop/iphone/accessories"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
}

resp = httpx.get(url, headers=headers)
html = HTMLParser(resp.text)

products = html.css(".as-pinwheel-tiletitle a")

for product in products:
    print(product.css_first(".as-pinwheel-tilelink").text())
