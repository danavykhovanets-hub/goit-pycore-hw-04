def total_salary(path):
    with open(path, 'r', encoding='utf-8') as file:
        salaries = []
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                salaries.append(float(parts[1]))

    total = sum(salaries)
    average = total / len(salaries) if salaries else 0
    return total, average


# Виклик функції:
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
