def cat_info(): 
    with open("cats_file", 'r', encoding='utf-8') as file:

        # Виявляємо інформацію про котів і готуємо її до обробки
        cats_info = []
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                id, name, age = parts

        # Формуємо список з інформацією про котів
                cats_info.append({
                    'id': id.strip(),
                    'name': name.strip(),
                    'age': int(age.strip()),
                })
    
    return cats_info

cats_info = cat_info()
print(cats_info)