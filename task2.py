def get_cats_info(path):
    with open(path, 'r', encoding='utf-8') as file:
        cats_info = []
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                id, name, age = parts
                cats_info.append({
                    'id': id.strip(),
                    'name': name.strip(),
                    'age': age.strip()
                })
    return cats_info


# Виклик функції:
cats_info = get_cats_info("cats_file.txt")
print(cats_info)