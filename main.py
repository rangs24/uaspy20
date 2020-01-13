from core.baseapp import BaseApp
from data_model.book import book
from view.view_book import ViewBook

class MainApp(BaseApp):
    def __init__(self):
        self.books = []
        self.IBook = []
        self.VBook = []
        BaseApp.__init__(self)

class Vbook(book) :
    def __init__(self):
        vBook =  ViewBook(self,books=self)
        vBook.list_book

    if __name__ == "__main__" :
        app = MainApp()
        app.run()

    @property
    def list_book(self):
        return self.list_book
    def add_book(self):
        return self.add_book()
    def search_book(self):
        return self.search_book()
