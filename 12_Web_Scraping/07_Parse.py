import bs4, requests

def getBookPrice(productUrl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # elems = soup.select('#a-autoid-2-announce > span.slot-price > span')
    elems = soup.select('#edit-attributes-1 > div:nth-child(2) > label')
    if elems:
        return elems[0].text.strip()
    else:
        return 'Price not found'
   


price = getBookPrice('https://nostarch.com/automatestuff2')
print('The price is', price)
# The price is Ebook (PDF, Mobi, and ePub), $31.99