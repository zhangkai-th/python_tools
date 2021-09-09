import psutil
import platform
import time
import os
import win32api,win32con
def get_os_start_time():
    up_time=psutil.boot_time()
    os_up_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(up_time))
    return os_up_time
def get_os_type():
    return platform.system()
"""
description:获取cpu信息
"""
def get_cup_info():
    cpu_message=psutil.cpu_times(percpu=True)
    logical_cpu=psutil.cpu_count(logical=True) #逻辑cpu个数
    physical_cpu=psutil.cpu_count(logical=False)  #物理cpu个数
    return cpu_message,logical_cpu,physical_cpu
"""
description:获取内存信息
"""
def get_memory():
    memory_message=psutil.virtual_memory()
    return memory_message
"""
description:获取交换空间信息
"""
def get_swap_memory():   #获取swap
    swap_memory=psutil.swap_memory()
    return swap_memory
"""
description:获取磁盘信息
"""
def get_disk_message():
    disk_tag=[]
    disk_message=psutil.disk_partitions(all=False)
    for disk in disk_message:
        disk_tag.append(disk)
    return disk_message,disk_tag


if __name__=="__main__":
    os_type=get_os_type()
    if os_type == "Windows":
        print(get_os_start_time())
        win32api.MessageBox(0, "这是一个测试提醒OK消息框", "提醒",win32con.MB_OK)
    else:
        print("\033[0;36m当前系统为Linux,暂不支持\033[0m")
