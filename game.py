from hero import Hero

from goblin import Goblin


ARENA_NAME = "The Labubu Realm"

 
"""Have the Hero attack one Goblin. Save the returned damage in a variable.
    Pass that damage to the Goblin's take_damage() method.
    If the Goblin is still alive, allow it to attack the Hero once."""

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Tripe T")
    secondgoblin = Goblin("Labubu")
    hero = Hero("BIBBLE")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    
    print(f"{secondgoblin.name} enters the arena with {secondgoblin.health} health.")

    print(f"{hero.name} enters the arena with {hero.health} health.")


    bibble = Hero("BIBBLE)")
    heroAttack = bibble.attack()
    goblin.take_damage(heroAttack)

    print("Bibble attacks ")
    tt = Goblin("Tripe T")
    goblinAttack = tt.attack()
    print("Tripe T a")
    hero.take_damage(goblinAttack)
if __name__ == "__main__":
    main()
