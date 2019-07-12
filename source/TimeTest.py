import time

str_time = time.time()
time.sleep(10)
end_time = time.time()

print(round(int(end_time-str_time)))