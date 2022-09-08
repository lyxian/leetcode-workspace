# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'
# - pytest .. (if __init__.py exists in tests dir)

import pytest
from probs.nTribonacciNumber import Solution

@pytest.mark.parametrize(
    'n, output',
    [
        (4, 4),
        (25, 1389537),
        (35, 615693474),
    ]
)
def testCase(n, output):
    assert Solution().tribonacci(n) == output