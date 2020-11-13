from dataclasses import dataclass


@dataclass
class Item:
    quality: int
    days_remaining: int

    def tick(self) -> None:
        ...


class Normal(Item):
    def tick(self) -> None:
        self.days_remaining -= 1
        if self.quality == 0:
            return

        self.quality -= 1
        if self.days_remaining <= 0:
            self.quality -= 1


class Brie(Item):
    def tick(self) -> None:
        self.days_remaining -= 1
        if self.quality >= 50:
            return

        self.quality += 1
        if self.days_remaining <= 0:
            self.quality += 1

        self.quality = min(self.quality, 50)


class Backstage(Item):
    def tick(self) -> None:
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


class Conjured(Item):
    def tick(self) -> None:
        self.days_remaining -= 1
        if self.quality == 0:
            return

        self.quality -= 2
        if self.days_remaining <= 0:
            self.quality -= 2


DEFAULT_CLASS = Item
SPECIALIZED_CLASSES = {
    "normal": Normal,
    "Aged Brie": Brie,
    "Backstage passes to a TAFKAL80ETC concert": Backstage,
    "Conjured Mana Cake": Conjured,
}


class GildedRose:
    def __init__(self, name: str, quality: int, days_remaining: int) -> None:
        self.name = name
        self.item = SPECIALIZED_CLASSES.get(name, DEFAULT_CLASS)(
            quality, days_remaining
        )

    @property
    def quality(self) -> int:
        return self.item.quality

    @property
    def days_remaining(self) -> int:
        return self.item.days_remaining

    def tick(self) -> None:
        return self.item.tick()
