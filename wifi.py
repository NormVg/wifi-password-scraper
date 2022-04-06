import subprocess, os

os.system('color a')
def avalable_wifi():
    data1 = subprocess.check_output(['netsh','wlan','show','profiles'])
    data2 = data1.decode("utf-8")
    data3 = data2.split('\n')
    #print(data3)
    
    names = []
    for line in data3:
        if "All User Profile     : " in  line:
            name = line.split(':')[1]
            names.append(name[1:-1])
            #print(name)
        #print(names)
    return names


cre = []
for name in avalable_wifi():
    nDATA = subprocess.check_output(['netsh','wlan','show','profile',name,'key=clear'])
    data = nDATA.decode('utf-8',errors='backslashreplace')
    data = data.split('\n')
    names = []
    
    for line in data:
        if 'Key Content' in line:
            passs = line.split(":")[1]
        #else:
          #  passs = 'NOT_AVALABLE'
    o = f'name = {name} , password = {passs}'
    print(o)
    cre.append(o)
with open('log.txt','w') as f:
    for cr in cre:
        f.write(f'{cr} \n')
    f.close()
        #
    

    
