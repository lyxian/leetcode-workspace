# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'
# - pytest .. (if __init__.py exists in tests dir)

import pytest
from probs.concatenateConsecutiveBinary import Solution

@pytest.mark.parametrize(
    'n, output',
    [
        (1, 1),
        (3, 27),
        (12, 505379714),
    ]
)
def testCase(n, output):
    assert Solution().concatenatedBinary(n) == output