import unittest
from Task_2.ChangeLanguage import ChangeLang

class TestChangeLeng(unittest.TestCase):

    changeleng = ChangeLang(onLeng = 'Русский')

    def test_changeleng(self):
        result = self.changeleng.change_leng()
        self.assertEqual(result[0], 'Русский RU')
        self.assertEqual(result[1][0], 'Криптовалюты')
        self.assertEqual(result[1][1], 'Цена')
        self.assertEqual(result[1][2], '₽')

if __name__ == '__main__':
    unittest.main()
