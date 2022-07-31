
# Reg_Gen
Simple python script that generates a pre-defined range of random numbers.
The original objective is to populate Prolog KBs. <br>

## **Usage**

It works with 2 parameters:

**argv[1]** is the first atom's name of our predicate.
**argv[2]** is the maximum range of registers.

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
The following line shows exemplifies how to output the script to a text file using cli:

    PS>python script.py user 500 > file.txt
