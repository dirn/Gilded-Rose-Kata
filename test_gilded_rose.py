import pytest

from gilded_rose import GildedRose


def test_normal_item_before_sell_date() -> None:
    item = GildedRose("normal", 10, 5)
    item.tick()

    assert item.quality == 9
    assert item.days_remaining == 4


def test_normal_item_on_sell_date() -> None:
    item = GildedRose("normal", 10, 0)
    item.tick()

    assert item.quality == 8
    assert item.days_remaining == -1


def test_normal_item_after_sell_date() -> None:
    item = GildedRose("normal", 10, -1)
    item.tick()

    assert item.quality == 8
    assert item.days_remaining == -2


def test_normal_item_of_zero_quality() -> None:
    item = GildedRose("normal", 0, 5)
    item.tick()

    assert item.quality == 0
    assert item.days_remaining == 4


def test_brie_before_sell_date() -> None:
    item = GildedRose("Aged Brie", 10, 5)
    item.tick()

    assert item.quality == 11
    assert item.days_remaining == 4


def test_brie_before_sell_date_with_max_quality() -> None:
    item = GildedRose("Aged Brie", 50, 10)
    item.tick()

    assert item.quality == 50
    assert item.days_remaining == 9


def test_brie_on_sell_date() -> None:
    item = GildedRose("Aged Brie", 10, 0)
    item.tick()

    assert item.quality == 12
    assert item.days_remaining == -1


def test_brie_on_sell_date_near_max_quality() -> None:
    item = GildedRose("Aged Brie", 49, 0)
    item.tick()

    assert item.quality == 50
    assert item.days_remaining == -1


def test_brie_on_sell_date_with_max_quality() -> None:
    item = GildedRose("Aged Brie", 50, 0)
    item.tick()

    assert item.quality == 50
    assert item.days_remaining == -1


def test_brie_after_sell_date() -> None:
    item = GildedRose("Aged Brie", 10, -1)
    item.tick()

    assert item.quality == 12
    assert item.days_remaining == -2


def test_brie_after_sell_date_with_max_quality() -> None:
    item = GildedRose("Aged Brie", 50, -1)
    item.tick()

    assert item.quality == 50
    assert item.days_remaining == -2


def test_sulfuras_before_sell_date() -> None:
    item = GildedRose("Sulfuras, Hand of Ragnaros", 10, 5)
    item.tick()

    assert item.quality == 10
    assert item.days_remaining == 5


def test_sulfuras_on_sell_date() -> None:
    item = GildedRose("Sulfuras, Hand of Ragnaros", 10, 0)
    item.tick()

    assert item.quality == 10
    assert item.days_remaining == 0


def test_suluras_item_after_sell_date() -> None:
    item = GildedRose("Sulfuras, Hand of Ragnaros", 10, -1)
    item.tick()

    assert item.quality == 10
    assert item.days_remaining == -1


def test_backstage_pass_long_before_sell_date() -> None:
    item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 10, 11)
    item.tick()

    assert item.quality == 11
    assert item.days_remaining == 10


def test_backstage_pass_medium_close_to_sell_date_upper_bound() -> None:
    item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 10, 10)
    item.tick()

    assert item.quality == 12
    assert item.days_remaining == 9


def test_backstage_pass_medium_close_to_sell_date_upper_bound_at_max_quality() -> None:
    item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 50, 10)
    item.tick()

    assert item.quality == 50
    assert item.days_remaining == 9


def test_backstage_pass_medium_close_to_sell_date_lower_bound() -> None:
    item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 10, 6)
    item.tick()

    assert item.quality == 12
    assert item.days_remaining == 5


def test_backstage_pass_medium_close_to_sell_date_lower_bound_at_max_quality() -> None:
    item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 50, 6)
    item.tick()

    assert item.quality == 50
    assert item.days_remaining == 5


def test_backstage_pass_very_close_to_sell_date_upper_bound() -> None:
    item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 10, 5)
    item.tick()

    assert item.quality == 13
    assert item.days_remaining == 4


def test_backstage_pass_very_close_to_sell_date_upper_bound_at_max_quality() -> None:
    item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 50, 5)
    item.tick()

    assert item.quality == 50
    assert item.days_remaining == 4


def test_backstage_pass_very_close_to_sell_date_lower_bound() -> None:
    item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 10, 1)
    item.tick()

    assert item.quality == 13
    assert item.days_remaining == 0


def test_backstage_pass_very_close_to_sell_date_lower_bound_at_max_quality() -> None:
    item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 50, 1)
    item.tick()

    assert item.quality == 50
    assert item.days_remaining == 0


def test_backstage_pass_on_sell_date() -> None:
    item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 10, 0)
    item.tick()

    assert item.quality == 0
    assert item.days_remaining == -1


def test_backstage_pass_after_sell_date() -> None:
    item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 10, -1)
    item.tick()

    assert item.quality == 0
    assert item.days_remaining == -2


@pytest.mark.skip()
def test_conjured_item_before_sell_date() -> None:
    item = GildedRose("Conjured Mana Cake", 10, 5)
    item.tick()

    assert item.quality == 8
    assert item.days_remaining == 4


@pytest.mark.skip()
def test_conjured_item_at_zero_quality() -> None:
    item = GildedRose("Conjured Mana Cake", 0, 5)
    item.tick()

    assert item.quality == 0
    assert item.days_remaining == 4


@pytest.mark.skip()
def test_conjured_item_on_sell_date() -> None:
    item = GildedRose("Conjured Mana Cake", 10, 0)
    item.tick()

    assert item.quality == 6
    assert item.days_remaining == -1


@pytest.mark.skip()
def test_conjured_item_on_sell_date_at_zero_quality() -> None:
    item = GildedRose("Conjured Mana Cake", 0, 0)
    item.tick()

    assert item.quality == 0
    assert item.days_remaining == -1


@pytest.mark.skip()
def test_conjured_item_after_sell_date() -> None:
    item = GildedRose("Conjured Mana Cake", 10, -1)
    item.tick()

    assert item.quality == 6
    assert item.days_remaining == -2


@pytest.mark.skip()
def test_conjured_item_after_sell_date_at_zero_quality() -> None:
    item = GildedRose("Conjured Mana Cake", 0, -1)
    item.tick()

    assert item.quality == 0
    assert item.days_remaining == -2
