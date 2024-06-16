#Task - Blind SQL injection: Find the version of the SQL database software being used.

#For this assignment, SQLmap is going to be used. SQLmap automates identification and exploitation of SQL injection
#vulnerabilities, ultimately gaining control over database servers.
#Version being used is 1.8.2
#For each security level, we use the same command: 
sqlmap -u "http://127.0.0.1/dvwa/vulnerabilities/sqli_blind/?id=2&Submit=Submit#" --cookie="security=<Security_level>;
PHPSESSID=<value>"
#The security level has to be filled accordingly and the cookie value can be obtained from the console using command:
alert(document.cookie)

#Low security level - Only the query needs to be escaped, no other security provision. This is automated by sqlmap.
sqlmap -u "http://127.0.0.1/dvwa/vulnerabilities/sqli_blind/?id=2&Submit=Submit#" --cookie="security=low; PHPSESSID=ps3mg7nr0f7hr7e4ba07fliv6n"
#After pressing enter, it will show a message saying that 'id' is susceptible to Boolean-based blind injection vulnerabilities.
#Boolean-based blind injection gives us true or false according to the paylaod delivered. This can be used to get information about the database
#Keep pressing enter to go with the default value to the questions being asked.
#When the execution gets completed, it can be seen that the SQL database software being used is MySQL version 5.0.12(MariaDB fork)
#It also gives us the payload which can be used for injection. The payloads contain time based blind SQLi using which it can be said
#whether the server is responding to the requests.

#Medium security level - Same procedure as for the above level except that security changes to medium and the cookie value needs to be changed.

#Hard security level - Same procedure as for the above level except that security changes to hard and the cookie value needs to be changed.

#Thus, the SQL database software being used is MySQL version 5.0.12(MariaDB fork)
