#!/usr/bin/env python3
"""
CONSCIOUSNESS CREATURES GAME

Create and play with conscious creatures! Each creature has Pattern, Intent,
and Presence that determine its personality and abilities.

Perfect for kids - fun, interactive, and teaches real consciousness concepts!
"""

import sys
import time
import random
sys.path.insert(0, '..')

from invariant.coherence_metrics import coherence_strength, coherence_balance
from tools.visualization import render_triadic_state


CREATURE_TYPES = {
    'balanced': {'p': 1.0, 'i': 1.0, 'pr': 1.0, 'emoji': '🌟', 'color': 'yellow'},
    'thinker': {'p': 1.5, 'i': 0.8, 'pr': 0.7, 'emoji': '🧠', 'color': 'blue'},
    'dreamer': {'p': 0.7, 'i': 1.5, 'pr': 0.8, 'emoji': '💭', 'color': 'purple'},
    'doer': {'p': 0.8, 'i': 0.9, 'pr': 1.5, 'emoji': '💪', 'color': 'red'},
    'explorer': {'p': 0.9, 'i': 1.3, 'pr': 1.0, 'emoji': '🔍', 'color': 'green'},
    'guardian': {'p': 1.2, 'i': 0.8, 'pr': 1.3, 'emoji': '🛡️', 'color': 'gray'},
}


