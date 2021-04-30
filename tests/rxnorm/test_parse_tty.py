import pytest
from phdata.rxnorm import parseTTY


test_data = [
    (
        ['SCD'],
        [
            {'tty': 'SCD', 'conceptProperties': [{'rxcui': 1}, {'rxcui': 2}]},
            {'tty': 'IN', 'conceptProperties': [{'rxcui': 3}, {'rxcui': 4}]}
        ],
        [{'rxcui': 1}, {'rxcui': 2}]
    ),
    (
        ['SCD', 'IN'],
        [
            {'tty': 'SCD', 'conceptProperties': [{'rxcui': 1}, {'rxcui': 2}]},
            {'tty': 'IN', 'conceptProperties': [{'rxcui': 3}, {'rxcui': 4}]}
        ],
        [{'rxcui': 1}, {'rxcui': 2}, {'rxcui': 3}, {'rxcui': 4}]
    ),
]


@pytest.mark.parametrize('tty_list,concept_groups,expected', test_data)
def test_parse_tty(tty_list, concept_groups, expected):
    result = parseTTY(tty_list, concept_groups)
    assert result == expected
