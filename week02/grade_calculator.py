total_students = 0
total_score = 0
# Başlangıçta 0 öğrenci ve 0 toplam puan var. Bunlar en sonda ortalamayı hesaplamak için.
while True:
  # burası sonsuz döngü.break yazana kadar tekrar tekrar öğrenci sorar.
    name = input("Enter student name (or q to quit): ")

    if name == "q":
        break

    score = int(input("Enter score: "))

    if score < 0 or score > 100:
        print("Invalid score. Please enter a number between 0 and 100.")
        continue

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(name + ":", score, "->", grade)
# öğrencinin sonucunu ekrana yazar
    total_students = total_students + 1
    total_score = total_score + score
# ilk başta sıfır öğrenci vardı bir ekleye ekleye gidiyor en sonunda sınava kaç öğrenci girdiğini öğrenmemizi sağlayacak  ve öğrencilerin kaç puan aldığını söyleyecek
if total_students > 0:
    average = total_score / total_students
    print("Total students:", total_students)
    print("Average score:", round(average, 2))
  # sonucu iki ondalık sayıya yuvarlıyor yani uzatmıyor
else:
    print("No students entered.")
