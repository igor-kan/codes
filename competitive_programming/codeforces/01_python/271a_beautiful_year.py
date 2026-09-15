"""Codeforces 271A - Beautiful Year."""
def beautiful_year(year):
    while True:
        year += 1
        if len(set(str(year))) == 4:
            return year


if __name__ == "__main__":
    assert beautiful_year(1987) == 2013
    assert beautiful_year(2013) == 2014
    print("271A beautiful year ok")
