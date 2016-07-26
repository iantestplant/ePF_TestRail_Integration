from testrail import APIClient
import sys

#connection information
client = APIClient('https://testplant.testrail.net/')
client.user = 'ian.parker@testplant.com'
client.password = 'T3stPl4nt'

#open the RunHistory.csv file, then check if the last line includes the word "Success"
#(The latest result is in the last line)
#f = open('C:/Workspaces/ePF/TestRailSample/TestRail_sample.suite/Results/main/RunHistory.csv')
resultFolder = sys.argv[1]
print resultFolder
sys.exit()

lastLine = f.readlines()[-1] # Read the last line of the results file
f.close()
fields = lastLine.split(',') # Split the line into comma separated fields

if len(fields) != 10:
	print("Error: Last line of RunHistory has fewer than 10 fields")
	sys.exit()

if fields[1].find('Success') >= 0:
    print ('Last Run: Success')

    result = client.send_post(
        'add_result_for_case/1/1',
        {'status_id': 1, 'comment': fields[8]}
    )
elif fields[1].find ('Failure') > 0:
	print ('Last Run: Failure')
	result = client.send_post(
		'add_result_for_case/1/1',
		{'status_id': 5, 'comment': fields[8], 'defects':fields[3]}
	)
	print(result)  # this prints the result of the TestRail Post. On success it lists the TestRail

