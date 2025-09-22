# ============================================
#   🎯 Mini Project: Even-Odd Number Sorter
#   Author: Your Name
#   Description: Sorts numbers into Even & Odd
# ============================================

import time

def print_header():
    print("╔" + "═"*48 + "╗")
    print("║{:^48}║".format("✨ EVEN-ODD NUMBER SORTER ✨"))
    print("╚" + "═"*48 + "╝")

def print_footer():
    print("╔" + "═"*48 + "╗")
    print("║{:^48}║".format("🎉 Thank you for using the Sorter! 🙌"))
    print("╚" + "═"*48 + "╝")

# --- Main Program ---
print_header()
time.sleep(0.5)
# Input
num = []
size = int(input("\n🔢 Enter how many numbers you want to add: "))

for i in range(size):
    elem = int(input(f"👉 Enter number {i+1}: "))
    num.append(elem)

# Display original numbers
print("\n📜 Original Number List:")
print(" ".join(map(str, num)))
print("─"*50)

# Separate into evens and odds
evennum = sorted([i for i in num if i % 2 == 0])
oddnum = sorted([i for i in num if i % 2 != 0])

# Display evens
print("\n🔵 Even Numbers")
print("─"*50)
if evennum:
    print(" ".join(map(str, evennum)))
    print(f"✅ Total Even Numbers: {len(evennum)}")
else:
    print("❌ No even numbers found!")

# Display odds
print("\n🔴 Odd Numbers")
print("─"*50)
if oddnum:
    print(" ".join(map(str, oddnum)))
    print(f"✅ Total Odd Numbers: {len(oddnum)}")
else:
    print("❌ No odd numbers found!")

print()
print_footer()