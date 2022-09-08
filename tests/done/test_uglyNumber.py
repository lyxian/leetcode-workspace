# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'
# - pytest .. (if __init__.py exists in tests dir)

import pytest
from probs.uglyNumber import Solution

@pytest.mark.parametrize(
    'n, output',
    [
        (6, True),
        (1, True),
        (30, True),
        (14, False),
        (21, False),
    ]
)
def testCase(n, output):
    assert Solution().isUgly(n) == output