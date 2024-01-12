import time, os

#Contador de tempo de estudo e descanso
timeCount = 0
tempEstudo = float(input("Digite o tempo de estudo em min: "))
tempDescanso = float(input("Digite o tempo de descanso em min: "))
tempEstudo = tempEstudo * 60
tempDescanso = tempDescanso * 60
while True:
    if timeCount < tempEstudo:
        timeCount += 1
        time.sleep(1)
    else:
        timeCount = 0
        os.system('notify-send "Hora de descançar!"')
        os.system('paplay /usr/share/sounds/freedesktop/stereo/message.oga')
        while timeCount < tempDescanso:
            timeCount += 1
            time.sleep(1)
        timeCount = 0
        os.system('notify-send "Hora de estudar!"')
        os.system('paplay /usr/share/sounds/freedesktop/stereo/message.oga')
