import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com')
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, 'html.parser')
news_titles_tag = soup.find_all(name="a", class_="titlelink")
print(news_titles_tag)
news_text = [text.text for text in news_titles_tag]
news_link = [link.get("href") for link in news_titles_tag]
article_upvotes = [int(score.text.split()[0]) for score in soup.find_all(name="span", class_="score")]
print(news_text)
print(news_link)
print(article_upvotes)

max_vote = max(article_upvotes)
max_vote_index = article_upvotes.index(max_vote)
print(f"The article with the most votes is {news_text[max_vote_index]} with {max_vote} votes. \nLink:"
      f" {news_link[max_vote_index]}")