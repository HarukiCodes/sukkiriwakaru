height = int(input('身長(cm)を入力してください >>')) / 100
weight = int(input('体重(kg)を入力してください >>'))
bmi = weight / height**2
print(f'BMIは{bmi}です')
