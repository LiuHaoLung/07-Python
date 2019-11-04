from difflib import Differ
from difflib import HtmlDiff
from difflib import SequenceMatcher

with open('file1.txt') as f1, open('file2.txt') as f2:
    d1 = Differ().compare(f1.readlines(), f2.readlines())
    print('\n'.join(d1))

with open('file1.txt') as f1, open('file2.txt') as f2:
    # isjunk 規則是忽略某些元素，在這個位置放上 None，代表不忽略任何元素。
    # f1.read()和f2.read()要的是 immutable ，所以不會用 readlines（回傳 list），而是用 read（回傳 string）
    # quick_ratio() 是在計算在這兩個檔案中，有多少的相同百分比，如果都不相同，則 % 為 0，如果是 1 ，則代表兩個檔案完全相同
    d2 = SequenceMatcher(None, f1.read(), f2.read()).quick_ratio()
    # 會介於 0-1 之間
    print(d2)
    # 有兩個小數點（.2f）
    print('There is a %.2f percent match!' % (d2 * 100))

with open('file1.txt') as f1, open('file2.txt') as f2:
    # fromlines 和 tolines 是要比較的檔案
    # fromdesc 和 todesc 是在 html 的表格中，會呈現的欄位名稱
    d3 = HtmlDiff().make_file(fromlines = f1.readlines(), tolines = f2.readlines(), fromdesc = 'file1', todesc = 'file2')
    print(d3, file = open('result.html','w'))