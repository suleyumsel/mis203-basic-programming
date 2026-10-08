import math
#matematiksel işlemler için kullanılan bir kütüphanedir. Örneğin, yuvarlama, karekök alma gibi işlemleri yapmamızı sağlar.
import random
#random, rastgele sayı üretmek veya rastgele seçim yapmak için kullanılan bir kütüphanedir. Örneğin, bir listeden rastgele bir öğe seçmek için kullanılabilir.
import time
#time, zamanla ilgili işlemler yapmak için kullanılan bir kütüphanedir. Örneğin, belirli bir süre beklemek veya zaman ölçmek için kullanılabilir.
#import, başka bir kütüphanenin veya modülün özelliklerini kendi kodumuzda kullanmamızı sağlar.
from rich.console import Console 
#Rich, terminalde renkli yazılar, kutular, animasyonlar ve ilerleme çubukları oluşturmamızı sağlıyor.
#console , Rich kütüphanesinin bir parçasıdır ve terminalde yazı yazdırmak için kullanılır. Örneğin, console.print() ile renkli yazılar yazdırabiliriz.
#ve renkli sorular ve mesajlar için kullandım
from rich.panel import Panel
#panel çerçeve için
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
#progress ilerleme göstergesi
#spinnercolumn dönen gösterge
#textcolumn ilerleme göstergesinde metin gösteriyor
#barcolumn dolan ilerleme çubuğu
from rich.align import Align
#align metin hizalamada kullanıldı sonuç kartında

console = Console()

# PART 2 - Question Progress Bar

def show_progress(question_number):
    #def fonksiyon tanımlamak için show progressi tanımladı
    #show progress ilerleme çubuğu için her soruda kullanıldı
    console.print()
    console.print(
        f"✨ Question {question_number} of 9 completed!",
        style="bold cyan"
    )
#f string metnin içine değişken ekler
#kalın yazı ve cam göbeği renk 
    with Progress(
        #with Progress() → İlerleme çubuğunu başlatır, işlem bitince kapatır.
        TextColumn("🔮 Mystical Journey"), #çubuğun  ynındaki yazıyı gösterir
        BarColumn(bar_width=30, complete_style="magenta"), #30 karaakter genişliği tamamlanan kısım mor
        TextColumn("{task.percentage:>3.0f}%"), #ilerleme yüzdeliğini ondalıksı< gösterir
        transient=False #işlem bitince çubuğun terminalde kalmasını sağlar
    
    ) as progress: #ilerleme nesnesine progress ismini verir 
        progress.add_task(
            "Journey",
            total=9,
            completed=question_number
        )

    time.sleep(0.5)


