from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
#print(response.text) #prints page source

soup = BeautifulSoup(response.text, "html.parser")

#get the news with the highest up-voting points on first page
#arrow in front of title: div class votearrow
#title link: inside span class titleline

#get article_tag text from a, with classes title and titlespan
#print(soup.title)

#article text
article_tag_spans = soup.find_all("span", class_="titleline")

article_texts = []
article_links = []
article_upvotes = []

for span in article_tag_spans:
    article_tag = span.find("a")  # get the <a> inside each <span>
    if article_tag:
        text = article_tag.get_text()
        link = article_tag.get("href")
        article_texts.append(text)
        article_links.append(link)
    else:
        article_texts.append("No title found")
        article_links.append("No link found")

#article upvote, get just the number fro "62 points" and convert it to int
article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all("span", class_="score")]

#print(article_texts)
#print(article_links)
#print(article_upvotes)

#Challenge: print out the title of the article with the highest number of upvotes
most_upvotes = max(article_upvotes)
most_upvoted_index = article_upvotes.index(most_upvotes)

print(article_texts[most_upvoted_index])
print(article_links[most_upvoted_index])


