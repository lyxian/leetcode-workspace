# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'
# - pytest .. (if __init__.py exists in tests dir)

import pytest
from probs.countAndSay import Solution

@pytest.mark.parametrize(
    'n, output',
    [
        (1, '1'),
        (2, '11'),
        (3, '21'),
        (4, '1211'),
        (5, '111221'),
    ]
)
def testCase(n, output):
    assert Solution().countAndSay(n) == output