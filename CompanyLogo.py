# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# from collections import Counter, OrderedDict

# class OrderedCounter(Counter, OrderedDict):
#     pass
# [print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]
#-------------------------------------------------------------------------------
import math
import os
import random
import re
import sys

from collections import Counter, OrderedDict
if __name__ == '__main__':
    s = sorted(input())
    z=Counter(s).most_common(3)
    for i in z:
        print(*i)