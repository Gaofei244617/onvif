

# 设置静态IP
# cmd = "netsh interface ipv4 set address name=\"WLAN\" source=static addr=192.168.1.1 mask=255.255.0.0 gateway=192.168.1.1"
# 向网卡添加IP
# cmd2 = "netsh interface ipv4 add address name=\"WLAN\" addr=192.168.1.14 mask=255.255.0.0"

net_name = "WLAN"
net_mask = "255.255.0.0"
net_gateway = "192.168.0.1"
net_ip = "192.168.0.1"

cmd = "netsh interface ipv4 set address" + \
    " name=\"" + net_name + "\"" + \
    " source=static" + \
    " addr=" + net_ip + \
    " mask=" + net_mask + \
    " gateway=" + net_gateway

f = open("add_ip.bat", "w")

# 设置静态IP
f.write(cmd + "\n")

# 向网卡添加IP
for i in range(100):
    for j in range(256):
        cmd = "netsh interface ipv4 add address" + \
            " name=\"" + net_name + "\"" + \
            " addr=" + "192.168." + str(i) + "." + str(j) + \
            " mask=" + net_mask
        f.write(cmd + "\n")

f.write("pause\n")
f.close()
