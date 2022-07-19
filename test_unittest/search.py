'''
    Created by dl on 2022/7/19
    PROJECT_NAME：lagou_test
'''
import unittest


class Search:
    def search_fun(self):
        print("search")
        return True


class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setUp Class")
        cls.search = Search()

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDown Class")
        # cls.search = Search()

    # def setUp(self) -> None:
    #     print("setUp")
    #     self.search = Search()
    #
    # def tearDown(self) -> None:
    #     print("tearDown")
    #     # self.search = Search

    def test_search1(self):
        print("test_search1")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search2(self):
        print("test_search2")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search3(self):
        print("test_search3")
        # search = Search()
        assert True == self.search.search_fun()


if __name__ == '__main__':
    unittest.main()
