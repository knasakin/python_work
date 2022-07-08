# 11.2. Население
import unittest
from city_functions import formatted_city_country


class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        city_country = formatted_city_country('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        city_country = formatted_city_country('santiago', 'chile', '5000000')
        self.assertEqual(city_country, 'Santiago, Chile - Population 5000000')


if __name__ == '__main__':
    unittest.main()
