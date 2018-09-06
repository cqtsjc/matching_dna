# matching_dna
Code that matches dna sequences in a file [Python]

Problem statement:
Matching DNA Sequences in an input File :

--------------------------------------------------------

 

Assume in biology a certain genome sequencing task looks at strings of nucleobases: A(denine),C(ytosine),T(hymine),G(uanine). 

Recall that A matches with T and C matches with G. Match is case insensitive. So (AT,CG) is an example match. So, are (aT, Cg)

Assume a biologist has a database of an even number of nucleobase strings and wants to check whether each one has a match in the database. 

 

So for example if the input file has:

 

ACGTA

CTG

TGCAT

CA

GAC

GT

 

then we would output True 

 

since:

ACGTA matches with TGCAT

CTG matches with GAC

CA matches with GT

 

Assignment is to Write a program that will output 

1. True or False to the screen based on the contents of the input file. 

2. With each sequence its matched sequence. 

 

Your program should check whether each sequence has a matching sequence somewhere else in the file. 

Output True only if all sequences have a match.

 

1. Preferably, your solution must run in time O(n). That is,  you will read the entire file only one.

2. You are not allowed to use external libraries. Use only file operations and dictionaries/hashmaps/sets/java collection classes

 

Your program should get one parameter, the name of the input file.

 

./dna_check input.txt

 

The input file format will resemble the sample text file shown above and will not have any format errors.

1. Each input line (terminated by "\n") is a DNA sequence

2. Line may have spaces bewtween letters A, T, C and G. These to be omitted. 

3. Space before and after the sequence to be trimmed 

4. Empty lines to be ignored.

 

Other than possibley having blank lines mixed throughout the file. 

But we guarantee that there won't be spaces between letters on a line and that the line 

will contain all UPPER-CASE letters from the set {A,C,T,G}.
