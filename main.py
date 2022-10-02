# from Final1 import Course
#
# course_list = []
#
# def find_course(course_name, courses):
#
#     index = 0
#     for i in courses:
#         if i.course_name in course_name:
#             return index
#     return -1
#
# while True:
#     x = int(input("1. Create Course\n2. Print Courses List\n3. Find Course\n4. Exit"))
#
#     if x == 1:
#         course_name = input("Enter Course Name: ")
#         course_class = None
#         while True:
#             course_class = input("Select Course Class (A-B-C)")
#             if course_class in ["A", "B", "C"]:
#                 break
#         course = Course(course_name,course_class)
#         course_list.append(course)
#         print("Course Created Successfully")
#     elif x == 2:
#         print("---------------------------")
#         print("Course Name \t\t|Course Class")
#         print("---------------------------")
#         for i in course_list:
#             print(i.course_name, "\t\t|",i.course_class)
#     elif x == 3:
#         course_name = input("Enter Course Name: ")
#         course_index = find_course(course_name, course_list)
#         if course_index == -1:
#             print("Course Does Not Exist!")
#         else:
#             print(course_list[course_index].course_name, "\t\t",course_list[course_index].course_class )
#     elif x == 4:
#         exit()




from Final1 import Course
#
# course_list = []
#
# class Student(Course):
#
#     def __init__(self):
#         super().__init__()
#         self.student_name = input("Enter Student Name: ")
#         self.student_id =
#
#
