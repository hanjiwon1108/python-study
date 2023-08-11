### 객체 지향 프로그램 도입의 필요성 ###

# 학생 정보를 전달하는 student_info() 함수
# 이름, 학년, 반, 전화번호, 주소, 성적

def student_info(name, grade, class_number, phone_number, address, score):
    # 학생정보를 print()으로 출력
    # VSC 기능: alt + shift + 방향키
    print(name)
    print(grade)
    print(class_number)
    print(phone_number)
    print(address)
    print(score)

# stuent_info() 함수를 사용하여 학생을 생성
name1 = 'Lee Seung Ah'
grade1 = 3
class_number1 = 2
phone_number1 = "010-1111-2222"
address1 = "부산시 부산진구"
score1 = 85

# student_info(name1, grade1, class_number1, phone_number1, address1, score1)

# 클래스를 이용한 학생 관리 #
# class Student:
#     def __init__(self, name, grade,  class_number, phone_number, address, score):
#         self.name = name
#         self.grade = grade
#         self.class_number = class_number
#         self.phone_number = phone_number
#         self.address = address
#         self.score = score

# student1 = Student('이승아', 3, 2, '010-1111-2222', '부산시', '부산진구', 85)
# student2 = Student('이준국', 3, 2, '010-1111-2222', '부산시', '부산진구', 85)
# student3 = Student('이도경', 3, 2, '010-1111-2222', '부산시', '부산진구', 85)
# student4 = Student('이주현', 3, 2, '010-1111-2222', '부산시', '부산진구', 85)

# print(student1)
# print(student2)
# print(student3)
# print(student4)
