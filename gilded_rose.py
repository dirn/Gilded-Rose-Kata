from dataclasses import dataclass


@dataclass
class GildedRose:
    name: str
    quality: int
    days_remaining: int

    def tick(self) -> None:  # NOQA: C901
        if self.name == "normal":
            return self.normal_tick()
        elif self.name == "Aged Brie":
            return self.brie_tick()
        elif self.name == "Sulfuras, Hand of Ragnaros":
            return self.sulfuras_tick()
        elif self.name == "Backstage passes to a TAFKAL80ETC concert":
            return self.backstage_tick()

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

    def brie_tick(self) -> None:
        self.days_remaining -= 1
        if self.quality >= 50:
            return

        self.quality += 1
        if self.days_remaining <= 0:
            self.quality += 1

        self.quality = min(self.quality, 50)

    def sulfuras_tick(self) -> None:
        ...

    def backstage_tick(self) -> None:
        self.days_remaining -= 1
        if self.days_remaining < 0:
            self.quality = 0
            return
        if self.quality >= 50:
            return

        self.quality += 1
        if self.days_remaining < 10:
            self.quality += 1
        if self.days_remaining < 5:
            self.quality += 1

        self.quality = min(self.quality, 50)
