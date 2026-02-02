"""
Docstring for Lab3_xenzonz_add
i. LAB 3: Working with a list
ii. Sam Cocquyt
iii. Import list, append 5 more items, and print the list reversed alphabetically
iv. No starter code
v. 2/1/2026
"""

# import list from the list file
from Lab3_xenzonz_list import camping_items

# add items using append
camping_items.append("compass")
camping_items.append("battery bank")
camping_items.append("cookware")
camping_items.append("shotgun")
camping_items.append("camp chair")

# main guard
if __name__ == "__main__":
    print(f"Added items and list reversed alphabetically:")
    print(sorted(camping_items, reverse=True))