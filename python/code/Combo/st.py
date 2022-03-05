import re

string = "(This is (a) string)"
string = re.sub("[()]","", string)
print(string)

butt = "Luminosity (8143, 4384)"
butt = re.sub("[()]", "", butt)
print(butt)

butt =  re.sub("[,]", "", butt)
print(butt)
