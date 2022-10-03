# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'
# - pytest .. (if __init__.py exists in tests dir)

import pytest
from probs.maxPointsWithCost import Solution

@pytest.mark.parametrize(
    'points, output',
    [
        ([[1,2,3],[1,5,1],[3,1,1]], 9),
        ([[1,5],[2,3],[4,2]], 11),
    ]
)
def testCase(points, output):
    assert Solution().maxPoints(points) == output