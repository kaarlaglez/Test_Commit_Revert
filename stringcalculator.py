
# "" -> 0
# "0" -> 0
# "1,1" -> 2
# "2,10" -> 12



def Add(a: str) -> int:
  if a is None or a == "":
    return 0
  return int(a)