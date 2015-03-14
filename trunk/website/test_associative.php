<?php
$salaries = array();

array_push($salaries, array("mohammad" => 2000, "X"=>10000));
array_push($salaries, array("qadir" => 1000, "Y"=>20000));
array_push($salaries, array("zara" => 500, "Z"=>30000));

echo "Salary of mohammad is ". $salaries[0]['mohammad'] ." " . $salaries[0]['X']."<br />";
echo "Salary of qadir is ".  $salaries[1]['qadir']. " ". $salaries[1]['Y']."<br />";
echo "Salary of zara is ".  $salaries[2]['zara']. " ". $salaries[2]['Z']. "<br />";

/* Second method to create array. */
$salaries['mohammad'] = "high";
$salaries['qadir'] = "medium";
$salaries['zara'] = "low";

echo "Salary of mohammad is ". $salaries['mohammad'] . "<br />";
echo "Salary of qadir is ".  $salaries['qadir']. "<br />";
echo "Salary of zara is ".  $salaries['zara']. "<br />";
?>