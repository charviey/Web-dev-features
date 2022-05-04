#!/usr/bin/env python
# coding: utf-8

# Q1) Assume we have a function get_book_info(isbn) that takes a string ISBN argument and
# retrieves an object containing the Title, Author, and Language of a book (each represented as a string) that
# takes a nontrivial amount of time to run (perhaps because it’s making a call to a database). Write a
# wrapper function that increases performance by keeping results in memory for the quick lookup. To prevent
# memory from growing unbounded, we only want to store a maximum of N book records. At any given time,
# we should be storing the N books that we accessed most recently. Assume that N can be a large number
# when choosing data structure(s) and algorithm(s).

# In[8]:


def get_book_info(isbn):

    openLibraryUrl = "https://openlibrary.org/api/books"
    parameters = {"bibkeys": f"ISBN:{isbn}", "format": "json", "jscmd": "data"}
    response = requests.get(openLibraryUrl, params=parameters)
    book_info = response.json()[f"ISBN:{isbn}"]

    title = book_info["title"]
    authorNames = []
    
    for author in book_info["authors"]:
        authorNames.append(author["name"])
    languageBook = book_info["cover"]["small"] if "cover" in book_info else ""

    return (title, authorNames, languageBook)

