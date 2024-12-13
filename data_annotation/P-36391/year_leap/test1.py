def is_leap_year(year):
    """
    Determines if a given year is a leap year.

    Args:
        year: An integer representing the year.

    Returns:
        True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# Example usage:
years_to_test = [1900, 2000, 2020, 2023, 2024]
for year in years_to_test:
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


# A more concise version:
def is_leap_year_concise(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


print("\nTesting concise function:")
for year in years_to_test:
    if is_leap_year_concise(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
