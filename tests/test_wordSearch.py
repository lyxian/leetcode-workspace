# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'
# - pytest .. (if __init__.py exists in tests dir)

import pytest
from probs.wordSearch import Solution

@pytest.mark.parametrize(
    'board, word, output',
    [
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False),
        ([["A"]], "A", True),
        ([["a","b"],["c","d"]], "cdba", True),
    ]
)
def testCase(board, word, output):
    assert Solution().exist(board, word) == output