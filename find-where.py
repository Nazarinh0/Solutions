TITLE, AUTHOR, YEAR = 'title', 'author', 'year'
BOOKS = [
    {TITLE: 'Book of Fooos', AUTHOR: 'Foo', YEAR: 1111},
    {TITLE: 'Cymbeline', AUTHOR: 'Shakespeare', YEAR: 1611},
    {TITLE: 'The Tempest', AUTHOR: 'Shakespeare', YEAR: 1611},
    {TITLE: 'Book of Foos Barrrs', AUTHOR: 'FooBar', YEAR: 2222},
    {TITLE: 'Still foooing', AUTHOR: 'FooBar', YEAR: 333},
    {TITLE: 'Happy Foo', AUTHOR: 'FooBar', YEAR: 4444},
]


def find_where(books, request):
     for items in books:
        print('ITEM VALUES', set(items.values()))
        print('REQUEST VALUES', set(request.values()))
        print(set(request.values()).issubset(items.values()))
        if set(request.values()).issubset(items.values()):
            return items
     return None


print(find_where(BOOKS, {AUTHOR: 'Shakespeare', YEAR: 1611}))