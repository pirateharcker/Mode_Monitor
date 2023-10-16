import subprocess

print(".----------------------MODE MONITOR----------------------.")
print(":     **                      **                  **     .")
print(":    ****                    ****                ****    :")
print(":   ******                  ******              ******   :")
print(":  ********      {.A.}     ********    {.A.}   ********  :")
print(":  ********                ********            ********  :")
print(":   ******                  ******              ******   :")
print(":    ****                    ****                ****    :")
print(":     **                      **                  **     :")
print(":----------------------MODE MONITOR----------------------:")

def activate_mode_monitor(interface):
    try:
        subprocess.run(['sudo', 'ifconfig', interface, 'down'])
        
        subprocess.run(['sudo', 'iw', 'dev', interface, 'set', 'monitor', 'none'])
        
        subprocess.run(['sudo', 'ifconfig', interface, 'up'])
        
        print(f"Le mode monitor a été activé sur l\'interface {interface}.")
        
    except Exception as e :
        print(f"Erreur : {str(e)}")
        
interface = 'wlan0'
activate_mode_monitor(interface)