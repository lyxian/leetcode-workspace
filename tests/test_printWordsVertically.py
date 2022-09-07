# RUN
# - python -m pytest -p no:cacheprovider tests -sv --ignore tests/done
# - python -m pytest -p no:cacheprovider tests -sv -k 'not tests/done'
# - pytest .. (if __init__.py exists in tests dir)

import pytest
from probs.printWordsVertically import Solution

@pytest.mark.parametrize(
    's, output',
    [
        ('HOW ARE YOU', ['HAY','ORO','WEU']),
        ('TO BE OR NOT TO BE', ['TBONTB','OEROOE','   T']),
        ('I AM BAD', ['IAB',' MA','  D']),
        ('BAD AM I', ['BAI','AM','D']),
        ("CONTEST IS COMING", ["CIC","OSO","N M","T I","E N","S G","T"]),
    ]
)
def testCase(s, output):
    assert Solution().printVertically(s) == output