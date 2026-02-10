import pandas as pd

semesterTable = {
 'Subject' : ['math' , 'English' , None , 'social studies' , None, 'Physics' , 'Chemistry' , 'Biology'] , 'Classroom' : [220 , 450 , 'GYM' , 225 , 100 , 125 , 115 , 116] 
 ,'Semeseter' : ['1&2' , None , '1&2' , None, 2 , 1 , 2 , None] 
 , 'Day' : [1 ,2 ,1 , 2 ,1 , 2 , 3 , 1 ]
}
frame = pd.DataFrame(semesterTable)
print(frame)
newF = frame.dropna()
print(newF.to_string())

