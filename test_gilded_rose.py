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
        self.assertEquals(4, sulfuras_item.sell_in)
        self.assertEquals("Sulfuras", sulfuras_item.name)


    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEquals(["Sulfuras"], all_items)


    def test_aged_grie_should_not_decrease_quality(self):
        items = [Item("Aged Brie", 10, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        aged_brie_item = items[0]
        self.assertEquals(29, aged_brie_item.quality)
        self.assertEquals(4, aged_brie_item.sell_in)
        self.assertEquals("Aged Brie", aged_brie_item.name)
        
    def test_quality_should_decrease_buy_two_if_sell_by_date_has_passed(self):
        items = [Item("Baby Seat", -1, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        baby_seat_item = items[0]
        self.assertEquals(29, baby_seat_item.quality)
        self.assertEquals(-2, baby_seat_item.sell_in)
        self.assertEquals("Baby Seat", baby_seat_item.name)
        
    def test_quality_never_be_negative(self):
        items = [Item("Mug", -1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        mug_item = items[0]
        self.assertEquals(-1, mug_item.quality)
        self.assertEquals(-2, mug_item.sell_in)
        self.assertEquals("Mug", mug_item.name)

    # example of test that checks for syntax errors
    def test_update_sell_date(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        updated_sell_date = gilded_rose.update_sell_date()
        self.assertEquals(4, updated_sell_date)

if __name__ == '__main__':
    unittest.main()
