import time

minutes = int(input("Enter The Number Of Minutes To Focus:"))
seconds = minutes *60
while seconds:
  mins,secs = divmod(seconds,60)
  timer = '{:02d}:{:02d}'.format(mins,secs)
  print(timer,end="\r")
  seconds -=1
  
  print("Time's up!")
