#importando módulos necessários (sys: para passagem de argumentos no
#script e socket para gerenciar as portas de rede)
import socket, sys

#realizando tratamento do argumento passado. Deve-se passar, no minimo UM 
# argumento ( o 0 é o próprio script)
if len(sys.argv) > 1:
     print('Verificando HOST')
     
     #o argumento necessário é o IP (utilizando lib 'sys').
     ip = sys.argv[1]
     
     print('inicializando o Scan em: ' + ip)
     
     for port in range(1, 65535):
        
        meu_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        if meu_socket.connect_ex((ip, port)) == 0:
                print('Porta: ' + str(port) + " ABERTA")
                meu_socket.close()
        else:
            print('Porta: ' + str(port) + ' FECHADA')
else:
    print('Informe o Internet Protocol (IP) para proceder com o SCAN de REDE :)')
    exit(0)
            
            
            
