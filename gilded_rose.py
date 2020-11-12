from dataclasses import dataclass


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
class GildedRose:
    name: str
    _quality: int
    _days_remaining: int

    @property
    def quality(self) -> int:
        if hasattr(self, "item"):
            return self.item.quality
        return self._quality

    @quality.setter
    def quality(self, value: int) -> None:
        self._quality = value

    @property
    def days_remaining(self) -> int:
        if hasattr(self, "item"):
            return self.item.days_remaining
        return self._days_remaining

    @days_remaining.setter
    def days_remaining(self, value: int) -> None:
        self._days_remaining = value

    def tick(self) -> None:
        if self.name == "normal":
            return self.normal_tick()
        elif self.name == "Aged Brie":
            return self.brie_tick()
        elif self.name == "Sulfuras, Hand of Ragnaros":
            return self.sulfuras_tick()
        elif self.name == "Backstage passes to a TAFKAL80ETC concert":
            return self.backstage_tick()

    def normal_tick(self) -> None:
        self.item = Normal(self.quality, self.days_remaining)
        return self.item.tick()

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
