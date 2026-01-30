ip_address=[]

with open("sample.log","r") as log:
    lines=log.readlines()

for line in lines:
    if "reverse mapping" in line:
        words=line.split("[")
        ip_addr=words[1].split("]")
        ip_address.append(ip_addr[0])

with open("ip_address.txt","w") as ip:
    for addr in ip_address:
        ip.write(addr+"\n")

print("IP addresses have been extracted successfully.")