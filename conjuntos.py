set_a = set(['Red', 'Blue', 'Green', 'Black'])
set_b = set(['Black', 'Green', 'Yellow', 'Orange'])
set_x = set_a.union(set_b)
set_y = set_a.intersection(set_b)
set_z = set_a.difference(set_b)

print(f'{set_x} \n{set_y} \n{set_z}')
print(set_a.issuperset(set_y))
print(set_a.issubset(set_x))

set_a.add('Purple')
print(set_a.issubset(set_x))
print(set_a)