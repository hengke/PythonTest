# coding:utf-8

# 使用utf-8编码

import platform

import wmi

print("您的CPU生产商为:" + platform.machine())

print("您的CPU家族为:" + platform.processor())

cpuinfo = wmi.WMI()
for cpu in cpuinfo.Win32_Processor():

    print("您的CPU序列号为:" + cpu.ProcessorId.strip())

    print("您的CPU名称为:" + cpu.Name)

    print("您的CPU已使用:%d%%" % cpu.LoadPercentage)

    print("您的CPU核心数为:%d" % cpu.NumberOfCores)

    print("您的CPU时钟频率为:%d" % cpu.MaxClockSpeed)