# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'
# - pytest .. (if __init__.py exists in tests dir)

import pytest
from probs.countPrimes import Solution

@pytest.mark.parametrize(
    'n, output',
    [
        (10, 4),
        (20, 8),
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 1),
        (4, 2),
        (5, 2),
        (499979, 41537),
        (5000000, 348513),
    ]
)
def testCase(n, output):
    assert Solution().countPrimesA(n) == output