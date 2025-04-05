import subprocess
import re

# A list of the flags we'll call for this script. We can add other dig options like mx or txt to increase calls and data. Defaults according to specification are 'A' and 'CNAME'.
digflags = ['a','cname']

# Our example file is a simple csv file with a domain seperated by comma on a single line.
tldlist = open('sampleinput.csv','r')
outputfile = open('tlddigdata.csv','w')

def digcall(domain):
	try:
		# The DIG command uses our FLAG (a,cname by default), and the TLD specified. In order to get clean, concise results from the dig stdout, we specify additional flags: answer and authority, respectively for A and CNAME records. The script was also tested adding MX records to the digflags library and utilizing the +short dig flag to return those results as well, allowing for additional functionality should the user wish.
		if flag == 'a':
			result = subprocess.run(['dig', flag, domain, '+noall', '+answer'], capture_output=True, text=True) 
		elif flag == 'cname':
			result = subprocess.run(['dig', flag, domain, '+noall', '+authority'], capture_output=True, text=True)
		else:
			result = subprocess.run(['dig', flag, domain, '+short'], capture_output=True, text=True)
		return result.stdout
	except Exception as e:
		print (e)
		return (e)



if __name__ == "__main__":
	print ("..Start..")
#Assuming the document may seperate domains by a combination of new lines and commas, we loop both lines and split the list by commas so that we can iterate through each domain
	for line in tldlist:
#		print (line)
		domainslist= line.split(',')
		#iterate through the domains in the domain list per line
		for tld in domainslist:
			tld= tld.replace('\n','')
			print ("[>] TLD: "+tld)
			# iterate through dig flags specified
			for flag in digflags:
			#	print ("	[-] Record Type: "+flag)
				output = (digcall(tld))
			#	print (output)
				recordslist = output.split('\n')
			#	print (recordslist)
				for record in recordslist:
					if record != '':
#						finalline = ''
						finalline = (''+tld+','+flag+','+record+'\n')
				#		recordline=''
				#		recordline += writeline+record
						print ("[....]LINE TO WRITE to csv output:")
						print (finalline)
#						outputfile.write(finalline)
						print ("[!] Written.")
print ("[!!!] End of Process")
