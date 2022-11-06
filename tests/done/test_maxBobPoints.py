# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'
# - pytest .. (if __init__.py exists in tests dir)

import pytest
from probs.maxBobPoints import Solution

@pytest.mark.parametrize(
    'numArrows, aliceArrows, output',
    [
        (9, [1,1,0,1,0,0,2,1,0,1,2,0], [0,0,0,0,1,1,0,0,1,2,3,1]),
        (3, [0,0,1,0,0,0,0,0,0,0,0,2], [0,0,0,0,0,0,0,0,1,1,1,0]),
    ]
)
def testCase(numArrows, aliceArrows, output):
    assert Solution().maximumBobPoints(numArrows, aliceArrows) == output