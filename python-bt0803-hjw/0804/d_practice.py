class Book:
    title = ""
    author = ""
    def set_info(self, title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print(f'Title : {self.title}, Author : {self.author}')

book1 = Book()
book1.set_info('아낌없이 주는 나무', '쉘 실버스틴')

book2 = Book()
book2.set_info('키다리 아저씨', '진 웹스터')

book_list = [book1, book2]

for book in book_list:
    book.print_info()