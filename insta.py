from bs4 import BeautifulSoup
import requests
# définir le lien à web scraper
url = 'https://www.instagram.com/wij.zx/?__a=1'
# récupérer le contenu du site web
reponse = requests.get(url)
# parser le contenu HTML à l'aide de BeautifulSoup
soup = BeautifulSoup(reponse.text, features="html.parser")
#collect all books
books = soup.findAll(class_='formattedJson')

#Filter title and price from books and print all
print (books);
