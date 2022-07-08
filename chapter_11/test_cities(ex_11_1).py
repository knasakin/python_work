# 11.1. Город, страна
import unittest
from city_functions import formatted_city_country


class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        city_country = formatted_city_country('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()
