def longest_palindromic_substring(s):
    maks=''
    for i in range(len(s)):
        for j in range(i+2,len(s)+1):
            if s[i:j]==s[i:j][::-1] and len(s[i:j])>len(maks):
                maks=s[i:j]
    return maks
    """
    Given a string find the longest palindromic substring
    """