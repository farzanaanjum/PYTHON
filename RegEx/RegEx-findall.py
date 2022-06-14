import re

text = "A boy dancing on the road and a girl also dancing on the road"

txt = re.findall("dancing", text)

print(txt)
