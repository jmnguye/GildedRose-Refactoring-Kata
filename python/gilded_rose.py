# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def increase_quality(self, item):
        item.quality = item.quality + 1
        return item.quality

    def decrease_quality(self, item):
        item.quality = item.quality - 1
        return item.quality
   
    def decrease_quality_whenever_quality_is_positive(self, item):
        if item.quality > 0:
            item.quality = self.decrease_quality(item)
        return item.quality


    def increase_quality_whenever_quality_below_50(self, item):
        if item.quality < 50:
            item.quality = self.increase_quality(item)
        return item.quality

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name != "Sulfuras, Hand of Ragnaros":
                item.quality = self.decrease_quality_whenever_quality_is_positive(item)
            else:
                item.quality = self.increase_quality_whenever_quality_below_50(item)

            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in < 11:
                    item.quality = self.increase_quality_whenever_quality_below_50(item)
                if item.sell_in < 6:
                    item.quality = self.increase_quality_whenever_quality_below_50(item)

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1

            if item.sell_in < 0:
                if item.name == "Aged Brie":
                    item.quality = self.increase_quality_whenever_quality_below_50(item)
                else :
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        item.quality = 0
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = self.decrease_quality_whenever_quality_is_positive(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
