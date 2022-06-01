from bs4 import BeautifulSoup
import requests
# définir le lien à web scraper
url = 'https://books.toscrape.com/catalogue/category/books/classics_6/index.html'
# récupérer le contenu du site web
reponse = requests.get(url)
# parser le contenu HTML à l'aide de BeautifulSoup
soup = BeautifulSoup(reponse.text, features="html.parser")
#collect all books
books = soup.findAll(class_='product_pod')

#sorted books by book price
def price(e):
    return e.find(class_='price_color').get_text()[2::]
books.sort(key=price,reverse=True)

#Filter title and price from books and print all
for book in books:
    title = book.h3.a.get_text()
    price = book.find(class_='price_color').get_text()[2::]
    print(title,price)
