# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'

import pytest
from probs.movePiecesToObtainString import Solution

@pytest.mark.parametrize(
    'start, target, output',
    [
        ('_L__R__R_', 'L______RR', True),
        ('R_L_', '__LR', False),
        ('LR__', '__LR', False),
        ('_R', 'R_', False),
    ]
)
def testCase(start, target, output):
    assert Solution().canChange(start, target) == output