
# Reg_Gen
Simple python script that generates a pre-defined range of phone numbers.
This script was originally made to populate Prolog KBs. <br>

## **Usage**

This script works with 2 parameters:

**argv[1]** is the first atom's name of our predicate.
**argv[2]** is the maximum range of our script.

(first atom will concatenate with the range, starting from 0)
## **Example**
The following command should print 5 items:

    PS>python script.py user 5

*output:*
   

     register('user0', '36930211').
     register('user1', '49457398').
     register('user2', '68248168').
     register('user3', '44565303').
     register('user4', '80362601').


## *Output*
The following code shows how to output the script to a text file using powershell:

`PS>python script.py user 500 > file.txt`
