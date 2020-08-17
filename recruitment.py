def main():
	#write your code here
	skills =["1. Python","2. C++","3. Javascript","4. Juggling","5. Running","6. Eating"]
cv={}
print("Welcome to the special recruitment program, please answer the following questions:")
cv["name"]= input("What's your name?")
cv["age"]= input("How old are you?")

cv["experience"]= input("How many years of experience do you have?")
cv["skills"] = []
#cv={"name":,"age":, "experience":,"skills":[]}
#for x in skills:
 # print(x)
skills =["1. Python","2. C++","3. Javascript","4. Juggling","5. Running","6. Eating"]

print("skills:")
print(skills[0])
print(skills[1])
print(skills[2])
print(skills[3])
print(skills[4])
print(skills[5])

#print(skills)
s=input("Choose a skill from above by entering its number:")
s=int(s)
cv["skills"]=skills[s-1]
s2=input("Choose another skill from above by entering its number:")
s2=int(s2)
cv["skills"]=skills[s2-1]
#print(cv["skills"])
if int(cv["age"])>=25 and int(cv["age"])<=40 and int(cv["experience"])>5 and "6.Eating" in cv["skills"] :
	 print("You have been accepted,"+cv["name"])
	 #"apple" in thislist
else:
	 print("reject")

if __name__ == '__main__':
	main()
