# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()


class Item:

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Sellable(Item):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def increase_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1

    def decrease_quality(self):
        if self.quality > 0:
            self.quality = self.quality - 1

    def decrease_sell_in(self):
        self.sell_in = self.sell_in - 1

    def update_quality(self):
        self.decrease_quality()
        self.decrease_sell_in()
        if self.sell_in < 0:
            self.decrease_quality()


class AgedBrie(Sellable):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
            self.increase_quality()
            self.decrease_sell_in()
            if self.sell_in < 0:
                self.increase_quality()


class Sulfuras(Sellable):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        pass


class BackstagePasses(Sellable):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
            self.increase_quality()
            if self.sell_in < 11:
                self.increase_quality()
            if self.sell_in < 6:
                self.increase_quality()
            self.decrease_sell_in()
            if self.sell_in < 0:
                self.quality = 0
