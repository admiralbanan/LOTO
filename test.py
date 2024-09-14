import pytest
from loto import Player, Card, Bag, Game

def test_card_creation():
    card = Card("Test Player")
    assert len(card.numbers) == 15
    assert len(set(card.numbers)) == 15  # Проверка уникальности

def test_card_eq():
    card1 = Card("Player 1")
    card2 = Card("Player 1")
    assert card1 != card2  # Так как карточки разные

def test_card_str():
    card = Card("Player 1")
    assert str(card).startswith("Card(Player 1):")

def test_player_creation():
    player = Player("Test Player")
    assert player.name == "Test Player"
    assert isinstance(player.card, Card)

def test_player_eq():
    player1 = Player("Player 1")
    player2 = Player("Player 1")
    assert player1 != player2  # Разные карточки

def test_player_str():
    player = Player("Player 1")
    assert str(player) == "Player(Player 1, Human: True)"

def test_bag():
    bag = Bag()
    drawn_numbers = []
    for _ in range(90):
        num = bag.draw_number()
        assert num not in drawn_numbers
        drawn_numbers.append(num)
    assert len(drawn_numbers) == 90
    assert bag.draw_number() is None  # Мешок пуст

def test_bag_eq():
    bag1 = Bag()
    bag2 = Bag()
    assert bag1 != bag2  # Разные списки чисел

def test_bag_str():
    bag = Bag()
    assert str(bag).startswith("Bag(90 remaining numbers)")

def test_game():
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    game = Game([player1, player2])
    assert len(game.players) == 2

def test_game_str():
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    game = Game([player1, player2])
    assert str(game) == "Game with players: Player 1, Player 2"

def test_game_eq():
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    game1 = Game([player1, player2])
    game2 = Game([player1, player2])
    assert game1 != game2  # Разные карточки
