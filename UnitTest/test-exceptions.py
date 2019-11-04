# 檢查例外
import pytest
from unittest import mock
from calculator import calculator

class TestClass(object):
    def test_FileNotFoundError(self):
    	# excel檔案找不到錯誤
        with mock.patch('builtins.input', return_value = 10), pytest.raises(FileNotFoundError):
            calculator("/Users/How.Short/Desktop/Python內容/Python-class/classforunittest/value.xlsx", 0)
    
    def test_KeyError(self):
    	# excel裡面的index錯誤
        with mock.patch('builtins.input', return_value = 10), pytest.raises(KeyError):
            calculator("/Users/How.Short/Desktop/Python內容/Python-class/classforunittest/values.xlsx", 7)
        
    def test_ZeroDivisionError(self):
    	# 輸入的值是0，分母為0的錯誤
        with mock.patch('builtins.input', return_value = 0), pytest.raises(ZeroDivisionError):
            calculator("/Users/How.Short/Desktop/Python內容/Python-class/classforunittest/values.xlsx", 0)
            
#run with: D:\testing>pytest -rv --disable-warnings test_exceptions.py