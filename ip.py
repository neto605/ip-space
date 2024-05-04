import json
import re

def carregar_ips_hyundai(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        data = arquivo.read()
        # Usando expressão regular para encontrar endereços IP
        ips = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}\b', data)
    return set(ips)


def carregar_ips_aws(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        data = json.load(arquivo)
        ips = [item["ip_prefix"] for item in data["prefixes"]]
    return set(ips)


def comparar_ips(dataset1, dataset2):
    ips_dataset1 = carregar_ips_hyundai(dataset1)
    ips_dataset2 = carregar_ips_aws(dataset2)
    
    ips_divergentes = ips_dataset1 - ips_dataset2
    
    cont1 = 0 
    for ip in ips_dataset1:
        cont1 += 1
    
    print("Dataset1:", cont1, "resultados")
   
    cont2 = 0 
    for ip in ips_dataset2:
        cont2 += 1
        
    
    print("Dataset2:", cont2, "resultados")
            
    if not ips_divergentes:
        print("Todos os IPs são iguais nos dois datasets.")
    else:
        print("Os seguintes IPs estão presentes no dataset 1, mas não no dataset 2:")
        for ip in ips_divergentes:
            print(ip)

dataset1 = "dataset1.txt"
dataset2 = "dataset2.txt"

comparar_ips(dataset1, dataset2)

