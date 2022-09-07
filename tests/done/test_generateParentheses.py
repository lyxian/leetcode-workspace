# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'
# - pytest .. (if __init__.py exists in tests dir)

import pytest
from probs.generateParentheses import Solution

@pytest.mark.parametrize(
    'n, output',
    [
        (1, ['()']),
        (2, ['(())', '()()']),
        (3, ['((()))','(()())','(())()','()(())','()()()']),
    ]
)
def testCase(n, output):
    assert Solution().generateParenthesis(n) == output