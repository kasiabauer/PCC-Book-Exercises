people_num = int(input(f"Na ile osób chcesz zarezerwować stolik?: "))

if people_num > 8:
    print(f"Proszę zaczekać na stolik.")
else:
    print(f"Stolik jest gotowy.")
