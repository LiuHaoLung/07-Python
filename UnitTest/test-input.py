# 檢查使用者所輸入的值
from unittest import mock
from calculator import calculator

class TestClass(object):
    def test_positive_int(self):
        # builtins.input 對應到使用者所輸入的值，return_value就是使用這所輸入的值，也就代表y
        with mock.patch('builtins.input', return_value = 10):
            # 這邊的0，代表index 0，也就代表x
            assert calculator("/Users/How.Short/Desktop/Python內容/Python-class/classforunittest/values.xlsx", 0) == 894
    
    def test_negative_int(self):
        with mock.patch('builtins.input', return_value = -20):
            assert calculator("/Users/How.Short/Desktop/Python內容/Python-class/classforunittest/values.xlsx", 0) == 224
        
    def test_positive_float(self):
        with mock.patch('builtins.input', return_value = 10.33):
            assert calculator("/Users/How.Short/Desktop/Python內容/Python-class/classforunittest/values.xlsx", 0) == 838
        
    def test_negative_float(self):
        with mock.patch('builtins.input', return_value = -9.89):
            assert calculator("/Users/How.Short/Desktop/Python內容/Python-class/classforunittest/values.xlsx", 0) == 914
            
#run with: D:\testing>pytest -rv --disable-warnings test_input.py