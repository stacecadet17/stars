def draw_stars(list):
  for item in list:
    if isinstance(item, int):
      print "*" * item
    else:
      print item[0].lower() * (len(item))


draw_stars([4, 6, 1, 3, 5, 7, 25])
draw_stars([4, "Tom", 7, "Stars", 2])
