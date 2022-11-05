# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'
# - pytest .. (if __init__.py exists in tests dir)

import pytest
from probs.rotateList import Solution

@pytest.mark.parametrize(
    'head, k, output',
    [
        ''
    ]
)
def testCase(head, k, output):
    assert Solution().rotateRight(head, k) == output