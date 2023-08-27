

#Importando módulo de acesso a subprocessos.
import subprocess

#Processo que irá executar o comando 'ntsh wlan show network.
#A variável 'redes' armazena o valor de saída do comando acima.
redes = subprocess.run(['netsh', 'wlan', 'show', 'network'], capture_output=True, text=True).stdout 
lista = redes.split('\n')

#variável que armazena o nome das redes (SSID).
ssids = [k for k in lista if 'SSID' in k]

#Caso queria printar o network_type, basta adicioná-lo no print abaixo.
#A variável 'network_type' aramazena o tipo de rede wi-fi.
network_type = [k for k in lista if 'Tipo de rede' in k]

#Imprimindo na tela o valor dos nomes das redes a partir do comando armazena na variável 'redes'.
print(f"SSIDs:{ssids}\n ")


#fim