names = ["Alex", "Maya", "Leo", "Nora", "Kai"]
classes = ["Warrior", "Mage", "Archer", "Rogue"]
weapons = ["Sword", "Bow", "Staff", "Dagger"]
print("===== RANDOM CHARACTER =====")
import random
name = random.choice(names)
class1 = random.choice(classes)
weapon = random.choice(weapons)
level= random.randint(1, 50)
print(f"{'Name':<12}:{name}")
print(f"{'Class':<12}:{class1}")
print(f"{'Weapon':<12}:{weapon}")
print(f"{'Level':<12}:{level}")
print("="*25)