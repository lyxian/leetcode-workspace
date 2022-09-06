# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'
# - pytest .. (if __init__.py exists in tests dir)

import pytest
from probs import Solution

@pytest.mark.parametrize(
    'ARGUMENTS, output',
    [
        ''
    ]
)
def testCase(ARGUMENTS, output):
    assert Solution().FUNCTION(ARGUMENTS) == output