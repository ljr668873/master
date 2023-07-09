#!/usr/bin/python3
import psutil
import matplotlib.pyplot as plt
import time
import sys
import matplotlib.dates as mdates

def plot_process_stats(pid, duration,sampler_interval):
    cpu_data = []
    mem_data = []
    timestamps = []

    end_time = time.time() + duration

    while time.time() < end_time:
        process = psutil.Process(pid)
        cpu_percent = process.cpu_percent(interval=1)
        mem_info = process.memory_info()
        mem_usage = mem_info.rss
        timestamp = time.strftime('%H:%M', time.localtime())

        cpu_data.append(cpu_percent)
        mem_data.append(mem_usage)
        timestamps.append(timestamp)
        time.sleep(sampler_interval)
    fig, ax1 = plt.subplots()
    ax1.plot(timestamps, cpu_data, 'b-')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('CPU Usage (%)', color='b')
    ax1.tick_params('y', colors='b')
    ax1.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax2 = ax1.twinx()
    mem_data_hr = [psutil._common.bytes2human(mem) for mem in mem_data]  # 转换为人类可读的内存单位
    ax2.plot(timestamps, mem_data_hr, 'r-')
    ax2.set_ylabel('Memory Usage', color='r')
    ax2.tick_params('y', colors='r')
    ax2.xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.title('Process CPU and Memory Usage')
    plt.xticks(rotation=-60)
    plt.tight_layout()
    plt.savefig('monitor_cpu_memery{}.png'.format(int(time.time())))

# 定义输入参数
if len(sys.argv) < 4:
    print("请输入必要参数pid和持续时间,采集间隔(单位s)")
    sys.exit(1)

# 用法示例
process_pid = int(sys.argv[1])  # 替换为你要监视的进程的实际PID
monitor_duration = int(sys.argv[2])  # 监听持续时间（秒）
sampler_interval = int(sys.argv[3]) # 采集间隔
plot_process_stats(process_pid, monitor_duration,sampler_interval)
