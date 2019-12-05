import requests
from bs4 import BeautifulSoup
from newspaper import Article

response = requests.get('https://www.bbc.com/ukrainian')
doc = BeautifulSoup(response.text, 'html.parser')
# print(doc)

# headlines = doc.find_all('h3')

# for headline in headlines:
#     print(headline.text)
links = doc.find_all('a', { 'class': 'title-link' })

for link in links:
    # print(link.text)
    # print('http:/' + link['href'])
    article_address = 'https://www.bbc.com' + link['href']
    try:
        # article = requests.get(article_address)
        page = requests.request("GET", article_address)
        article = Article(article_address)

        article.download()
        article.parse()

        print(article.text)
    except:
        pass
    

    
    # doc_article = BeautifulSoup(article.text, 'html.parser')
    # stories = doc_article.find_all('p', _class = "story-body")
    # print(doc_article.prettify())
    # for story in stories:
    #     article_body = story.find_all('p')
    #     print(story.string)
        # for i in article_body:
        #     print(i)
    #     print(story.string)
# stories = doc.find_all('div', { 'class': 'gs-c-promo' })
# for story in stories:
#     print(story.text)