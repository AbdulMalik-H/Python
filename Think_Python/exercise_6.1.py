def arc(m,n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return arc(m-1,1)
    elif m > 0 and n > 0:
        return arc(m-1, arc(m,n-1))

print(arc(3,4)) # This arguments will work fine

print(arc(1579320,569328)) # This arguments will cuase an error 