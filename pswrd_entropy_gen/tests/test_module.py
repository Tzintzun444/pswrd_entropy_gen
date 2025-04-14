import pytest
from src.pswrd_entropy_gen.generator import Generator


@pytest.mark.parametrize("length, use_uppercase, use_numbers, use_punctuations",
                         [
                             (12, True, True, True),
                             (-1, True, False, False),
                             (0, True, True, False),
                             (17, False, False, False),
                             ('Hello',),
                             (12, 'hello', 'hello', 'hello')
                         ])
def test_generate_password(length, use_uppercase=True,
                           use_numbers=True, use_punctuations=True):

    test_case = Generator.generate_password(length, use_uppercase=use_uppercase,
                                            use_numbers=use_numbers,
                                            use_punctuations=use_punctuations)
    length_expected = len(length)
    type_expected = str

    assert len(test_case) == length_expected
    assert test_case is str
