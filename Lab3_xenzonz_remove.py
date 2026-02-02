"""
Docstring for Lab3_xenzonz_remove
i. LAB 3: Working with a list
ii. Sam Cocquyt
iii. Import further modified list, remove binoculars, print final list, and print total items
iv. No starter code
v. 2/1/2026
"""
# import further modified list
from Lab3_xenzonz_replace import camping_items

# remove binoculars in list
if "binoculars" in camping_items:
    camping_items.remove("binoculars")

# main guard
if __name__ == "__main__":
    print(f"Final list:")
    # final resulting list
    print(f"{camping_items}")
    # total items using len()
    print(f"Total items being brought to the camping trip: {len(camping_items)}")
