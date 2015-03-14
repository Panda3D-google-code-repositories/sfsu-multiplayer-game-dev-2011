<?php
	session_start();
	$charName = $_SESSION['charName'];
	
	$newPassword = md5($_POST['newPname']);
	
	$con = mysql_connect("smurf.sfsu.edu", "BeastReality", "beastreality");
	
	mysql_select_db("BeastRealityDB", $con) OR die('Wrong DB name!');
	
	$sql = "UPDATE player SET password = '$newPassword' WHERE character_name = '$charName'";
	
	mysql_query($sql) OR die("Change password failed!");
	echo "<script type='text/javascript'>";
	echo "alert('Successfully change password!');";
	echo "window.location=\"userDashboard.php\";</script>";
	
	mysql_close($con);
	session_destroy(); 
?>