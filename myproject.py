Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> lowest=int(input("Enter the lowest number of the range:"))
Enter the lowest number of the range:1
>>> highest=int(input("Enter the highest number of the range:"))
Enter the highest number of the range:20
>>> for x in range(lowest,highest+1):
	if(x%2!=0):
		print(x)

		
1
3
5
7
9
11
13
15
17
19
>>> 
