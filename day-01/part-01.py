file = open('day-01/input.txt')

calibration_sum = 0

for line in file:
  calibration = []
  for char in line:
    if (char.isdigit()):
      calibration.append(char)
    
  
  calibration_sum += int(calibration[0] + calibration[-1])

print(calibration_sum)