class Book():
    
    def __init__(self,title,author,pages):
        
        self.title = title
        self.author = author
        self.pages = pages

b = Book('Python rocks','Jose',200)
print(b)
print(str(b))

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f'{self.title} by {self.author}'

b = Book('Python rocks','Jose',200)
print(b)
print(str(b))

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages  
    def __str__(self):
        return f'{self.title} by {self.author}'
    def __len__(self):
        return self.pages

b = Book('Python rocks','Jose',200)
print(b)
print(len(b))

class Book():
    def __init__(self,title,author,pages):
        
        self.title = title
        self.author = author
        self.pages = pages 
    def __str__(self):
        return f'{self.title} by {self.author}'
    def __len__(self):
        return self.pages
    # 為了要在刪除物件時，出現一個訊息
    def __del__(self):
        print('A book object has been deleted!')

b = Book('Python rocks','Jose',200)
print(b)
print(len(b))
# 再用 del 時，不需要再額外加上 print()
del b