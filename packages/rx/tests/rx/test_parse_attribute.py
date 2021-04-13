import pytest
from rx.core import parseAttribute

test_data = [
    ('testkey', [{'testkey': 1}, {'testkey': 2}], [1,2])
]


@pytest.mark.parametrize('key,obj_list,expected', test_data)
def test_parse_attribute(key, obj_list, expected):
    result = parseAttribute('testkey', obj_list)
    assert result == expected
