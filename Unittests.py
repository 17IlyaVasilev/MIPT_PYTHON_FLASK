import unittest
import main
from app_module import routes, items

class MyTestCase(unittest.TestCase):
    def test_1(self):
        a = False
        for i in items.tp:
            if (i == "SBER"):
                a = True
        self.assertEqual(a, True)

    def test_2(self):
        a = False
        for i in items.tp:
            if (i == "GAZP"):
                a = True
        self.assertEqual(a, True)

    def test_3(self):
        a = False
        for i in items.tp:
            if (i == "TROL"):
                a = True
        self.assertEqual(a, False)

    def test_4(self):
        a = False
        for i in range(len(items.tp)):
            if (items.tp[i] == "SBER"):
                if (items.tp1[i] > 200):
                    a = True
        self.assertEqual(a, True)

    def test_5(self):
        self.assertEqual(items.url_to_scrape, "https://smart-lab.ru/q/shares/")

    def test_6(self):
        self.assertTrue(len(items.st) > 0)
        


if __name__ == '__main__':
    unittest.main()
