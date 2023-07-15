print("30 Days Down - What did you think?")
print()
for i in range(1, 31):
  # very important promt (digest and take it 1 day more of study)
  thought = input(f"Day {i}:\n")
  print()
  myText = f"You thought Day {i} was"
  print(f"{myText:^35}")
  print(f"{thought:^35}")
  print()