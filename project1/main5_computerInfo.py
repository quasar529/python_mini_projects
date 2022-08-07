from tkinter import CURRENT
import psutil
cpu = psutil.cpu_freq()
cpu_current_ghz = round(cpu.current / 1000, 2)
print(f"cpu 속도 : {cpu_current_ghz}GHZ")

cpu_core = psutil.cpu_count(logical=False)
print(cpu_core)

memory = psutil.virtual_memory()
memory_total = round(memory.total/1024**3)
print(f'메모리: {memory_total}GB')

disk = psutil.disk_partitions()
print(disk)

net = psutil.net_io_counters()
print(net)
