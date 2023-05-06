prompt = "\nPodaj nazwy miast, które chciałbyś odwiedzieć:"
prompt += "\n(Gdy zakończysz podawanie miast, napisz 'koniec')"

while True:
    city = input(prompt)

    if city == 'koniec':
        break
    else:
        print(f"Chciałabym odwiedzić {city.title()}")
