# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEquals(80, sulfuras_item.quality)
        self.assertEquals(5, sulfuras_item.sell_in)
        self.assertEquals("Sulfuras", sulfuras_item.name)


    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEquals(["Sulfuras"], all_items)

    def test_conjured_item_quality_should_drop_twice_as_fast_as_normal_item(self):
        items = [Item("Conjured", 5, 35)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        conjured_item = items[0]
        self.assertEquals(33, conjured_item.quality)

    def test_backstage_passes_quality_should_drops_to_zero_after_concert(self):
        items = [Item("Backstage passes", 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        backstage_passes_item = items[0]
        self.assertEquals(0, backstage_passes_item.quality)
        self.assertEquals(-1, backstage_passes_item.sell_in)
        self.assertEquals("Backstage passes", backstage_passes_item.name)
        
    def test_aged_grie_quality_should_not_increase_by_two_if_sell_by_date_has_passed(self):
        items = [Item("Aged Brie", -1, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        aged_brie_item = items[0]
        self.assertEquals(31, aged_brie_item.quality)
        self.assertEquals(-2, aged_brie_item.sell_in)
        self.assertEquals("Aged Brie", aged_brie_item.name)
        
    def test_aged_grie_should_only_increase_by_1(self):
        items = [Item("Aged Brie", 0, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        aged_brie_item = items[0]
        self.assertEquals(2, aged_brie_item.quality)
        self.assertEquals(-1, aged_brie_item.sell_in)
        self.assertEquals("Aged Brie", aged_brie_item.name)


    # example of test that checks for syntax errors
    def test_apply_discount(self):
        items = [Item("Sulfuras", 5, 20)]
        gilded_rose = GildedRose(items)
        sulfuras_item = gilded_rose.apply_discount()[0]
        self.assertEquals(16, sulfuras_item.quality)

if __name__ == '__main__':
    unittest.main()
