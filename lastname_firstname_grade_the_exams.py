import collections
from typing import Counter


#ham de xu li file
def show_output(file):
    print(f"Successfully opened {filename}")
    lines = file.readlines()
    # (count) dem so ky tu trong 1 dong
    count = 0
    # dem so luong dong chuan format
    total = 0
    #dem tong so dong trong file
    count_line = 0
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    answer_key = answer_key.split(',')
    #list chua answer_key
    answer = list(answer_key)
    #list chua cac dong answer chuan format
    student_answer = list()
    #list chua cac cau bi khoanh sai
    wrong_student = list()
    #list chua cac ma sinh vien 
    msv = list()

    print("**** ANALYZING ****")
    for line in (lines):
        count_line += 1
        # cat chuoi xoa bo \n 
        line = line[:len(line)-1]
        
        for words in line:
            if words == ",":
                count+=1
        if count==25:
            total+=1
        #thieu values
        elif count!=25:
            print(f"Invalid line of data: does not contain exactly 26 values:")
            print(line) 
            wrong_student.append(line)
        #sai dinh dang #N...
        if (line[1:8].isnumeric()==False) or (line[9] != ","):
            total-=1
            print(f"Invalid line of data: N# is invalid:")
            print(line)
            wrong_student.append(line)
        # nhan cac dong khong bi loi format hay thieu values
        if line not in wrong_student:
            student_answer.append(line)
            # cat chuoi lay chuoi o dau , dau tien
            msv.append(line[:9])
        count=0

    #task 3
    # tổng điểm từng sinh viên
    grade = 0
    # list chua diem cua cac sinh vien
    list_grade = list()
    # list chua cac cau sinh vien khong khoanh
    question_pass = list()
    # list chua cac cau sinh vien khoanh sai
    wrong = list()
    # print(student_answer)
    for i in student_answer:
        k = 0
        #loai bo dau , ra khoi chuoi
        i = i.rsplit(",")
        #loai bo ma sinh vien ra khoi chuoi
        i = (i[1:])
        for x in range(0,25):
            #khoanh dung
            if answer[x] == i[k]:
                grade += 4
            #khong khoanh
            elif i[k] == "":
                question_pass.append(k)
                grade += 0
            #khoanh sai
            else:
                wrong.append(k)
                grade -= 1
            k+=1
             
        list_grade.append(grade)
        grade = 0


    list_grade_copy = list_grade
    #so hoc sinh gioi
    csg = 0
    #gia tri trung binh
    mean_avg = 0
    #diem cao nhat
    highest_score = max(list_grade)
    #diem thap nhat
    lowest_score = min(list_grade)
    #khoang cach giua so lon nhat va nho nhat
    range_score = highest_score - lowest_score
    #sap xep danh sach diem cua cac sinh vien
    list_grade = sorted(list_grade)
    #diem trung vi
    median_score = 0

    x = int(len(list_grade)/2)
    #len(list_grade) le
    if len(list_grade) % 2 == 1:
        median_score = list_grade[x]
    #len(list_grade) chan
    else:
        median_score = float(list_grade[x-1] + list_grade[x])/2
    #tim so hoc sinh gioi va diem trung binh cua cac sinh vien
    for count_student_grade in list_grade:
        if count_student_grade > 80:
            csg += 1
        mean_avg += float((count_student_grade)/len(list_grade))   
    
    #dem tan suat so cau khong khoanh cua sinh vien
    d = Counter(question_pass)
    d = dict(sorted(d.items()))
    #lay gia tri so lan khong khoanh cau nhieu nhat cua sinh vien
    dmax = max(d.values())
    pass_anwser = list()
    for k,v in d.items():
        if v == dmax:
            #luu gia tri cau khong khoanh nhieu nhat cua sinh vien
            pass_anwser.append(k)

    #dem tan suat so cau khoanh sai cua sinh vien
    d1 = Counter(wrong)
    d1 = dict(sorted(d1.items()))
    #lay gia tri so lan khoanh sai cau nhieu nhat cua sinh vien
    dmax_wrong = max(d1.values())
    wrong_anwser = list()

    for k,v in d1.items():
        if v == dmax_wrong:
            #luu gia tri cau khoanh sai nhieu nhat cua sinh vien
            wrong_anwser.append(k)
   
    #task 4:
    
    txt1 = list()
    txt = str()
    j = 0
    #noi 2 chuoi voi nhau
    for i in msv:
        txt = i  + "," +str(list_grade_copy[j]) +"\n"
        j+=1
        #luu tru chuoi vua noi vao list
        txt1.append(txt)
    #viet ra file
    with open(f"{filename[:6]}_grades.txt", "w") as file:
        file.writelines(txt1)
          

    #print
    print("**** REPORT ****")
    print(f'Total valid lines of data: {total}')
    print(f"Total invalid lines of data: {count_line-total}")
    print(f"Total student of high scores: {round(csg,2)}")
    print(f"Mean (average) score: {round(mean_avg,2)}")
    print(f"Highest score: {highest_score}")
    print(f"Lowest score: {lowest_score}")
    print(f"Range of scores: {range_score}")
    print(f"Median score: {round(median_score,3)}")

    print("Question that most people skip: ", end="")
    for i in range(0, len(pass_anwser)):
        print(f"{pass_anwser[i]+1} - {dmax} - {round(dmax/total,2)}", end=", ")
    print("")
    print("Question that most people answer incorrectly: ", end="")
    for i in range(0, len(wrong_anwser)):
        print(f"{wrong_anwser[i]+1} - {dmax_wrong} - {round(dmax_wrong/total,2)}", end=", ")

    print("")
    # neu anwser cua sinh vien ko co ai bi sai format hoac thua values
    if total == count_line:
        print("No errors found!")


#bat loi nhap Y or N
def getYorN():
    while True:
        try:
            s = input("")
            if s == "Y" or s == "N":
                return s
            else:
                z = 5 / 0
        except(Exception):
            print("Please enter Y or N: ", end = "")
            
            
# bat loi cua file
while True:
    try:
        filename = input("Enter a filename: " ) + ".txt"
        file = open(filename, 'r')
        show_output(file)
        #muon tiep tuc thi nhan Y
        print("Do you want continue:(Y/N) ", end="")
        if(getYorN() == "N" ):
            break
    except(FileExistsError, FileNotFoundError): 
        print("Sorry, File cannot be found.")
    
