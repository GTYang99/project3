from gpiozero import MCP3008

# MCP3008第6個針腳
# 原廠文件MCP3008為5伏特
temperatrue = MCP3008(6,max_voltage=5.0)
lightValue = MCP3008(7,max_voltage=5.0)

def getTemperature():
    # temperatrue.value()
    # Value從設備讀取的當前值，縮放為 0 到 1 之間的值（或 -1 到 +1，對於在差分模式下運行的某些設備）。
    # 5.0是電壓
    print("溫度:",temperatrue.value*5.0*100)

def getLightValue():
    # lightValue.value()
    print("光線:",lightValue.value*1000)