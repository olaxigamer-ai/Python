import numpy  as np

data_type=[('name','S15'),('class',int),('height',float)]

student_detail=[('James',5,48.5),('Niel',4,52.2),('Robert',2,49.7),('Alex',1,57.3)]

student=np.array(student_detail,data_type)
print(student)

sort=np.sort(student,order='class')
print(sort)