import time

frames = ["|", "/", "-", "\\"]
for i in range(20):
    print(f"\r{frames[i % 4]} Processing", end="")
    time.sleep(0.2)
print("\nDone!")
