available_spots, students = (int(input()), [])
department_dict = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
exam_id = {"Physics": ["P", "M"], "Chemistry": ["C"], "Mathematics": ["M"], "Engineering": ["CS", "M"], "Biotech": ["C", "P"]}
with open("applicants.txt", "r") as file:
    for line in file:
        line = line.split()
        students.append({"name": f"{line[0]} {line[1]}", "P": int(line[2]), "C": int(line[3]), "M": int(line[4]),
                         "CS": int(line[5]), "AES": int(line[6]), "p1": line[-3], "p2": line[-2], "p3": line[-1]})
student_list_copy = list(students)
for n in range(1, 4):
    for field in department_dict:
        student_list_copy.sort(key=lambda s: (-(max(sum([s[exam_id[field][x]] for x in range(len(exam_id[field]))]) / len(exam_id[field]), s["AES"])), s["name"]))
        students = list(student_list_copy)
        for student in students:
            if (len(department_dict[field]) < available_spots) and (student[f"p{n}"] == field):
                department_dict[field].append(student_list_copy.pop(student_list_copy.index(student)))
for field, approved_list in department_dict.items():
    file = open(f"{field}.txt", "w")
    approved_list.sort(key=lambda s: (-(max(sum([s[exam_id[field][x]] for x in range(len(exam_id[field]))]) / len(exam_id[field]), s["AES"])), s["name"]))
    for s in approved_list:
        file.write(f"{s['name']} {(max(sum([s[exam_id[field][x]] for x in range(len(exam_id[field]))]) / len(exam_id[field]), s['AES']))}\n")
    file.close()