def sub_str(s):
    al="AEIOU"
    k_c=0
    s_c=0
    for i in range(len(s)):
        if s[i] in al:
            k_c+=len(s)-i
        else:
            s_c+=len(s)-i
    if k_c>s_c:
        print("Kevi",k_c)
    else:
        print("Surat",s_c)
s=input()
sub_str(s)

