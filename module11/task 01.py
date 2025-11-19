class Publication:
    def __init__(self,name):
        self.name = name

    def print_information(self):
        print(f"publication name is {self.name}")

class Book(Publication):
    def __init__(self,name,author,page_count):
        self.author = author

        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"author :{self.author} page count: {self.page_count}")


class Magazine(Publication):
    def __init__(self,name,chief_editor):
        self.editor = chief_editor
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"chief editor : {self.editor}")

magazine = Magazine("Donald Duck","Aki Hyyppa")
magazine.print_information()

book1 = Book("Compartment No.6","Rosa Liksom",192)
book1.print_information()