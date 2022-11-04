from gpiozero import MCP3008

def getTemperature():
    temperatrue = MCP3008(7)
    print(temperatrue.value*3.3*100)