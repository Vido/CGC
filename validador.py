import re

def valida_cep(cep):
    match = re.match(r'^[1-9]\d{5}$', cep)
    if match is None:
        return False

    pares = set([])
    for i in range(0, 6):
        substr = cep[i:i+2]
        if substr in pares:
            return False 
        pares.add(substr)

    return True

if __name__ == '__main__':
    cep = input('Digite um CEP:')
    print(valida_cep(cep))

