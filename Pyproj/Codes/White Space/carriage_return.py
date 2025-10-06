import time

for i in range(101):
    print(f"Loading... {i}%", end="")
    time.sleep(1)

#wtih carriage return
    print("\r", end="")

# or 
import time

for i in range(101):
    print(f"\rLoading... {i}%", end="")
    time.sleep(1)