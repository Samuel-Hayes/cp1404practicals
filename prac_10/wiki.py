import wikipedia

page = input("Enter page: ")
# while page != '':
#     page = input("Enter page: ")
wikipedia.search(page)
wikipedia.summary("Google")
wikipedia.page(page)
