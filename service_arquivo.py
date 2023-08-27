'''
importando módulos necessários . Socket será utilizado para conexão.
esse cpodigo lê as portas discriminadas em um outro arquivo ('portas_ip_abertas.txt')
rodar outro script antes ou colocar portas no seguinte padrão no arquivo: 
Porta: n° da porta
depois pode prosseguir com o script
Além disso, o código em questão cria um arquivo com as versoes do serviço. 
O arquivo é criado no próprio diretório onde o script foi rodado.

'''

import socket, sys


#argumento que deve ser passado é o ip


arquivo  = open('portas_192.168.0.30_abertas.txt')

if len(sys.argv) > 1:
    for linha in arquivo.readlines():
        port = linha.split(':')
        port = int(port[1])
        print('Verificando Versão do serviço na porta:' + str(port))
        

        try:
            ip = sys.argv[1]
            socket.setdefaulttimeout(20)
            
            k = socket.socket()
            
            k.connect((ip, port))
            
            if port == 80 or port == 443:
                
                request = 'GET HTTP/1.1 \r \n'
                
                k.send(request.encode())
                
            servico = k.recv(2048)
            
            servico = servico.decode()
            
            k.close()
        
            print('-->' + ip + ' >>>>>' + str(servico))

            arquivo = open('servicos_versoes_' + ip + '.txt ', 'a+')
            arquivo.write('--->Servico da porta: ' + str(port))
            arquivo.write(str(servico) +'\n')
            arquivo.close()
            
        except:
                print('NÃO foi possível se conectar com o servico!!!\n')        

else:
    print('fornecça o IP para análise')
        