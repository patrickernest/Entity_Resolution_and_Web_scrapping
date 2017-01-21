###############################################################################
###############################################################################

# Question 1 : Entity Resolution - UIC Courses  - query.py

###############################################################################

import sys
import fileinput
import string

###############################################################################

# After we have obtained our cleaned.txt file, we run the query file by using 
# the command python3 query.py cleaned.txt . In this code file we generally
# are querying data from our cleaned.txt data. In q1, we find the distinct courses.
# In q2, we find the course taught by Professor Mitchell Theys. In q3, we find the
# two professors whose interests are closely aligned. 

###############################################################################

def run():
	arr = [] 
	for stri in fileinput.input():
		stri=stri.strip()
		arr.append(stri)
	prof = []
	cours = []
	for i in arr:
		ies=i.split(" - ")
		prof.append(ies[0])
		cours.append(ies[1])
	pl2=len(cours)
	c_final = []
	for i in range(0,pl2):       
		c_final.append([])
	for i in range(0,pl2):
		c_ss=cours[i].split("|")                                
		xy=len(c_ss)                                
		for k in range(0,xy):
			c_final[i].append(c_ss[k])
	q1(c_final)
	q2(prof,c_final)
	q3(prof,c_final)

###############################################################################

# In the function q1, we find the distinct courses that exist in the obtained
# cleaned.txt file.

###############################################################################
	
def q1(cf):
	cf_1=[]
	for i in range(0,len(cf)):
		for j in range(0,len(cf[i])):
			cf_1.append(cf[i][j])
	cf_1_u=set(cf_1)
	cf_uni=list(cf_1_u)
	cf_len=len(cf_uni)
	print ("")
	print ("1: How many distinct courses does this dataset contain?")
	print ("")
	print ("Answer: ",cf_len)
	print ("")

##############################################################################

# In the function q2, we find the courses that are being taught by Professor 
# Mitchell Theys. The courses are already arranged in alphabetical order in 
# the cleaned.txt file therefore it is not required for us order here.

##############################################################################

def q2(pr,cf):
	print ("2: List all the courses (in alphabetical order) taught by Professor Mitchell Theys in comma‐separated form.")
	print ("")
	print ("Answer:")
	print ("")
	for i in range(0,len(cf)):
		if pr[i]=="Theys":
			for j in range(0,len(cf[i])):
				if j==(len(cf[i])-1):
					print (cf[i][j])
				else:
					print (cf[i][j]+",",end='')
	print ("")

#############################################################################

# In the function q3, we find the two professors among the professors who teach
# at-least 5 courses. From that we use Jaccard Similarity as mentioned in the 
# question to determine which two professors have their interests closely aligned.

#############################################################################

def q3(pr,cf):
	prn=[]
	cfn=[]
	for i in range(0,len(pr)):
		if len(cf[i])>4:
			prn.append(pr[i])
			cfn.append(cf[i])
	jdist,pro_n=jsend(prn,cfn)
	index=jdist.index(max(jdist))
	print ("3: For professors who have taught at least 5 courses, using Jaccard distance to determine which two professors have the most aligned teaching interests based on course titles. Note that you should implement the function to calculate Jaccard distance instead of using an existing package.")
	print ("")
	print ("Answer:")
	print ("")
	print ("Given below are the list of professors who have taught at least 5 courses:-")
	print ("")
	l=len(prn)
	for i in range(0,l):
		print (i+1,")",prn[i])
	print ("")
	print ("The two professors who have aligned teaching interests are:-")
	print ("")
	l2=len(pro_n[index])
	for i in range(0,l2):
		print (i+1,")",pro_n[index][i])
		if i!=l2-1:
			print ("AND")
		
	print ("")

#############################################################################

# In the next there functions jsend(), jacc() and jcomp(), we calculate the 
# Jaccard Similarity between the corresponding professors. And then return
# the Jaccard Similarity values.

#############################################################################

def jsend(pr,cf):
	jdist=[]
	pro_n=[]	
	l=len(cf)
	for i in range(0,(len(cf)-1)):
		for j in range(i+1,len(cf)):
			jd=jacc(cf[i],cf[j])
			jdist.append(jd)
			pro_n.append([pr[i],pr[j]])
	return jdist,pro_n
			

def jacc(s1,s2):
	l1=len(s1)
	l2=len(s2)
	dist=0
	#c=0
	dist=jcomp(s1,s2)
	return dist

def jcomp(s1,s2):
	nc1=set(s1).intersection(s2)
	nc2=list(nc1)
	nc=len(nc2)
	na=len(s1)
	nb=len(s2)
	t=nc/(na+nb-nc)
	return t
	
if __name__ == '__main__':
	run()          
