<!DOCTYPE html>
<html>
<head>
   <title>XSS 1</title>
<link rel="shortcut icon" href="../Resources/hmbct.png" />
</head>
<body>

<div align="center">
   <form method="GET" action="" name="form">
   <p>Your Text:<input type="text" name="username"></p>
   <input type="submit" name="submit" value="Submit">
</form>
	</div>
<?php
if(isset($_GET["username"]))

	echo("Your text is ".$_GET["username"])?>
</body>
</html>
