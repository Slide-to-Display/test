import GetStateList


def test_GetStateList():
    expected = [('worldwide\n', 'Worldwide\n'), ('eur', 'EUR'),
                ('azn ', 'AZN '), ('jpn', 'JPN')]
    assert GetStateList.GetStateList().__str__() in expected.__str__()


def test_GetStateList1():
    expected = [('worldwide\n', 'Worldwide\n'), ('eur', 'EUR'),
                ('azn ', 'AZN '), ('jpn', 'JPN')]
    assert GetStateList.GetStateList1(
        "state_list").__str__() in expected.__str__()
