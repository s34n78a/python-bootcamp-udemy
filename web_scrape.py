import requests
import bs4

res = requests.get('https://quotes.toscrape.com/')
print(res.text)
soup = bs4.BeautifulSoup(res.text, 'lxml')
#print(soup)

print()

authors = soup.select('.author')
#print(authors)
author_set = set()
for author in authors:
    author_set.add(author.getText())
print(sorted(author_set))

print()

quotes = soup.select('.quote .text')
#print(quotes)
quotes = [quotes[x].getText() for x in range(len(quotes))]
print(quotes)

print()

top_tags = soup.select('.tag-item .tag')
#print(top_tags)
for tag in top_tags:
    print(tag.getText())

page_num = 1
author_set = set()
while True:
    res = requests.get('http://quotes.toscrape.com/page/{}/'.format(page_num))
    #print(res.text)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    authors = soup.select('.author')
    if authors == []:
        break
    for author in authors:
        author_set.add(author.getText())
    #print(page_num, sorted(author_set))
    page_num += 1
print(sorted(author_set))