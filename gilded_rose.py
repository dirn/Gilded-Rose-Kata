from dataclasses import dataclass


@dataclass
class GildedRose:
    name: str
    quality: int
    days_remaining: int

    def tick(self) -> None:
        if self.name == "normal":
            return self.normal_tick()

        if (
            self.name != "Aged Brie"
            and self.name != "Backstage passes to a TAFKAL80ETC concert"
        ):
            if self.quality > 0:
                if self.name != "Sulfuras, Hand of Ragnaros":
                    self.quality -= 1
        else:
            if self.quality < 50:
                self.quality += 1
                if self.name == "Backstage passes to a TAFKAL80ETC concert":
                    if self.days_remaining < 11:
                        if self.quality < 50:
                            self.quality += 1
                    if self.days_remaining < 6:
                        if self.quality < 50:
                            self.quality += 1
        if self.name != "Sulfuras, Hand of Ragnaros":
            self.days_remaining -= 1
        if self.days_remaining < 0:
            if self.name != "Aged Brie":
                if self.name != "Backstage passes to a TAFKAL80ETC concert":
                    if self.quality > 0:
                        if self.name != "Sulfuras, Hand of Ragnaros":
                            self.quality -= 1
                else:
                    self.quality = self.quality - self.quality
            else:
                if self.quality < 50:
                    self.quality += 1

    def normal_tick(self) -> None:
        self.days_remaining -= 1
        if self.quality == 0:
            return

        self.quality -= 1
        if self.days_remaining <= 0:
            self.quality -= 1
