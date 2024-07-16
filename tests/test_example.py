from hexlet_pytest.example import reverse_string


def test_reverse():
    assert reverse_string('Hexlet') == 'telxeH'


def test_reverse_empty():
    assert reverse_string('') == ''
