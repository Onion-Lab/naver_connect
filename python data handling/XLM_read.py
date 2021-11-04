from bs4 import BeautifulSoup

with open("D:\\Python\\Naver_connect\\python_data_handling\\books.xml","r",encoding="utf-8") as books_file :
    books_xml = books_file.read()

soup = BeautifulSoup(books_xml, "lxml")

for book_info in soup.find_all("author") :
    print(book_info)
    print(book_info.get_text())

    