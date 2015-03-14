<?php

$userName = $_POST['Uname'];
$password = md5($_POST['Pword']);
$email    = $_POST['Email'];
$charName = $_POST['Cname'];

$con = mysql_connect("smurf.sfsu.edu","BeastReality","beastreality");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

mysql_select_db("BeastRealityDB", $con);

$sql = "INSERT INTO player(user_name, password, email_id, character_name) VALUES
        ($userName, $password, $email, $charName);";
        
if (mysql_query("SELECT COUNT(character_name) FROM player WHERE character_name = $charName;") > 0) {
    echo "<script type='text/javascript'>alert('Character name is not available');</script>";
} else {
    mysql_query(sql);
    header("Location: registerSuccess.php");
}

mysql_close($con);
?>