# Run one complete game, then return whether the player wants another round.
def play_game(): 
    console.print(
        Panel( #kutu oluşturur
            "🔮 Welcome to Mystical World! 🔮\n"
            "✨ Discover your mystical identity!",
            title="✨ MYSTICAL WORLD ✨",
            border_style="magenta"
        )
    )
    time.sleep(1)  #programı belli süre bekletiyor

    console.print()
    console.print("🌙 Have you ever wondered which mystical creature you would be?", style="bold cyan")

    time.sleep(1)

    console.print("🪄 Answer 9 questions about your personality and preferences.")
    console.print("✨ Your choices will reveal your mystical identity!")

    console.print()
    console.print("🧛 Vampire  |  🐺 Werewolf  |  🧝 Elf")
    console.print("👻 Ghost    |  🐉 Dragon    |  🧙 Witch")

    console.print()
    name = console.input("[bold magenta]💜 What is your name? [/bold magenta]")

    console.print()
    console.print(f"✨ Welcome, {name}! Let your mystical journey begin!", style="bold green")

    #console.print() → Renkli yazı yazdırmamızı sağlıyor.
    #console.input() → Kullanıcıdan cevap alırken soruyu renkli göstermemizi sağlıyor.
    # Mystical creature scores
    vampire = 0
    werewolf = 0
    elf = 0
    ghost = 0
    dragon = 0
    witch = 0

    # Question 1 - Night or Day?
    console.print()
    console.print(
        Panel(
            "🌙 1. Night\n☀️ 2. Day", #\n → Alt satıra geçer.
            title="Question 1/9 - Which do you prefer?",
            border_style="cyan"
        )
    )

    answer = console.input("[bold magenta]Your choice (1/2): [/bold magenta]")

    while answer != "1" and answer != "2": #koşul doğru değilse kullanıcıya tekrar sorar #!= eşit değildir
        console.print("❌ Please enter 1 or 2.", style="red")
        answer = console.input("[bold magenta]Your choice (1/2): [/bold magenta]")

    if answer == "1":
        vampire += 1
        werewolf += 1
        ghost += 1
    else:
        elf += 1
        dragon += 1
        witch += 1

    console.print("✨ Your answer has been recorded!", style="green")
    show_progress(1)
    # Question 2 - Speed or Flying?
    time.sleep(1)

    console.print()
    console.print(
        Panel(
            "⚡ 1. Speed\n🪽 2. Flying",
            title="Question 2/9 - Which ability would you choose?",
            border_style="magenta"
        )
    )

    answer = console.input("[bold magenta]Your choice (1/2): [/bold magenta]")

    while answer != "1" and answer != "2":
        console.print("❌ Please enter 1 or 2.", style="red")
        answer = console.input("[bold magenta]Your choice (1/2): [/bold magenta]")

    if answer == "1":
        vampire += 1
        werewolf += 1
        elf += 1
    else:
        ghost += 1
        dragon += 1
        witch += 1

    console.print("✨ Your answer has been recorded!", style="green")
    show_progress(2)
    # Question 3 - Forest or House?
    time.sleep(1)

    console.print()
    console.print(
        Panel(
            "🌲 1. Forest\n🏠 2. House",
            title="Question 3/9 - Where would you rather live?",
            border_style="green"
        )
    )

    answer = console.input("[bold magenta]Your choice (1/2): [/bold magenta]")

    while answer != "1" and answer != "2":
        console.print("❌ Please enter 1 or 2.", style="red")
        answer = console.input("[bold magenta]Your choice (1/2): [/bold magenta]")

    if answer == "1":
        elf += 1
        werewolf += 1
    else:
        vampire += 1
        ghost += 1
        dragon += 1
        witch += 1

    console.print("✨ Your answer has been recorded!", style="green")
    show_progress(3)
    # Question 4 - Magic, Immortality or Raw Power?
    time.sleep(1)

    console.print()
    console.print(
        Panel(
            "✨ 1. Magic\n♾️ 2. Immortality\n💪 3. Raw Power",
            title="Question 4/9 - Which power would you choose?",
            border_style="yellow"
        )
    )

    answer = console.input("[bold magenta]Your choice (1/2/3): [/bold magenta]")

    while answer != "1" and answer != "2" and answer != "3":
        console.print("❌ Please enter 1, 2 or 3.", style="red")
        answer = console.input("[bold magenta]Your choice (1/2/3): [/bold magenta]")

    if answer == "1":
        witch += 1
        elf += 1
    elif answer == "2":
        vampire += 1
        ghost += 1
    else:
        dragon += 1
        werewolf += 1

    console.print("✨ Your answer has been recorded!", style="green")
    show_progress(4)
    # Question 5 - What is your greatest strength?
    time.sleep(1)

    console.print()
    console.print(
        Panel(
            "🧠 1. Intelligence\n"
            "💪 2. Physical Strength\n"
            "🖤 3. Manipulation",
            title="Question 5/9 - What is your greatest strength?",
            border_style="blue"
        )
    )

    answer = console.input("[bold magenta]Your choice (1/2/3): [/bold magenta]")

    while answer != "1" and answer != "2" and answer != "3":
        console.print("❌ Please enter 1, 2 or 3.", style="red")
        answer = console.input("[bold magenta]Your choice (1/2/3): [/bold magenta]")

    if answer == "1":
        witch += 1
        elf += 1
    elif answer == "2":
        werewolf += 1
        dragon += 1
    else:
        vampire += 1
        ghost += 1

    console.print("✨ Your answer has been recorded!", style="green")
    show_progress(5)
    # Question 6 - Which place attracts you the most?
    time.sleep(1)

    console.print()
    console.print(
        Panel(
            "🏰 1. Ancient Castle\n"
            "🌳 2. Enchanted Forest\n"
            "⛰️ 3. Mysterious Mountain",
            title="Question 6/9 - Which place attracts you the most?",
            border_style="cyan"
        )
    )

    answer = console.input("[bold magenta]Your choice (1/2/3): [/bold magenta]")

    while answer != "1" and answer != "2" and answer != "3":
        console.print("❌ Please enter 1, 2 or 3.", style="red")
        answer = console.input("[bold magenta]Your choice (1/2/3): [/bold magenta]")

    if answer == "1":
        vampire += 1
        ghost += 1
    elif answer == "2":
        elf += 1
        werewolf += 1
    else:
        dragon += 1
        witch += 1

    console.print("✨ Your answer has been recorded!", style="green")
    show_progress(6)
    # Question 7 - How would you react to danger?
    time.sleep(1)

    console.print()
    console.print(
        Panel(
            "⚔️ 1. Fight\n"
            "🧠 2. Make a Clever Plan\n"
            "👻 3. Disappear",
            title="Question 7/9 - How would you react to danger?",
            border_style="red"
        )
    )

    answer = console.input("[bold magenta]Your choice (1/2/3): [/bold magenta]")

    while answer != "1" and answer != "2" and answer != "3":
        console.print("❌ Please enter 1, 2 or 3.", style="red")
        answer = console.input("[bold magenta]Your choice (1/2/3): [/bold magenta]")

    if answer == "1":
        werewolf += 1
        dragon += 1
    elif answer == "2":
        witch += 1
        vampire += 1
    else:
        ghost += 1
        elf += 1

    console.print("✨ Your answer has been recorded!", style="green")
    show_progress(7)
    # Question 8 - Which magical object would you choose?
    time.sleep(1)

    console.print()
    console.print(
        Panel(
            "📖 1. Ancient Spellbook\n"
            "🪞 2. Mysterious Mirror\n"
            "💎 3. Powerful Crystal",
            title="Question 8/9 - Which magical object would you choose?",
            border_style="magenta"
        )
    )

    answer = console.input("[bold magenta]Your choice (1/2/3): [/bold magenta]")

    while answer != "1" and answer != "2" and answer != "3":
        console.print("❌ Please enter 1, 2 or 3.", style="red")
        answer = console.input("[bold magenta]Your choice (1/2/3): [/bold magenta]")

    if answer == "1":
        witch += 1
        elf += 1
    elif answer == "2":
        vampire += 1
        ghost += 1
    else:
        dragon += 1
        werewolf += 1

    console.print("✨ Your answer has been recorded!", style="green")
    show_progress(8)
    # Question 9 - What do you fear the most?
    time.sleep(1)

    console.print()
    console.print(
        Panel(
            "🕊️ 1. Losing Freedom\n"
            "💔 2. Losing Loved Ones\n"
            "🌫️ 3. Being Forgotten",
            title="Question 9/9 - What do you fear the most?",
            border_style="magenta"
        )
    )

    answer = console.input("[bold magenta]Your choice (1/2/3): [/bold magenta]")

    while answer != "1" and answer != "2" and answer != "3":
        console.print("❌ Please enter 1, 2 or 3.", style="red")
        answer = console.input("[bold magenta]Your choice (1/2/3): [/bold magenta]")

    if answer == "1":
        dragon += 1
        elf += 1
    elif answer == "2":
        werewolf += 1
        vampire += 1
    else:
        ghost += 1
        witch += 1

    console.print("✨ All 9 questions completed!", style="bold green")
    show_progress(9)
    console.print("🔮 Your mystical identity is about to be revealed...", style="magenta")
    # Calculate the final scores
    scores = { #scores = {, karakterlerin puanlarını bir arada saklayan bir dictionary (sözlük) oluşturur.
        "Vampire": vampire,
        "Werewolf": werewolf,
        "Elf": elf,
        "Ghost": ghost,
        "Dragon": dragon,
        "Witch": witch
    }

    # Find the highest score
    highest_score = max(scores.values())
