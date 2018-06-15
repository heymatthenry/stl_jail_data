import os,glob
from subprocess import call

os.chdir("data")
files = [f for f in glob.glob("*.csv") if "booking" in f or "Booking" in f]

columns = "IMN,SEX,RACE,BOOKING_DATE_TIME,DAYS_CONFINED,OFFENSE_TYPE,ARREST_AGENCY,BOND_CODE,BOND_AMOUNT,CHARGE_DESCRIPTION,COURT_NAME,DISPOSITION"

for f in files:
    output = f"clean/{f}"
    with open(output, "w") as outfile:
        call(["csvcut", "-c", columns, f], stdout = outfile)
