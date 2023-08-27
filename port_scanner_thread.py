#importandoi módulos necessários. Socket para conexão, sys para passagem de argumento ao rodar o script (ip)
# e o threading para realizar um processamento acelerado do scan de portas, diferente do scan de portas sequencial.
import socket, sys, threading 

#definindo funcão para scan de portas de rede
def scan_porta(port):
    
    #estabelencendo conexão (socket - porta)
    meu_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    meu_socket.settimeout(0.5)
    
    #fazendo validação. O método 'connect_ex' retorna 0 de a conexão for estabelecida
    if meu_socket.connect_ex((ip, port)) == 0:
        print('Porta: ' + str(port) + " ABERTA!")
        meu_socket.close()
        
        #criando arquivo para salvar output do scan de rede
        #o arquivo criado é salvo no mesmo diretório onde o script foi executado
        arquivo = open('portas_' + ip + '_abertas.txt', 'a+')
        arquivo.write('Porta: ' + str(port) + ' -ABERTA-\n')
        arquivo.close()
        
        
        
        

#definindo valor padrão para variável de indentação        
r = 1

#validando entrada (argumento - IP) passado pelo usuário. Deve-se, pelo menos, ter um IP para scanear

if len(sys.argv) > 1:
     print('Verificando HOST')
     
     #o argumento necessário é o IP (utilizando lib 'sys').
     ip = sys.argv[1]
     
     print('inicializando o Scan em: ' + ip)  
     
     #em relação ao código anterior, 'port_scanner_seq.py', para melhorar sua eficiência reduziu-se o número de portas para scan
     #além do uso do threading
     
     #Dentro deste laço 'for', pode-se modificar o segundo argumento para realizar o scan de quantas
     #portas forem necessárias. O número de portas vai de 1 até 65535 (já definido no for abaixo).
     for port in  range(1, 65535):
         
         #aqui se usa o módulo threading para processamento paralelo do scan
         t = threading.Thread(target = scan_porta, kwargs = {'port': r})
         r += 1
         t.start()
else:
    print('Informe o Internet Protocol (IP) para proceder com o SCAN de REDE :)')
    exit(0)    