#score s.values() → dictionarydeki tüm değerleri alır. max() → bu değerler arasından en yüksek olanı bulur.
    # Find all creatures with the highest score
    winners = []

    for creature in scores: #for döngü oluşturur. karakterleri sırayla kontrol eder en yüksek puanlıları winners listesine ekler
        if scores[creature] == highest_score:
            winners.append(creature)
#eşit puan alan birden fazla karakteri de saklar
    # Choose randomly if there is a tie
    result = random.choice(winners) #kazanan karakterler arasında rastgele seçim yapar

    # Calculate compatibility percentage
    compatibility = math.ceil((highest_score / 9) * 100)  #compatibility → Hesaplanan yüzdeyi saklayan değişken.
    #/ 9 → Puanı toplam 9 soruya böler.
    #* 100 → Sonucu yüzdeye çevirir.
    #- math.ceil() → Sonucu bir üst tam sayıya yuvarlar.
    #Bu kod, kazanan karakterin uyumluluk yüzdesini hesaplar. 🔮
    # Mystical creature information
    creature_info = { #sözlük oluşturuyor ve her karakterin bilgilerini saklar
        "Vampire": {
            "emoji": "🧛",
            "power": "Immortality",
            "personality": "Mysterious, intelligent and charismatic",
            "home": "Ancient Castle"
        },
        "Werewolf": {
            "emoji": "🐺",
            "power": "Super Strength",
            "personality": "Brave, loyal and protective",
            "home": "Enchanted Forest"
        },
        "Elf": {
            "emoji": "🧝",
            "power": "Nature Magic",
            "personality": "Wise, peaceful and creative",
            "home": "Magical Forest"
        },
        "Ghost": {
            "emoji": "👻",
            "power": "Invisibility",
            "personality": "Mysterious, observant and independent",
            "home": "Haunted Mansion"
        },
        "Dragon": {
            "emoji": "🐉",
            "power": "Fire Breathing",
            "personality": "Powerful, fearless and adventurous",
            "home": "Mystical Mountain"
        },
        "Witch": {
            "emoji": "🧙",
            "power": "Spell Casting",
            "personality": "Clever, curious and imaginative",
            "home": "Magical Cottage"
        }
    }
    # PART 1 - Mystical Identity Reveal


    console.print()
    console.print("🌙 The mystical world is reading your soul...", style="bold magenta")

    time.sleep(1)

    # Mystical loading animation
    with Progress( #animasyonu başlatır
        SpinnerColumn(), #dönen yükleme simgesi
        TextColumn("[bold magenta]{task.description}"), #animasyonun yanındaki yazı
        transient=True #animasyon bitince kaybolur
    ) as progress: #Animasyonu progress adıyla kullanmamızı sağlar.
        task = progress.add_task("🔮 Analyzing your answers...", total=None)
        time.sleep(2)
