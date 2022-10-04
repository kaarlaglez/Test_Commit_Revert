

# "" -> 0



def Add(a: str) -> int:
  if a is None or a == "":
    return 0
  return int(a)