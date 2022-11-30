"""
Testing and using APIs
"""

import wikipedia

search_phrase = input("Search: ")
while input != "":
    try:
        title = wikipedia.search(search_phrase)
        summary = wikipedia.summary(search_phrase)
        page = wikipedia.page(search_phrase)
        url = page.url
        print(title)
        print(summary)
        print(url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
