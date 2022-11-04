from gpiozero import MCP3008
from gpiozero import DistanceSensor

# MCP3008第6個針腳
# 原廠文件MCP3008為5伏特
temperatrue = MCP3008(6,max_voltage=5.0)
lightValue = MCP3008(7,max_voltage=5.0)
# 超音波接收器針腳位置
#gpio23 -> echo 220,220分壓
#gpio24 -> trig
sensor = DistanceSensor(23, 24)

def getTemperature():
    # temperatrue.value()
    # Value從設備讀取的當前值，縮放為 0 到 1 之間的值（或 -1 到 +1，對於在差分模式下運行的某些設備）。
    # 5.0是電壓
    print("溫度:",temperatrue.value*5.0*100)

def getLightValue():
    # lightValue.value()
    print(f"光線:{lightValue.value*1000:.1f}")

def getDistance():    
    # print("距離:",sensor.distance)
    if sensor.distance < 1.0: 
        print(f"距離:{sensor.distance*100:.2f}公分")
    else:
        print(f"距離:大於100公分")