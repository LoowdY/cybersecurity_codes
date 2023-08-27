#need improvement (not working in all Operating systems)
#a ideia desta ferramenta é utilizar o protocolo ARP (Adress Resolution Protocol) e 
# entender melhor o endereçamento do IP para Mac (Media Acess Control), ou seja, buscar escanear hosts de rede.

#importando módulos necessários
import scapy.all as scapy
import socket


requisicao = scapy.ARP()

requisicao.pdst = '192.168.0.1/24'

broadcast = scapy.Ether()

#endereço MAC (ff:ff:ff:ff:ff:ff)
broadcast.dst = 'ff:ff:ff:ff:ff:ff'

requisicao_broadcast = broadcast / requisicao

clientes = scapy.srp(requisicao_broadcast, timeout = 10, verbose = 1)[0]

for element in clientes:
    ip = element[1].prsc
    mac = element[1].hwsrc
    print(ip + '     ' + mac)
    
    
    try:
        a = socket.gethostbyname(ip)
        print('Nome da Máquina (hostname):' + a[0])
        
    except:
        print('Nome da máquina: DESCONHECIDO/NÃO ENCONTRADO.')



