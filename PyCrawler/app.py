import html
import requests

from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")
data = []


questions = soup.select(".s-post-summary--content-title")
for ul in soup.find_all('ul'):
    el = []
    for e in ul.find_all('li'):
        el.append(e)
        (data.append(el))
    # print(el)
for question in questions:
    print(question.select_one(".s-link"))
    print(question.select_one(".s-post-summary--stats-items_emphasized"))

#     print(type(questions[0]).select_one(".question-hyperlink").getText)
