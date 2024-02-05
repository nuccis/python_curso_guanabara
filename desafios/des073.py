#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem da colocação. Depois mostre: A) Apenas os 5 primeiros colocados; B) Os últimos 4 colocados da tabela; C) Uma lista com os times ordem alfabética; D) Em que posição na tabela está o time que eu escolher hehehe

times = ('Palmeiras', 'Flamengo', 'Botafogo', 'Atlético-MG', 'Grêmio', 'Bragantino', 'Fluminense', 'Athletico-PR', 'Cuiabá', 'São Paulo', 'Corinthians', 'Internacional', 'Fortaleza', 'Cruzeiro', 'Santos', 'Vasco da Gama', 'Bahia', 'Goiás', 'Coritiba', 'América-MG')

print('=#'*30)
print(f'A) Os 5 primeiros colocados: {times[0:5]}')
print('=#'*30)
print(f'B) Os últimos 4 da tabela: {times[16:20]}')
print('=#'*30)
print(f'C) Os times em ordem alfabética: {sorted(times)}')
print('=#'*30)
print(f'D) O Cuiabá está na posição {times.index('Cuiabá')+1} na tabela')