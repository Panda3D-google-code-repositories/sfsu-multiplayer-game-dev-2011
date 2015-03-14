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

$sql = "INSERT INTO player (user_name, password, email_id, character_name)
    VALUES ('$userName', '$password', '$email', '$charName')";

$checkCharName = mysql_query("SELECT COUNT(character_name) FROM player WHERE character_name = '$charName'");

$row = mysql_fetch_array($checkCharName);

if ($row[0] > 0) {
    header("Location: registerFail.php");
} elseif ($row[0] == 0) {
    mysql_query($sql) or die("Error in inserting new data");
    header("Location: registerSuccess.php"); 
}

mysql_close($con);
?>