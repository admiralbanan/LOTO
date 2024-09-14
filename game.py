import random

class Card:
    def __init__(self, name):
        self.name = name
        self.numbers = self.generate_card()
        self.marked = set()

    def generate_card(self):
        return random.sample(range(1, 91), 15)

    def mark_number(self, number):
        if number in self.numbers:
            self.marked.add(number)

    def is_winner(self):
        return len(self.marked) == len(self.numbers)

    def display(self):
        print(f"{self.name}'s Card: {self.numbers}")
        print(f"Marked: {sorted(self.marked)}")

class Bag:
    def __init__(self):
        self.numbers = list(range(1, 91))
        random.shuffle(self.numbers)

    def draw_number(self):
        return self.numbers.pop() if self.numbers else None

class Player:
    def __init__(self, name, is_human=True):
        self.name = name
        self.is_human = is_human
        self.card = Card(name)

    def play_turn(self, drawn_number):
        if drawn_number in self.card.numbers:
            self.card.mark_number(drawn_number)
            print(f"{self.name} marked {drawn_number}!")
        else:
            print(f"{self.name} did not mark {drawn_number}.")

    def has_won(self):
        return self.card.is_winner()

class Game:
    def __init__(self, players):
        self.bag = Bag()
        self.players = players

    def play(self):
        while True:
            input("\nНажмите Enter для вытягивания бочонка...")
            drawn_number = self.bag.draw_number()
            if drawn_number is None:
                print("No more numbers in the bag!")
                break
            print(f"\nNumber drawn: {drawn_number}")

            for player in self.players:
                player.play_turn(drawn_number)
                player.card.display()
                if player.has_won():
                    print(f"\n{player.name} wins!")
                    return

def get_player_count():
    while True:
        try:
            count = int(input("Введите количество настоящих игроков: "))
            if count >= 1:
                return count
            else:
                print("Число должно быть 1 или больше.")
        except ValueError:
            print("Ошибка: введите корректное число.")

def get_computer_count():
    while True:
        try:
            count = int(input("Введите количество компьютерных игроков: "))
            if count >= 0:
                return count
            else:
                print("Число должно быть 0 или больше.")
        except ValueError:
            print("Ошибка: введите корректное число.")

if __name__ == "__main__":
    player_count = get_player_count()
    computer_count = get_computer_count()

    players = []
    for i in range(player_count):
        name = input(f"Введите имя игрока {i + 1}: ")
        players.append(Player(name, is_human=True))

    for i in range(computer_count):
        players.append(Player(f"Компьютер {i + 1}", is_human=False))

    game = Game(players)
    game.play()
