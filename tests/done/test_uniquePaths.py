# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'
# - pytest .. (if __init__.py exists in tests dir)

import pytest
from probs.uniquePaths import Solution

@pytest.mark.parametrize(
    'm, n, output',
    [
        (1, 3, 1),
        (3, 1, 1),
        (3, 7, 28),
        (3, 2, 3),
        (3, 3, 6),
        (3, 5, 15),
    ]
)
def testCase(m, n, output):
    assert Solution().uniquePaths(m, n) == output