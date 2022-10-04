
# "" -> 0
# "0" -> 0
# "1,1" -> 2
# "2,10" -> 12
# "1,4,1" -> 6
# "1,2,3" -> 6



def Add(a: str) -> int:
  if a is None or a == "":
    return 0
  if "," in a:
    tokens = a.split(',')
    return int(tokens[0])+ int(tokens[1])
  return int(a)