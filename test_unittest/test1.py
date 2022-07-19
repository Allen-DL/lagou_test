import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
        print("cg")
    # setUpClass 和 tearDownClass 是在整个类的前后分别调用的方法
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown  calss")

    # setUp 和 tearDwon 方法是在每条测试用例前后分别调用的方法
    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_adc(self):

        print("acv")


if __name__ == '__main__':
    unittest.main()
