import pandas as pd

class Book:
    def __init__(self, book_id,title,author):
        self.book_id=book_id; self.title=title; self.author=author; self.available=True
    def display(self):
        print(f"{self.book_id} | {self.title} | {self.author} | {'Available' if self.available else 'Issued'}")

class Node:
    def __init__(self,book):
        self.book=book; self.next=None

class LinkedList:
    def __init__(self): self.head=None
    def append(self,book):
        n=Node(book)
        if not self.head: self.head=n; return
        t=self.head
        while t.next: t=t.next
        t.next=n
    def __iter__(self):
        t=self.head
        while t:
            yield t.book
            t=t.next

class Queue:
    def __init__(self): self.queue=[]
    def enqueue(self,name): self.queue.append(name)
    def dequeue(self): return self.queue.pop(0) if self.queue else None
    def display(self): print(self.queue if self.queue else "Waiting queue is empty.")

class Library:
    def __init__(self):
        self.__books=LinkedList()
        self.waiting_queue=Queue()
        for b in [Book("1","Calculus","Eshan"),Book("2","OOP","Abdullah"),Book("3","Accounting","Alisha"),Book("4","PSHR","Aniqa"),Book("5","PST","Hamza")]:
            self.__books.append(b)

    def add_book(self):
        self.__books.append(Book(input("Book ID: "),input("Title: "),input("Author: ")))
        print("Book added.")

    def view_books(self):
        for b in self.__books: b.display()

    def search_book(self):
        key=input("Enter title: ").lower()
        found=False
        for b in self.__books:
            if key in b.title.lower():
                b.display(); found=True
        if not found: print("Book not found.")

    def issue_book(self):
        bid=input("Book ID: ")
        for b in self.__books:
            if b.book_id==bid:
                if b.available:
                    b.available=False; print("Book issued.")
                else:
                    self.waiting_queue.enqueue(input("Book unavailable. Enter your name: "))
                    print("Added to waiting queue.")
                return
        print("Book not found.")

    def return_book(self):
        bid=input("Book ID: ")
        for b in self.__books:
            if b.book_id==bid:
                b.available=True
                print("Book returned.")
                n=self.waiting_queue.dequeue()
                if n: print(n,"can now issue this book.")
                return
        print("Book not found.")

    def export_books(self):
        df=pd.DataFrame([{"ID":b.book_id,"Title":b.title,"Author":b.author,"Available":b.available} for b in self.__books])
        print(df)

library=Library()
while True:
    print("\n1.Add Book\n2.View Books\n3.Search Book\n4.Issue Book\n5.Return Book\n6.View Waiting Queue\n7.Export Report\n8.Exit")
    c=input("Choice: ")
    if c=="1": library.add_book()
    elif c=="2": library.view_books()
    elif c=="3": library.search_book()
    elif c=="4": library.issue_book()
    elif c=="5": library.return_book()
    elif c=="6": library.waiting_queue.display()
    elif c=="7": library.export_books()
    elif c=="8": break
    else: print("Invalid choice.")