# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'
# - pytest .. (if __init__.py exists in tests dir)

import pytest
from probs.letterCombinations import Solution

@pytest.mark.parametrize(
    'digits, output',
    [
        ('23', ['ad','ae','af','bd','be','bf','cd','ce','cf']),
        ('', []),
        ('2', ['a','b','c']),
    ]
)
def testCase(digits, output):
    assert Solution().letterCombinations(digits) == output