"""
Docstring for Lab3_xenzonz_replace
i. LAB 3: Working with a list
ii. Sam Cocquyt
iii. Import modified list, replace a middle item with 'binoculars' then print slices
iv. No starter code
v. 2/1/2026
"""

# import modified list with 5 new items
from Lab3_xenzonz_add import camping_items

# middle index
replace_index = len(camping_items) // 2 
camping_items[replace_index] = "binoculars"

# binoculars location in index
binoculars_index = camping_items.index("binoculars")

# main guard
if __name__ == "__main__":
    # slice before binoculars
    print(f"Items before binoculars, not including binoculars:")
    print(camping_items[:binoculars_index])

    # slice containing only binoculars
    print(f"Binoculars:")
    print(camping_items[binoculars_index:binoculars_index + 1])

    #slice after binoculars
    print(f"Items after binoculars, not including binoculars:")
    print(camping_items[binoculars_index + 1:])

