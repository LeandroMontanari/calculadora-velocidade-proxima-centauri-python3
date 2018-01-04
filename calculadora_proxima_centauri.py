################################################
##### PROGRAMADO POR: LEANDRO L. MONTANARI #####
################################################


def v(k):  # Função para melhorar a exibição dos resultados
    mf = '{:.2f}'.format(k)
    dec = mf[-2:]
    intf = '{:,}'.format(int(k))
    antes = str(intf).replace(',', '.')
    fn = '{}{}{}'.format(antes, ',', dec)
    return fn


c = 299792458  # Constante da velocidade da luz em metros por segundo
sa = 31557600  # Quantidade de segundos em um ano comum

lym = c * sa  # Ano-luz em metros
lykm = lym / 1000  # Ano-luz em quilômetros

proximacentauri = 4.243  # Distância de Proxima Centauri em anos-luz
kmpc = proximacentauri * lykm  # Distância de Proxima Centauri em quilômetros

tempo_anos = int(input('Em quantos anos você quer chegar em Proxima Centauri? '))

tempo_segundos = tempo_anos * sa

vel_kmps = kmpc / tempo_segundos  # Velocidade necessária em km/s
vel_kmph = vel_kmps * 60 * 60  # Velocidade necessária em km/h

porcentagem = (vel_kmps / (c / 1000)) * 100

vel_kmph = v(vel_kmph)
vel_kmps = v(vel_kmps)
porcentagem = v(porcentagem)

print(f'\nPara chegar em Proxima Centauri em {tempo_anos} anos, você precisaria viajar a '
      f'{vel_kmph} km/h ou {vel_kmps} km/s ({porcentagem}% da velocidade da luz).')

fim = input('\nPressione <Enter> para sair...')

