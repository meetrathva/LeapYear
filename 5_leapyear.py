year = int(input("Enter year: "))
fh = open("5_leapyear.txt","w")
fh.write(str(year))
if(year%4==0):
    fh.write("\nThe given year is leap year")
else:
    fh.write("\nThe given year is NOT leap year")
fh.close()