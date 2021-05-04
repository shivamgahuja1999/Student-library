class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("books present in this library are : ")
        for book in self.books:
            print("     * "+book)

    def borrowBook(self, bookname):
        if bookname in self.books:
            print(
                f"you have been issued {bookname}. Please keep it safe otherwise you will be fined")
            self.books.remove(bookname)
            return True
        else:
            print(
                "This book is either not available or someone has already issued this book.Please wait untill the book is returned")
            return False

    def returnBook(self, bookname):
        print("Thanks for returning this book")
        self.books.append(bookname)


class Student:
    def requestBook(self):
        self.book = input("enter the book you want to issue: ")
        return self.book

    def returnBook(self):
        self.book = input("enter the book you want to return: ")
        return self.book

    def displayIssuedBooks(self):
        pass

if __name__=="__main__":
    centralLibrary =Library(["python","java","c programming","c++","c#","PHP"])
    student=Student()
    # centralLibrary.displayAvailableBooks()
    while True:
        welcomeMsg='''****Welcome to Central Library*****
        Please choose an option:
        1. List all books
        2. Request a book
        3. Add / Return a book
        4. Exit
        '''
        print(welcomeMsg)
        a=int(input("____enter a choice____\n"))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for choosing central library.Have a nice day")
            exit()
        else:
            print("invalid choice")