import re
text = '"title":"请问：平光是谁？","content":"娘搞后来，就被笑话到了现在……"'
title = re.findall(r'"title":"(.*?)"',text)[0]
content = re.findall(r'"content":"(.*?)"', text)[0]
print(f"{title}\n{content}")