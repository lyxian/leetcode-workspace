# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'
# - pytest .. (if __init__.py exists in tests dir)

import pytest
from probs.validParentheses import Solution

@pytest.mark.parametrize(
    's, output',
    [
        ('()[]{}', True),
        ('(]', False),
        ('({}{}', False),
        ('({}{}]', False),
        ('({}{}(', False),
        ('({})[]', True),
        ('({((()))})[]', True),
    ]
)
def testCase(s, output):
    assert Solution().isValid(s) == output