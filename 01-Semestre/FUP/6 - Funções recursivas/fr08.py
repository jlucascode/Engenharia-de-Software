def SomaSerie(i, j, k):
  if i > j:
    return 0
  else:
    return i + SomaSerie(i + k, j, k)