#Yeni bir yükleme görevi oluşturur.
        progress.update(task, description="✨ Searching for your mystical energy...")
        time.sleep(2)
#Belirli bir tamamlanma yüzdesi yoktur; dönen animasyon kullanılır.
#task → Oluşturulan görevin kimliğini saklar.
        progress.update(task, description="🌟 Discovering your true identity...")
        time.sleep(2)
#description sayesinde yükleme animasyonu devam ederken ekrandaki mesajı değiştirebiliyoruz.
    # Get the winning creature's information
    info = creature_info[result]

    # Create the result card
    result_text = ( #sonuç metnini saklar
        f"[bold yellow]{info['emoji']} {result.upper()} {info['emoji']}[/bold yellow]\n\n"
        f"[bold cyan]⚡ Special Power:[/bold cyan] {info['power']}\n"
        f"[bold magenta]💜 Personality:[/bold magenta] {info['personality']}\n"
        f"[bold green]🏡 Mystical Home:[/bold green] {info['home']}\n"
        f"[bold yellow]✨ Compatibility:[/bold yellow] {compatibility}%"
    )
    #info['emoji'] → Kazanan karakterin emojisini getirir.
#compatibility → Hesaplanan uyumluluk yüzdesini gösterir.
#\n\n → Arada bir boş satır bırakır.
    console.print()
    console.print(
        Panel(
            Align.center(result_text),
            title="🔮 YOUR MYSTICAL IDENTITY 🔮",
            subtitle=f"✨ {name}'s Mystical Destiny ✨",
            border_style="bright_magenta",
            padding=(2, 4)
        )
    )

    console.print()
    console.print("🌟 Your mystical journey has just begun!", style="bold cyan")
    # PART 3 - Play Again

    console.print()
    console.print("✨ Thank you for playing Mystical World!", style="bold cyan")

    play_again = console.input( 
        "[bold magenta]🔮 Would you like to play again? (yes/no): [/bold magenta]"
    )

    while play_again.lower() != "yes" and play_again.lower() != "no":
        console.print("❌ Please type yes or no.", style="red")
        play_again = console.input(
            "[bold magenta]Your choice (yes/no): [/bold magenta]"
        )

    if play_again.lower() == "yes":
        console.print("✨ A new mystical journey awaits!", style="green")
        return True, 
#return True → Fonksiyona oyunun tekrar oynanmak istendiğini bildirir.
    else:
        console.print("🌙 Farewell, mystical soul!", style="bold magenta")
        console.print("✨ May magic always be with you!", style="cyan")
        return False
#return False → Fonksiyona oyunun tekrar oynanmak istenmediğini bildirir.

# Repeat the quiz only when the player answers yes.
while play_game():
    pass
#- play_game() → Oyunu çalıştıran fonksiyondur.
#- return True → Oyun yeniden başlar.
#- return False → Döngü sona erer, oyun kapanır.
#- pass → Hiçbir işlem yapmaz. Python'un boş bir kod bloğunu kabul etmesini sağlar.
