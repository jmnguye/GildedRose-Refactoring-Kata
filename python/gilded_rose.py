# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def increase_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

    def decrease_quality(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1

    def decrease_sell_in(self, item):
        item.sell_in = item.sell_in - 1

    def update_quality(self):

        for item in self.items:

            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.increase_quality(item)
                if item.sell_in < 11:
                    self.increase_quality(item)
                if item.sell_in < 6:
                    self.increase_quality(item)
                self.decrease_sell_in(item)
                if item.sell_in < 0:
                    item.quality = 0
                continue

            if item.name == "Aged Brie": 
                self.increase_quality(item)
                self.decrease_sell_in(item)
                if item.sell_in < 0:
                    self.increase_quality(item)
                continue

            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            self.decrease_quality(item)
            self.decrease_sell_in(item)
            if item.sell_in < 0:
                self.decrease_quality(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Sellable():
    def __init__(self, item):
        self.name = item.name
        self.sell_in = item.sell_in
        self.quality = item.quality


    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

if __name__ == "__main__":
    print ("OMGHAI!")
    items = [
             Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
             Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ]

    days = 31
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()
