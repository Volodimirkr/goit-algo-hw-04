def total_salary(path):
    try:
        with open(path, "r") as fh:
            lines = fh.readlines()
            total_sallary = 0
            avarage_sallary = 0
            for line in lines:
                name, sellary = line.strip().split(",")
                total_sallary += int(sellary)
            avarage_sallary = total_sallary // len(lines)
            return total_sallary,avarage_sallary 
    except FileNotFoundError:
        print("File not found")

total, average = total_salary("dz4.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
