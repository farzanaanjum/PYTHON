# Split the String

import re

string = "A boy dancing on the road and a girl also dancing on the road"

str = re.split("\s", string)

print(str)



# Split the string at the first white-space character:

stirng = "A boy dancing on the road and a girl also dancing on the road"

str = re.split("\s", string, 1)

print(str)                
