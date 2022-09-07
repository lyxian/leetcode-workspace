# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'
# - pytest .. (if __init__.py exists in tests dir)

import pytest
from probs.mostWaterContainer import Solution

@pytest.mark.parametrize(
    'height, output',
    [
        ([1,8,6,2,5,4,8,3,7], 49),
        ([1,1], 1),
        ([3,1,3,2,2,2,2], 12),
    ]
)
def testCase(height, output):
    assert Solution().maxArea(height) == output