# Name:GOBIKA NANTHINI MK

# ROLL NO:IIP_AIMLTN_2602829

# Assignment: Python Loops & Automation - Subjective Question



print("===== Task 1: Find Maximum and Minimum =====")

temperature = [28, 32, 35, 29, 31, 27, 30]

high=temperature[0]

low=temperature[0]

for i in temperature:

  if i>high:

    high=i

  if i<low:

    low=i

     

print("Highest Temperature:", high, "°C")

print("Lowest Temperature:", low, "°C"





print("\n===== Task 2: Count Hot Days =====")

temperatures = [28, 32, 35, 29, 31, 27, 30]

hot_days=0 

for i in temperatures:

  if i >= 30:

    continue

  hot_days+=1 

print("Hot Days (>30°C):", hot_days)





print("\n===== Task 3: Alert System =====")

temperatures = [28, 32, 35, 40, 31, 33, 30]

hot_days = 0

for i in range(len(temperatures)):

  temp = temperatures[i]

  if temp > 30:

    hot_days += 1

   

  if temp >= 40:

    print("Hot Days before alert:", hot_days)

    print(f"Alert! Extreme temperature {temp}°C detected on Day {i + 1}")

    break

