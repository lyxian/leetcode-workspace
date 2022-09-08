# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'
# - pytest .. (if __init__.py exists in tests dir)

import pytest
from probs.selfDividingNumbers import Solution

@pytest.mark.parametrize(
    'left, right, output',
    [
        (1, 22, [1,2,3,4,5,6,7,8,9,11,12,15,22]),
        (47, 85, [48,55,66,77]),
    ]
)
def testCase(left, right, output):
    assert Solution().selfDividingNumbers(left, right) == output