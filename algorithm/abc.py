#求在1000以内有a^2+b^2=c^的a,b,c
#1701.608326435089
import time

start_time = time.time()
for a in range(1001):
    for b in range(1001):
        c = 1000 - a -b
        if a**2+b**2==c**2:
            print(a, b, c)
end_time = time.time()

print("%d" % (end_time - start_time))


print("finished")

