s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

import re
otpt = [len(s_) for s_ in re.split(r'\s|"|,|\.', s)]

print(''.join(map(str, otpt)))