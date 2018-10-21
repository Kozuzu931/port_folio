def vorting_right(old,year):
    if year<=2015 and old>=20:
        right=True
    elif year>=2016 and old>=18:
        right=True
    else:
        right=False
        
    return right
