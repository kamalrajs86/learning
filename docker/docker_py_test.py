import os
import sys
import snowflake.connector

n = 5
k = n + n
print(k)

yr = open("/dockercon/input.dat","r")
print(yr.read())
yr.close()

con = snowflake.connector.connect(
                user="KAMALRAJS",
                password="",
                account="sla35871.us-east-1",
                warehouse="COMPUTE_WH",
                database="SFPRO",
                schema="WIP_SCH",
                role="SF_PRO_ROLE"
)

cur = con.cursor()
cur.execute("select * from SFPRO.WIP_SCH.EMPDETAILS1;")
rows = cur.fetchall()
print(rows)
