# 可以去測試是否可以順利執行
# 匯入要測試的檔案
import unittest
import classforunittest1


# 繼承 unittest 類別
class TestCap(unittest.TestCase):

	# 可以去測試任何一種情況
	def test_one_word(self):
		text = 'python'
		result = classforunittest1.cap_text(text)
		self.assertEqual(result,'Python')

	def test_multiple_words(self):
		text = 'monty python'
		result = classforunittest1.cap_text(text)
		self.assertEqual(result,'Monty Python')

if __name__ =='__main__':
	unittest.main()