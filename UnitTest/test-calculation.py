# 檢查結果是不是對的
from unittest import mock
from calculator import calculator

class TestClass(object):
    def test_index0(self):
        with mock.patch('builtins.input', return_value = 10):
            assert calculator("/Users/How.Short/Desktop/Python內容/Python-class/classforunittest/values.xlsx", 0) == 894
    
    def test_index1(self):
        with mock.patch('builtins.input', return_value = 10):
            assert calculator("/Users/How.Short/Desktop/Python內容/Python-class/classforunittest/values.xlsx", 1) == 3648
        
    def test_index2(self):
        with mock.patch('builtins.input', return_value = 10):
            assert calculator("/Users/How.Short/Desktop/Python內容/Python-class/classforunittest/values.xlsx", 2) == 207
        
    def test_index3(self):
        with mock.patch('builtins.input', return_value = 10):
            assert calculator("/Users/How.Short/Desktop/Python內容/Python-class/classforunittest/values.xlsx", 3) == 497
            
    def test_index4(self):
        with mock.patch('builtins.input', return_value = 10):
            assert calculator("/Users/How.Short/Desktop/Python內容/Python-class/classforunittest/values.xlsx", 4) == 2025
            
#run with: D:\testing>pytest -rv --disable-warnings test_calculation.py