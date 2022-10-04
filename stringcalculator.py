
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
    total = 0
    for token in tokens:
      total = total + int(token)
    return total
  return int(a)