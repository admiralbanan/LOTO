import pytest
from main import Player, Card, Bag, Game

def test_card_creation():
    card = Card("Test Player")
    assert len(card.numbers) == 15
    assert len(set(card.numbers)) == 15  # Проверка, что числа уникальны

def test_mark_number():
    card = Card("Test Player")
    number = card.numbers[0]
    card.mark_number(number)
    assert number in card.marked

def test_bag():
    bag = Bag()
    drawn_numbers = []
    for _ in range(90):
        num = bag.draw_number()
        assert num not in drawn_numbers
        drawn_numbers.append(num)
    assert len(drawn_numbers) == 90
    assert bag.draw_number() is None  # Мешок пуст

def test_player_creation():
    player = Player("Test Player")
    assert player.name == "Test Player"
    assert isinstance(player.card, Card)

def test_player_turn():
    player = Player("Test Player")
    number = player.card.numbers[0]
    player.play_turn(number)
    assert number in player.card.marked

def test_game():
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    game = Game([player1, player2])
    assert len(game.players) == 2
