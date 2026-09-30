tickets_sold = 0
# kac bilet sattik
total_revenue = 0
# toplam kac tl kazandik
free_tickets = 0
# kac ucretsiz bilet sattik
while True:
    # bu islemi surekli tekrar et demek dogru oldugu surece
    customer_name = input("Customer name (or q to quit): ")
    if customer_name.lower() == "q":
        break
    # lower kucuk harfe ceviriyor
    age = int(input("Age: "))
    if age < 0 or age > 120:
        print("Invalid age.")
        continue
    day = input("Day (weekday/weekend): ").lower()
    if day != "weekday" and day != "weekend":
        print("Invalid day.")
        continue
    student = input("Student (yes/no): ").lower()
    # ogrenci mi diye soruyoruz
    if student != "yes" and student != "no":
        print("Please answer yes or no.")
        continue
    # yes no harici bir sey demis mi
    if day == "weekday":
        base_price = 200
    else:
        base_price = 250
        # else kullandik cunku weekday degilse geriye weekend kaliyor

    if age < 6:
        price = 0
        ticket_type = "Free"
        # musteri 6 yasindan kucukse fiyat sifir ve bilet turu free

    elif age >= 65:
        price = base_price * 0.50
        ticket_type = "Senior"
        # 65 yas ve ustuyse yuzde 50 indirim

    elif age >= 6 and age <= 12:
        price = base_price * 0.60
        ticket_type = "Child"
        # 6-12 yas arasi yuzde 40 indirimli
        # yuzde 60 yazdik cunku fiyatın yuzde 60'ini odeyecek

    elif student == "yes" and age <= 25:
        price = base_price * 0.70
        ticket_type = "Student"
        # ogrenci ve 25 yas veya alti ise yuzde 30 indirim

    else:
        price = base_price
        ticket_type = "Standard"
        # yukaridakilerin hicbiri degilse standart bilet

    print(f"{customer_name}: {price:.2f} TRY ({ticket_type})")
    # metnin icine degisken degeri koyuyor

    tickets_sold = tickets_sold + 1
    total_revenue = total_revenue + price
    # sayac, kac bilet satilmis

    if ticket_type == "Free":
        free_tickets = free_tickets + 1
        # ucretsiz bilet sayiyor


if tickets_sold == 0:
    print("No tickets sold.")
    # hic bilet satilmis mi

else:
    average_price = total_revenue / tickets_sold
    # ortalama bilet fiyat

    print(f"Tickets sold: {tickets_sold}")
    print(f"Total revenue: {total_revenue:.2f} TRY")
    print(f"Average price: {average_price:.2f} TRY")
    print(f"Free tickets: {free_tickets}")


