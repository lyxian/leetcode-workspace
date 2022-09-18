# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'
# - pytest .. (if __init__.py exists in tests dir)

import pytest
from probs.longestCommonSubsequence import Solution

@pytest.mark.parametrize(
    'text1, text2, output',
    [
        ('abcde', 'ace', 3),
        ('abc', 'abc', 3),
        ('abc', 'def', 0),
        ('abcde', 'qce', 2),
        ('abcde', 'aca', 2),
        ('fweoihbudaoc', 'qwpriufsdnmsad', 5),
        ('ylqpejqbalahwr', 'yrkzavgdmdgtqpg', 3),
    ]
)
def testCase(text1, text2, output):
    assert Solution().longestCommonSubsequenceA(text1, text2) == output