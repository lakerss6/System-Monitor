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
