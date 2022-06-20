from datetime import date
from datetime import timedelta

def dayCalc( day ):
    if day == 0:
        return date.today() - timedelta( days = 2 )
    elif day == 6:
        return date.today() - timedelta( days = 1 )
    else:
        return date.today()
