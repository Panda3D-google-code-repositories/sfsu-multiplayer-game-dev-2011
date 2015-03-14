<?php
$charName = $_POST['Cname'];
$password = md5($_POST['Pword']);

$con = mysql_connect("smurf.sfsu.edu","BeastReality","beastreality"); 
if (!$con) {
	die('Could not connect: ' . mysql_error());
}

mysql_select_db("BeastRealityDB", $con) OR die('Wrong DB name!');

$checkUser = mysql_query("SELECT COUNT(character_name) FROM player WHERE character_name = '$charName' AND password = '$password'");

$row = mysql_fetch_array($checkUser);

if ($row[0] == 1) {     //Existing user
	$sql = "SELECT *
        	FROM world AS W, player AS P
        	WHERE P.character_name = '$charName' AND P.player_id_pk = W.creator_playerID_fk";
    $getInfo = mysql_query($sql);
	$numberOfRow = mysql_num_rows($getInfo);
	
    if($numberOfRow == 0) {
        header("Location: userDashboardEmpty.php");
    } else {
    	session_start();
		$_SESSION['sessionid'] = session_id();
		$_SESSION['Cname'] = $charName;
		$_SESSION['Pword'] = $password;
		$_SESSION['query'] = $getInfo;
        header("Location: userDashboardNotEmpty.php");
    }
} elseif ($row[0] == 0) {
	echo "<script type='text/javascript'>";
	echo "alert('You are not registered! Please register first!');";
	echo "window.location=\"register.php\";</script>"; 
}

mysql_close($con);
?>