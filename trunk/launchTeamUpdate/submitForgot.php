<?php
	$charName = $_POST['Cname'];
	
	$con = mysql_connect("smurf.sfsu.edu", "BeastReality", "beastreality");
	
	mysql_select_db("BeastRealityDB", $con) OR die('Wrong DB name!');
	
	$sql = "SELECT * FROM player WHERE character_name = '$charName'";
	
	$result = mysql_query($sql);
	
	$numberOfRow = mysql_num_rows($result);
	
	if ($numberOfRow == 0) {
		echo "<script type='text/javascript'>";
		echo "alert('Character name does not exist!');";
		echo "window.location=\"forgot.php\";</script>"; 
	} else {
		
		session_start();
		$_SESSION['charName'] = $charName;
		
		header("Location: userDashboardRetrievePassword.php");
	}
	
	mysql_close($con);
?>
