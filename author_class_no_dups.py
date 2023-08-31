#Part 2
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def __str__(self):
        if self.books:
            book_list = ', '.join(self.books)
        else:
            book_list = 'None'
        return f'Author\'s name: {self.name} - Books Published: {book_list}' 


    def publish(self, title):#no double underscore required?
        if title not in self.books:# I think this filters out dups?
            self.books.append(title)
        else:
            print('Cannot add duplicate books.')

def main():
    auth1 = Author('auth1')
    auth1.publish('book1')#calling in the publish method? with .publish, with string argument? 
    auth1.publish('book2')
    auth1.publish('book2')#adding duplicate here
    # print(auth1.name)#this not useful?
    print(auth1)

    auth2 = Author('auth2')
    auth2.publish('book1354135')
    auth2.publish('bookyjryjry')
    print(auth2)

    auth3 = Author('auth3')
    print(auth3)
main()



