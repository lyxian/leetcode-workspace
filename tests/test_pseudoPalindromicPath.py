# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'
# - pytest .. (if __init__.py exists in tests dir)

import pytest
from probs.pseudoPalindromicPath import Solution

@pytest.mark.parametrize(
    'root, output',
    [
        ([2,3,1], 0),
        ([2,3,1,3,1,None,1], 2),
        ([2,1,1,1,3,None,None,None,None,None,1], 1),
        ([9], 1),
        ([1,9,1,None,1,None,1,None,None,7,None,None,4], 1),
    ]
)
def testCase(root, output):
    assert Solution().pseudoPalindromicPaths(root) == output