# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'
# - pytest .. (if __init__.py exists in tests dir)

import pytest
from probs.minSwapSort import Solution

@pytest.mark.parametrize(
    'nums, output',
    [
        ([2, 8, 5, 4], 1),
        ([10, 19, 6, 3, 5], 2),
        ([10, 19, 6, 3, 5, 1], 5),
        ([34, 15, 24, 95, 59, 99, 40, 11, 54, 23, 79, 5], 8),
    ]
)
def testCase(nums, output):
    assert Solution().minimumSwaps(nums) == output