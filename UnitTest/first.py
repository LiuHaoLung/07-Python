def my_func(x, y, z):
    return x + y + z

# 要用test開頭，並在terminal的地方，進到這個檔案的位置，並執行pytest    
def test_result1():
    assert my_func(1, 2, 3) == 5
    
'''
def my_exception():
    div = 10 / 0
    return div
    
def test_result1():
    with pytest.raises(ZeroDivisionError):
        my_exception()
'''