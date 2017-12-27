'''
remember the point '.' in 'super().__init__()'
'''
class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display(self):
        pass
class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price
    def display(self):
        print('Title:', self.title, sep=' ')
        print('Author:', self.author, sep = ' ')
        print('Price:', self.price, sep = ' ')

new_book = MyBook('Love', 'Jason', 2588)
new_book.display()