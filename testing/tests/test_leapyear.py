from testing.project.leapyear import is_leap_year


def test_leap_years_dividable_by_4_but_not_100():
    leap_years = [1776, 1848, 1944, 1984]
    for year in leap_years:
        assert is_leap_year(year)


def test_leap_years_dividable_by_400():
    leap_years = [2000, 2400, 1600]
    for year in leap_years:
        assert is_leap_year(year)


def test_years_not_dividable_by_4_are_not_leap_years():
    non_leap_years = [1903, 1905, 2019, 1999]
    for year in non_leap_years:
        assert not is_leap_year(year)


def test_years_dividable_by_100_but_not_400_are_not_leap_years():
    non_leap_years = [1700, 1800, 1900, 2100]
    for year in non_leap_years:
        assert not is_leap_year(year)
