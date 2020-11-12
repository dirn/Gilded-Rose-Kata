from dataclasses import dataclass
from typing import Type, Union


@dataclass
class Normal:
    quality: int
    days_remaining: int

    def tick(self) -> None:
        self.days_remaining -= 1
        if self.quality == 0:
            return

        self.quality -= 1
        if self.days_remaining <= 0:
            self.quality -= 1


@dataclass
class Brie:
    quality: int
    days_remaining: int

    def tick(self) -> None:
        self.days_remaining -= 1
        if self.quality >= 50:
            return

        self.quality += 1
        if self.days_remaining <= 0:
            self.quality += 1

        self.quality = min(self.quality, 50)


@dataclass
class Sulfuras:
    quality: int
    days_remaining: int

    def tick(self) -> None:
        ...


@dataclass
class Backstage:
    quality: int
    days_remaining: int

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


class GildedRose:
    def __init__(self, name: str, quality: int, days_remaining: int) -> None:
        self.name = name
        self.item = self.class_for(name)(quality, days_remaining)

    @property
    def quality(self) -> int:
        return self.item.quality

    @property
    def days_remaining(self) -> int:
        return self.item.days_remaining

    def tick(self) -> None:
        return self.item.tick()

    def class_for(self, name: str) -> Type[Union[Normal, Brie, Sulfuras, Backstage]]:
        if self.name == "normal":
            return Normal
        elif self.name == "Aged Brie":
            return Brie
        elif self.name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras
        elif self.name == "Backstage passes to a TAFKAL80ETC concert":
            return Backstage
        else:
            # This mostly exists to make mypy happy due to an otherwise
            # missing return.
            raise ValueError(f"{name} is not a valid item type")
