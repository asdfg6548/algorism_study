import datetime as dt

x=dt.datetime.now()

print(f"{x.year}-{str(x.month).zfill(2)}-{str(x.day).zfill(2)}")
