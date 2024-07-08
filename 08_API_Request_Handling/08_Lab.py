from pprint import pprint
from requests import get

# Making an API request
response = get('https://newsapi.org/v2/everything?q=tesla&from=2024-02-10&sortBy=publishedAt&apiKey=API_KEY_HERE')
# Get your api key from its website and put in the end to try the code yourself.
data = response.json()

# Printing the entire JSON response
pprint(data)

# Prompt user for author name
auth = input("Author's Name: ")

# Filtering articles based on the author's name using a while loop
i = 0
while i < len(data['articles']):
    if data['articles'][i].get('author') == auth:
        pprint(data['articles'][i])
    i += 1

# Alternative method using a for loop
for article in data.get('articles'):
    if article.get('author') == auth:
        pprint(article)