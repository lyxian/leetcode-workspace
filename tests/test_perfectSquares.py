# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'
# - pytest .. (if __init__.py exists in tests dir)

import pytest
from probs.perfectSquares import Solution

@pytest.mark.parametrize(
    'n, output',
    [
        (12, 3),
        (13, 2),
        (43, 3),
        (7168, 4),
        (10000, 1),
    ]
)
def testCase(n, output):
    assert Solution().numSquares(n) == output