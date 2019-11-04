import pandas
import pytest
import math
from unittest import mock

#Defining the function with 3 parameters
@pytest.fixture
def xyfunc():

    df = pandas.read_excel("/Users/How.Short/Desktop/Python內容/Python-class/classforunittest/values.xlsx")
    
    # excel 裡的值
    x = float(df["Price"][0])
    
    # 使用者輸入的值
    with mock.patch('builtins.input', return_value = 10):
        y = float(input("Enter the value of y: "))
    
    return math.pow(x / y, 2)

def test_result(xyfunc):
    result = round(xyfunc)
    assert result == 894