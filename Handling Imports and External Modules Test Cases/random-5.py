#esbmc verifies program logic and finds runtime assertion failures. The other 2 tools do not perform this type of check

import random

r:float = random.random()
assert 0.0 <= r < 0.89