A script based on the work guidelines of an upwork job posting:

"...create a script preferably in powershell but python can be ok as well.

1. the script should be able to get a list of TLD domain names from a CSV. (For example googledomce,msn.com,etc).
2. do a recusive DNS dig lookup of all the DNS records and export the A records and CNAME records for each TLDs to a CSV file.

"

The dnsdigscript.py is a proof of concept for this.

The script opens a specified file (sampleinput.csv) and reads each TLD that is represented as a string in the file. It then iterates
through a list of specified flags (record types) appropriate for the DIG command and returns the concise results for those records.
Each individual record is then added to a new csv output file (tlddigdata.csv).


Future work concepts:

Because it might be desirable to split the individual records by type (a/cname, etc) and the format
of rows may be inconsistent with csv formating as the returns of all records are not entirely consistent it would be
my recommendation to utilize a sqlite database to store these records, defining each record type as a table
and then defining the exact fields to be recorded creating a consistent data structure for all entries with a new row
for each record.
