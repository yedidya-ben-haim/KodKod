# region Part 1

def create_grades_file(filename):
    students = [
        ("Dan", [85, 90, 78]),
        ("MOMO", [92, 88, 95]),
        ("Yoni", [70, 65, 80]),
        ("Avi", [100, 95, 98]),
        ("Sara", [60, 72, 68]),
        ]
    with open("grades.txt", "w") as file:
        for name, grade in students:
            line = f"{name},{grade[0]},{grade[1]},{grade[2]}\n"
            file.write(line)

# endregion

# region Part 2

def calculate_averages(filename):
    """
    קוראת את grades.txt, ומחשבת ממוצע לכל סטודנט
    מחזיר:
    dict: {שם: ממוצע}
    """
    averages = {}

    with open("grades.txt", "r") as file:
        for line in file:
            line = line.strip().split(",")

            name = line[0]
            grade1 = float(line[1])
            grade2 = float(line[2])
            grade3 = float(line[3])

            student_average = (grade1 + grade2 + grade3) / 3

            averages[name] = student_average

    return averages

results = calculate_averages('grades.txt')
for name, avg in results.items():
    print(f'{name}: {avg:.1f}')

# endregion

# region Part 3

def save_results(averages, output_filename):
    '''
    כותבת לקובץ output_filename:
    שורה ראשונה: כותרת
    שורות הבאות:שם וממצוע
    ממוין מגבוה לנמוך
    '''

    inverted_list = []
    for name, avg in averages.items():
        inverted_list.append((avg, name))

    inverted_list.sort(reverse=True)

    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write("=== Student Results ===\n")

        counter = 1

        for avg, name in inverted_list:
            file.write(f"{counter}. {name}: {avg:.1f}\n")

            counter += 1




averages = calculate_averages('grades.txt')
save_results(averages, 'results.txt')