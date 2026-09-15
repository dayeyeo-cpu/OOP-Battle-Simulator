from hero import Hero

from goblin import Goblin


ARENA_NAME = "The Labubu Realm"

 
"""Have the Hero attack one Goblin. Save the returned damage in a variable.
    Pass that damage to the Goblin's take_damage() method.
    If the Goblin is still alive, allow it to attack the Hero once."""

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        heroAttack = hero.attack()
        enemy.take_damage(heroAttack)

        if enemy.is_alive():
            enemy_Comeback = enemy.attack()
            hero.take_damage(enemy_Comeback)

    if hero.is_alive():
        print(f"{hero.name} wins! ")

    else:
        print(f"{enemy.name} wins! ")

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Tripe T")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    secondgoblin = Goblin("Labubu")
    hero = Hero("BIBBLE")

    battle(hero, goblin)

    print(f"{secondgoblin.name} enters the arena with {secondgoblin.health} health.")

    print(f"{hero.name} enters the arena with {hero.health} health.")
    
    
if __name__ == "__main__":
    main()

