import unittest
import datetime

from Task_1.GetApi import GetAPI


class TestGetAPI(unittest.TestCase):

    getapi = GetAPI(url="https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",
                apikey='b0043f38-f970-404c-95f4-935f571a521c')

    def test_getapi_functional(self):
        result = self.getapi.get_api()
        date_json = datetime.datetime.strptime(result[1], "%Y-%m-%dT%H:%M:%S.%fZ")

        self.assertEqual(result[0], 200)
        self.assertEqual(date_json.date(), datetime.datetime.today().date())
        self.assertLessEqual(result[2], 10000)
        self.assertLessEqual(result[3], 0.5)



if __name__ == '__main__':
    unittest.main()
