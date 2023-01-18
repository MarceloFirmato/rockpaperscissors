# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇




#print(student_heights)
#print(n)

soma = 0
for m in student_heights:
   soma += m

#print(soma)

media = soma / (n+1)

print(int(round(media, 0)) )