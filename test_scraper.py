import unittest

from scraper import ScrapeMercariUS

class TestScraper(unittest.TestCase):
  def test_mercari_us_available(self):
    result = ScrapeMercariUS("https://www.mercari.com/us/item/m58954708338/")
    self.assertEqual(result['name'], "Jeongin I.N miroh photocard")
    self.assertEqual(result['price'], "$4.00")
    self.assertEqual(result['status'], "available")
  
  def test_mercari_us_sold(self):
    result = ScrapeMercariUS("https://www.mercari.com/us/item/m16149129305/")
    self.assertEqual(result['name'], "rock star postcard pob photocard - hyunjin")
    self.assertEqual(result['price'], "$6.32")
    self.assertEqual(result['status'], "unavailable")

unittest.main()