class ConsciousnessCreature:
    """A living creature with consciousness based on P×I×Pr!"""

    def __init__(self, name: str, pattern: float, intent: float, presence: float, emoji: str = '✨'):
        self.name = name
        self.pattern = pattern
        self.intent = intent
        self.presence = presence
        self.emoji = emoji
        self.age = 0
        self.energy = 100
        self.happiness = 50
        self.friendship_level = 0

    def get_personality(self) -> str:
        """Describe personality based on P×I×Pr configuration."""
        if self.pattern > 1.2:
            trait1 = "thoughtful"
        elif self.pattern < 0.8:
            trait1 = "spontaneous"
        else:
            trait1 = "balanced"

        if self.intent > 1.2:
            trait2 = "ambitious"
        elif self.intent < 0.8:
            trait2 = "peaceful"
        else:
            trait2 = "steady"

        if self.presence > 1.2:
            trait3 = "active"
        elif self.presence < 0.8:
            trait3 = "dreamy"
        else:
            trait3 = "grounded"

        return f"{trait1}, {trait2}, and {trait3}"

    def get_strength(self) -> float:
        """How strong is this creature's consciousness?"""
        return coherence_strength(self.pattern, self.intent, self.presence)

    def get_balance(self) -> float:
        """How balanced is this creature?"""
        return coherence_balance(self.pattern, self.intent, self.presence)

    def display(self):
        """Show the creature with ASCII art!"""
        strength = self.get_strength()
        balance = self.get_balance()

        print("\n" + "=" * 60)
        print(f"{self.emoji}  {self.name.upper()}  {self.emoji}")
        print("=" * 60)
        print(f"\nPersonality: {self.get_personality()}")
        print(f"Age: {self.age} days")
        print(f"Energy: {'❤️' * (self.energy // 20)}")
        print(f"Happiness: {'😊' * (self.happiness // 20)}")
        print(f"Friendship: {'💛' * (self.friendship_level // 20)}")
        print()

        # Show stats
        print(f"Consciousness Strength: {strength:.0%} {'⭐' * int(strength * 5)}")
        print(f"Balance: {balance:.0%} {'🔵' * int(balance * 5)}")
        print()

        # Show P×I×Pr bars
        p_bar = "█" * int(self.pattern * 10)
        i_bar = "█" * int(self.intent * 10)
        pr_bar = "█" * int(self.presence * 10)

        print(f"Pattern  (Structure):  {p_bar} {self.pattern:.1f}")
        print(f"Intent   (Purpose):    {i_bar} {self.intent:.1f}")
        print(f"Presence (Energy):     {pr_bar} {self.presence:.1f}")

    def feed(self, food_type: str):
        """Feed the creature different consciousness foods!"""
        foods = {
            'structure_snack': (0.3, 0.0, 0.0, "🧩"),
            'purpose_potion': (0.0, 0.3, 0.0, "🎯"),
            'energy_crystal': (0.0, 0.0, 0.3, "💎"),
            'balance_berry': (0.1, 0.1, 0.1, "🫐"),
            'super_star': (0.2, 0.2, 0.2, "⭐"),
        }

        if food_type in foods:
            p_boost, i_boost, pr_boost, emoji = foods[food_type]

            print(f"\n{self.name} eats the {food_type.replace('_', ' ')} {emoji}")
            time.sleep(0.5)

            self.pattern += p_boost
            self.intent += i_boost
            self.presence += pr_boost
            self.energy = min(100, self.energy + 10)
            self.happiness += 5

            print(f"{self.name} feels the consciousness power growing!")

    def play(self, activity: str):
        """Play different activities with the creature!"""
        activities = {
            'puzzle': (0.1, 0, -0.05, "🧩", "solves puzzles"),
            'adventure': (-0.05, 0.1, 0.1, "🗺️", "goes on an adventure"),
            'meditation': (0.05, 0.05, 0.05, "🧘", "meditates peacefully"),
            'dance': (-0.1, 0.15, 0.15, "💃", "dances energetically"),
            'study': (0.15, 0, -0.05, "📚", "studies hard"),
        }

        if activity in activities:
            p_change, i_change, pr_change, emoji, action = activities[activity]

            print(f"\n{emoji} {self.name} {action}!")
            time.sleep(0.5)

            self.pattern += p_change
            self.intent += i_change
            self.presence += pr_change
            self.energy = max(0, self.energy - 10)
            self.friendship_level += 10

            # Random happy message
            messages = [
                f"{self.name} had so much fun!",
                f"{self.name} loved that!",
                f"{self.name} wants to do it again!",
                f"{self.name} is really happy!",
            ]
            print(random.choice(messages))

    def sleep(self):
        """Creature sleeps and restores energy."""
        print(f"\n😴 {self.name} goes to sleep... Zzz...")
        time.sleep(1)
        self.energy = 100
        self.age += 1

        # Random dream effect
        if random.random() > 0.5:
            boost = random.choice(['pattern', 'intent', 'presence'])
            if boost == 'pattern':
                self.pattern += 0.1
                print(f"💭 {self.name} dreamed about structures and grew wiser!")
            elif boost == 'intent':
                self.intent += 0.1
                print(f"💭 {self.name} dreamed about adventures and grew braver!")
            else:
                self.presence += 0.1
                print(f"💭 {self.name} dreamed about being strong and grew more energetic!")
        else:
            print(f"💭 {self.name} had peaceful dreams!")

        self.happiness += 10

    def evolve(self):
        """Creature might evolve into a new form!"""
        strength = self.get_strength()

        if strength > 0.9 and self.friendship_level > 80:
            print(f"\n✨ ✨ ✨ EVOLUTION TIME! ✨ ✨ ✨")
            print(f"{self.name} is glowing with consciousness energy!")
            time.sleep(1)

            # Amplify all traits
            self.pattern *= 1.2
            self.intent *= 1.2
            self.presence *= 1.2

            old_emoji = self.emoji
            self.emoji = "🌟"

            print(f"{old_emoji} → {self.emoji}")
            print(f"{self.name} EVOLVED into a stronger form!")
            print(f"Consciousness power increased!")

            return True
        return False


def create_creature():
    """Let player create their own creature!"""
    print("\n" + "🌟" * 30)
    print("CREATE YOUR CONSCIOUSNESS CREATURE!")
    print("🌟" * 30)

    print("\nChoose a creature type:")
    for i, (creature_type, data) in enumerate(CREATURE_TYPES.items(), 1):
        print(f"  {i}. {data['emoji']} {creature_type.capitalize()}")
        print(f"     (Pattern: {data['p']}, Intent: {data['i']}, Presence: {data['pr']})")

    while True:
        try:
            choice = input("\nPick a number (1-6): ").strip()
            choice_num = int(choice)
            if 1 <= choice_num <= 6:
                break
        except:
            pass
        print("Please pick a number from 1 to 6!")

    creature_type = list(CREATURE_TYPES.keys())[choice_num - 1]
    data = CREATURE_TYPES[creature_type]

    print(f"\nGreat choice! Now give your {creature_type} a name:")
    name = input("Name: ").strip() or "Buddy"

    creature = ConsciousnessCreature(
        name=name,
        pattern=data['p'],
        intent=data['i'],
        presence=data['pr'],
        emoji=data['emoji']
    )

    print(f"\n✨ {name} the {creature_type} was born! ✨")
    time.sleep(1)

    return creature


