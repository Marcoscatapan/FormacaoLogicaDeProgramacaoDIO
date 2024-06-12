def calc(wins, losses):
    balance = wins - losses
    return balance

saldoDeVitorias = calc(89, 42)
playerResults = saldoDeVitorias

if playerResults <= 10:
    level = "Ferro"
elif 11 <= playerResults <= 20:
    level = "Bronze"
elif 21 <= playerResults <= 50:
    level = "Prata"
elif 51 <= playerResults <= 80:
    level = "Ouro"
elif 81 <= playerResults <= 90:
    level = "Diamante"
elif 91 <= playerResults <= 100:
    level = "Lendário"
elif playerResults >= 101:
    level = "Imortal"
else:
    level = "Nível não catalogado!"

print("O Herói tem um saldo de", saldoDeVitorias, "e está no nível", level)