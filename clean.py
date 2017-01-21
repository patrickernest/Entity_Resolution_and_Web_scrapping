########################################################################
########################################################################

# Question 1 : Entity Resolution - UIC Courses - clean.py

########################################################################

import sys
import fileinput
import enchant
import string

#########################################################################

# Initially we fisrt get the input of the file while run the command
# python3 clean.py class.txt .
# After we get all the data of that is there in the file class.txt
# we parse through every line a seperate the professor and corresponding 
# indicies into two lists. We essentially uses of the function strip()
# and split().
# The next step would be to obtain the unique names of the professors
# where we process the various formats of name that are given in the input
# file.

########################################################################

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
	prof_final = []
	for s in prof:
                if ',' in s:
                        ss=s.split(",")
                        prof_final.append(ss[0])
                elif '.' in s:
                        ss=s.split(".")
                        if ' ' in ss[-1]:
                                sss=ss[-1].split(" ")
                                prof_final.append(sss[-2])
                        else:
                                prof_final.append(ss[-1])
                else:
                        ss=s.split(" ")
                        prof_final.append(ss[-2])
	x=len(prof_final)
	for i in range(0,x):
                prof_final[i]=prof_final[i].title()
	prof_u=set(prof_final)
	prof_uni=list(prof_u)
	prof_uni.sort()
	pl2=len(prof_uni)

##########################################################################

# Now we merge the professors' courses under one professor index, so that
# there are no duplicate professor name and the corresponding courses are 
# also grouped into one index

##########################################################################

	count=0
	c_final = []
	for i in range(0,pl2):
		c_final.append([])
	for i in range(0,pl2):
		for j in range(0,x):
			if prof_final[j]==prof_uni[i]:
				c_ss=cours[j].split("|")
				xy=len(c_ss)
				for k in range(0,xy):
					c_final[i].append(c_ss[k].title())

##########################################################################

# Finally we call the function ench() which will do a spell check on all 
# the word that was input and it will correct the wrongly spelt words. The
# next the function that is called is jsend() is checks for course duplicates.
# Then we call pri() which essentially prints the output to a file named 
# cleaned.txt

##########################################################################

	c_f2=ench(c_final)
	c_f3=jsend(c_f2)
	pri(prof_uni,c_f3)

#########################################################################

# Prints the output to a file named cleaned.txt

#########################################################################

def pri(prof_uni,c_final):
	f = open('cleaned.txt', 'w')
	pl2=len(prof_uni)
	for i in range(0,pl2):
		c_final[i].sort()                       
	for i in range(0,pl2):
		f.write(prof_uni[i]+" - ")
		tr=len(c_final[i])
		for j in range(0,tr):
			if j==tr-1:
				f.write(c_final[i][j])
			else:
				f.write(c_final[i][j]+"|")
		f.write("\n")

##########################################################################

# Check the for spelling errors by using the dictionary library called as
# PyEnchant, the words are not just replaced like that, the edit distance
# is calculated between the original word and the suggested word, only if
# replacing the word the appropriate we do replace with the correct word.

##########################################################################

def ench(c_final):
	l=len(c_final)
	for i in range(0,l):
		l2=len(c_final[i])
		for j in range(0,l2):
			c_final[i][j]=stsplit(c_final[i][j])
	return c_final

##########################################################################

# The ench() function calls the stsplit() function to mainly do the integral
# processing of the data for spell check.

##########################################################################

def stsplit(st):
	d=enchant.Dict("en_US")
	sts=[word.strip(string.punctuation) for word in st.split(" ")]
	while '' in sts:
		sts.remove('')
	l=len(sts)
	for i in range(0,l):
		if (d.check(sts[i]))==False:
			sug=d.suggest(sts[i])
			flag=0
			if len(sts[i])==len(sug[2]) and flag==0:
				dist=edit(sts[i],sug[2])
				if dist<3 and (len(sts[i]))>3:
					st=st.replace(sts[i],sug[2])
				flag=1
			if len(sts[i])==len(sug[0]) and flag==0:
				dist=edit(sts[i],sug[0])
				if dist<3 and (len(sts[i]))>3:
					st=st.replace(sts[i],sug[0])
				flag=1
			if len(sts[i])==len(sug[1]) and flag==0:
				dist=edit(sts[i],sug[1])
				if dist<3 and (len(sts[i]))>3:
					st=st.replace(sts[i],sug[1])
				flag==1
			else:
				dist=edit(sts[i],sug[0])
				if dist<3 and (len(sts[i]))>3:
					st=st.replace(sts[i],sug[0])
		if 'z' in sts[i][-1]:
			s=sts[i].replace('z','s')
			st=st.replace(sts[i],s)
		if '.' in st:
			st=st.replace('.','')
		if '&' in st:
			st=st.replace('&','And')
		if sts[i]=='Intro':
			st=st.replace(sts[i],'Introduction')
	return st

##########################################################################

# This function is to mainly to check whether are duplicated course names.
# The course names are first passed to a function jacc() for further processing.

##########################################################################

def jsend(st):
	l=len(st)
	for i in range(0,l):
		l2=len(st[i])
		st[i]=jacc(st[i])
	return st

#########################################################################

# This function generally gets the name of the courses and checks whether
# there any duplicates using Jaccard Similarity/

#########################################################################

def jacc(st1):
	l=len(st1)
	if l==1:
		return st1
	for i in range(0,(len(st1)-1)):
		for j in range(i+1,len(st1)):
			dist=jcomp(st1[i],st1[j])
			if dist>0.7:
				st1.remove(st[j])
	return st1

########################################################################

# Calculates the Jaccard Similarity

########################################################################

def jcomp(s1,s2):
	s1s=[word.strip(string.punctuation) for word in s1.split(" ")]
	while '' in s1s:
		s1s.remove('')
	s2s=[word.strip(string.punctuation) for word in s2.split(" ")]
	while '' in s2s:
		s2s.remove('')
	nc1=set(s1s).intersection(s2s)
	nc2=list(nc1)
	nc=len(nc2)
	na=len(s1s)
	nb=len(s2s)
	t=nc/(na+nb-nc)
	return t
	
#######################################################################

# Calculates the Edit Distance

#######################################################################
def edit(s1, s2):
    m=len(s1)+1
    n=len(s2)+1

    tbl = {}
    for i in range(m): tbl[i,0]=i
    for j in range(n): tbl[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

    return tbl[i,j]

if __name__ == '__main__':
    run()
