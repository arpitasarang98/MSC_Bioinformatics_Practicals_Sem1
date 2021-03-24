Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\Iraje Software\Desktop\BioInformaticsPracs_Sem1\Prac2_GetValueOfSeq_36.py
Enter the first sequence::ACTG
Enter the second sequence::AGCT

Traceback (most recent call last):
  File "C:\Users\Iraje Software\Desktop\BioInformaticsPracs_Sem1\Prac2_GetValueOfSeq_36.py", line 29, in <module>
    find_identity(seq1,seq2)
  File "C:\Users\Iraje Software\Desktop\BioInformaticsPracs_Sem1\Prac2_GetValueOfSeq_36.py", line 6, in find_identity
    gap(a,b)
  File "C:\Users\Iraje Software\Desktop\BioInformaticsPracs_Sem1\Prac2_GetValueOfSeq_36.py", line 27, in gap
    b.insert(k,'-')
UnboundLocalError: local variable 'k' referenced before assignment
>>> 
= RESTART: C:\Users\Iraje Software\Desktop\BioInformaticsPracs_Sem1\Prac2_GetValueOfSeq_36.py
Enter the First sequence::ACTG
Enter the Second sequence::AGCT

['A', 'C', 'T', 'G']
['A', 'G', 'C', 'T']
Matching Score:: 4
Identity of the Sequences:: 25.0
>>> 