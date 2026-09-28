item1_name = input("First item name: ")
item1_quantity = int(input("First item quantity: "))
item1_price = float(input("First item unit price: "))
#ilk ürün
item2_name = input("Second item name: ")
item2_quantity = int(input("Second item quantity: "))
item2_price = float(input("Second item unit price: "))
#ikinci ürün
delivery_fee = float(input("Delivery fee: "))
tax_percentage = float(input("Tax percentage: "))
#kargo ücreti ve yüzdesi 
item1_total = item1_quantity * item1_price
item2_total = item2_quantity * item2_price
#item1_total → 1. ürünün adet × fiyatı
subtotal = item1_total + item2_total
tax = subtotal * tax_percentage / 100
final_total = subtotal + tax + delivery_fee
#subtotal → iki ürünün toplamı
#tax → sadece ürünlerin subtotal'ı üzerinden vergi
#final_total → subtotal + vergi + teslimat
print()
print("PURCHASE QUOTE")
print(f"{item1_name}: {item1_total:.2f} TRY")
print(f"{item2_name}: {item2_total:.2f} TRY")
print(f"Subtotal: {subtotal:.2f} TRY")
print(f"Tax: {tax:.2f} TRY")
print(f"Delivery fee: {delivery_fee:.2f} TRY")
print(f"Final total: {final_total:.2f} TRY")
#sonuçları ekrana yazdırmak için yapıldı. 
#2f virgülden sonra iki basamak göstermesi için
