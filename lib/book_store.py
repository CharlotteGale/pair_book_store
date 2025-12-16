class BookStore:
    def __init__(self, id, title, author_name):
        self.id = id
        self.title = title
        self.author_name = author_name

    def __repr__(self):
        return f"BookStore({self.id}, {self.title}, {self.author_name})"
    def __eq__(self, other):
        return self.__dict__ == other.__dict__