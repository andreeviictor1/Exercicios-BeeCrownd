idade = int(input())

anos = idade//365
dias = idade%365

meses = dias//30
dias = dias%30

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')
