


try:
    a=18
    b=8
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print("Exception occured = > "+str(e))

except:
    print("Exception occured")