"""
operators (none of theses change the original list )
<seq> + <seq>              - concatenation
<seq> * <int- expression>  - repetition
<seq>[]                    - indexing
<seq>[:]                   - slicing (always returns a list)
len<seq>                   - length
for <var> in <seq>:        - iteration
<expr> in <seq>            - Membership check
                                - checkis if a value is in the list
                                - returns a boolean

my_list = [3,4,5]
for i in my_list
    print(i)
    >>>3,4,5
for i in range(len(my_list))
    print(i)
    >>>0,1,2

if you watn to add lsitst to gether you have to use conatentations
appendign to a list with multiple thigns will treat it as a new list and a dd a new list within gth list
"""