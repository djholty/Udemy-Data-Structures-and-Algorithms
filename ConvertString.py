# Problem: if S1 and S2 are strings, convert S2 to S1 using delete, insert  or replace operation
#find the minumum count of edit operations
#ex S1 = 'table' S2 = 'tgable' eg use delete operation
#ex S1 = table, s2 = tble eg use insert operation
#https://www.youtube.com/watch?v=MiqoA-yF-0M

def editDistance(str1, str2, m, n):
# If first string is empty, the only option is to
# insert all characters of second string into first
    if m == 0:
        return n
    # If second string is empty, the only option is to
    # remove all characters of first string
    if n == 0:
        return m
    # If last characters of two strings are same, nothing
    # much to do. Ignore last characters and get count for
    # remaining strings.

    if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1)
    # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.

    return 1 + min(editDistance(str1, str2, m, n-1),    # Insert
                    editDistance(str1, str2, m-1, n),    # Remove
                    editDistance(str1, str2, m-1, n-1)    # Replace
    )
    
    # Driver code
    str1 = "sunday"
    str2 = "saturday"
    print (editDistance(str1, str2, len(str1), len(str2)))