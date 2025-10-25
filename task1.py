def total_and_average_salary (): 
    with open("salary_file.txt", 'r', encoding='utf-8') as file:

        # Виявляємо зарплати і готуємо їх до обчислень
        salaries = []
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                salaries.append(float(parts[1]))

    #Робимо необхідні обчислення
    total = sum(salaries)
    average = total / len(salaries) if salaries else 0
    
    return total, average

total, average = total_and_average_salary()


print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
