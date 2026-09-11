from goblin import Goblin


ARENA_NAME = "The Labubu Realm"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Tripe T")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    secondgoblin = Goblin("Labubu")
    
    print(f"{secondgoblin.name} enters the arena with {secondgoblin.health} health.")
    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()
