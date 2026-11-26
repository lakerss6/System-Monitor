import psutil

# print(psutil.cpu_times())
# print(psutil.cpu_stats())
cpuusage = psutil.cpu_percent(interval=1,percpu=True)
total = 0
for i in cpuusage:
    total += i
newusage = total / len(cpuusage)


# print(psutil.cpu_count())
# print(psutil.cpu_freq())

print("==== SYSTEM RESOURCE MONITOR ====")

print(f"Total CPU Usage: {newusage:.2f}%")
for i,usage in enumerate(cpuusage):
    print(f"CPU {i}: {usage:2f}")

print("==== MEMORY INFORMATION ====")
total_bytes = psutil.virtual_memory().total
total_gib = total_bytes / (1024 ** 3)
print(f"Total RAM: {total_gib}")
print(f"Available RAM: {psutil.virtual_memory().available / (1024 ** 3)}")
memory = (psutil.virtual_memory().total - psutil.virtual_memory().available) / psutil.virtual_memory().total * 100
print(f"Memory Usage: {memory}")



