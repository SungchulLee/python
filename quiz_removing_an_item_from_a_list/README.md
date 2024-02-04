# removing an item from a list

Task: Remove items of the list a which are also members of another list b.

Below is a code with bugs. Fix the code:

```
a = [1,2,3,4]
b = [1,2,5,6]

for item in a:
    if item in b:
        a.remove(item)

print(a) # [2, 3, 4]
``` 