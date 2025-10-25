# {}内に=を書くと値と式を両方出力できる
hp, maxHP = 80, 100
print(f'{hp} / {maxHP}')
print(f'{hp = } / {maxHP = }')  # hp = 80 / maxHP = 100
print(f'{hp / maxHP = }')
