from googletrans import Translator
from utils import f_path

with open(f"{f_path}text_4.txt", 'r', encoding='utf-8') as f1:
    content = f1.read().split('\n')
    for el in content:
        print(el)
        print(Translator().translate(el, dest='ru'))

# чаще всего на рандомных строках вылетала такая ошибка:
# C:\Python3\python.exe C:/PyProjects/PythonHomeWork/test_translate.py
# One - 1
# Translated(src=en, dest=ru, text=Один - 1, pronunciation=Odin - 1, extra_data="{'translat...")
# Two - 2
# Translated(src=en, dest=ru, text=Два - 2, pronunciation=Dva - 2, extra_data="{'translat...")
# Three - 3
# Translated(src=en, dest=ru, text=Три - 3, pronunciation=Tri - 3, extra_data="{'translat...")
# Four - 4
# Traceback (most recent call last):
#   File "C:\PyProjects\PythonHomeWork\test_translate.py", line 8, in <module>
#     print(Translator().translate(el, dest='ru'))
#   File "C:\Python3\lib\site-packages\googletrans\client.py", line 182, in translate
#     data = self._translate(text, dest, src, kwargs)
#   File "C:\Python3\lib\site-packages\googletrans\client.py", line 78, in _translate
#     token = self.token_acquirer.do(text)
#   File "C:\Python3\lib\site-packages\googletrans\gtoken.py", line 194, in do
#     self._update()
#   File "C:\Python3\lib\site-packages\googletrans\gtoken.py", line 62, in _update
#     code = self.RE_TKK.search(r.text).group(1).replace('var ', '')
# AttributeError: 'NoneType' object has no attribute 'group'
#
# Process finished with exit code 1