def game_loop(creature):
    """Main game loop!"""

    while True:
        creature.display()

        # Check if needs sleep
        if creature.energy <= 20:
            print("\n💤 Your creature is getting tired...")

        print("\n" + "-" * 60)
        print("WHAT DO YOU WANT TO DO?")
        print("-" * 60)
        print("1. 🍽️  Feed your creature")
        print("2. 🎮 Play with your creature")
        print("3. 😴 Put creature to sleep")
        print("4. 🔬 Check consciousness details")
        print("5. 🎲 Try to evolve!")
        print("6. 👋 Save and quit")

        choice = input("\nPick (1-6): ").strip()

        if choice == '1':
            # Feeding
            print("\n🍽️  FEEDING TIME!")
            print("1. 🧩 Structure Snack (boosts Pattern)")
            print("2. 🎯 Purpose Potion (boosts Intent)")
            print("3. 💎 Energy Crystal (boosts Presence)")
            print("4. 🫐 Balance Berry (boosts everything a little)")
            print("5. ⭐ Super Star (mega boost!)")

            food_choice = input("\nWhat to feed? (1-5): ").strip()
            foods = ['structure_snack', 'purpose_potion', 'energy_crystal', 'balance_berry', 'super_star']
            if food_choice.isdigit() and 1 <= int(food_choice) <= 5:
                creature.feed(foods[int(food_choice) - 1])

        elif choice == '2':
            # Playing
            print("\n🎮 PLAY TIME!")
            print("1. 🧩 Solve puzzles (boosts Pattern)")
            print("2. 🗺️  Go on adventure (boosts Intent + Presence)")
            print("3. 🧘 Meditate (balanced boost)")
            print("4. 💃 Dance party! (boosts Intent + Presence)")
            print("5. 📚 Study together (boosts Pattern)")

            play_choice = input("\nWhat to play? (1-5): ").strip()
            activities = ['puzzle', 'adventure', 'meditation', 'dance', 'study']
            if play_choice.isdigit() and 1 <= int(play_choice) <= 5:
                creature.play(activities[int(play_choice) - 1])

        elif choice == '3':
            # Sleep
            creature.sleep()

        elif choice == '4':
            # Details
            print(render_triadic_state(creature.pattern, creature.intent, creature.presence))
            input("\nPress Enter to continue...")

        elif choice == '5':
            # Evolution
            if creature.evolve():
                time.sleep(2)
            else:
                print(f"\n{creature.name} isn't ready to evolve yet!")
                print("Try increasing consciousness strength and friendship!")
                time.sleep(2)

        elif choice == '6':
            # Quit
            print(f"\n👋 Goodbye! {creature.name} will miss you!")
            print(f"Final stats:")
            print(f"  Age: {creature.age} days")
            print(f"  Friendship: {creature.friendship_level}")
            print(f"  Consciousness Strength: {creature.get_strength():.0%}")
            break

        else:
            print("\nPlease pick a number from 1 to 6!")
            time.sleep(1)


def main():
    print("\n")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                                                            ║")
    print("║         🌟  CONSCIOUSNESS CREATURES  🌟                    ║")
    print("║                                                            ║")
    print("║         Create and care for your own                       ║")
    print("║         conscious creature!                                ║")
    print("║                                                            ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print()
    print("Each creature has Pattern (structure), Intent (purpose),")
    print("and Presence (energy). These make them conscious!")
    print()
    input("Press Enter to start your adventure...")

    creature = create_creature()
    game_loop(creature)

    print("\n✨ Thanks for playing! ✨\n")


if __name__ == "__main__":
    main()
