<?php
	session_start();
	$charName = $_SESSION['Cname'];
	$password = $_SESSION['Pword'];
	if (!isset($_SESSION['Cname']) && !isset($_SESSION['Pword'])) {
		session_destroy();
		header("Location: userDashboard.php");
	}
?>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" type="text/css" href="css/mainStyle.css" />
        <link rel="stylesheet" type="text/css" href="css/supportStyle.css" />
        <link rel="stylesheet" type="text/css" href="css/template.css" />
        <title>Beast Reality - FAQ</title>
        <!--
        	_author_ : kelvin
        -->
    </head>
    <body>
        <div class = "contentWrapper">

            <div class = "header">
                <div class = "menu">
                    <?php
                    include 'navigation.php';
                    ?>
                </div>

                <div class="content">
                    <!-- Content of left panel -->
                    <div class="contentLeft">
		    <div id="nSupport">
			    
			    <?php
				include 'supportLeftContent.php';
			    ?>
			    
                        </div>
		    </div>

                    <!-- ################################################################# -->
                    <!-- Content of right panel -->
                    <div class="contentRight">
                        <!-- TYPE YOUR CONTENT HERE -->
                        
                        <h2 style="color: #fff;">Your Existing World(s):</h2><br />
						<?php
							$con = mysql_connect("smurf.sfsu.edu","BeastReality","beastreality"); 
							if (!$con) {
								die('Could not connect: ' . mysql_error());
							}

							mysql_select_db("BeastRealityDB", $con) OR die('Wrong DB name!');
							
							$sql = "SELECT W.game_name, W.env_type, W.access_type, W.game_mode
        							FROM world AS W, player AS P
        							WHERE P.character_name = '$charName' AND P.player_id_pk = W.creator_playerID_fk";
									
							$queryInfo = mysql_query($sql);
																
							echo "<table border='1' style='border-color: #fff; color: #fff;'>";
							echo "<tr>";
							echo "<th>Game Name</th>";
							echo "<th>Environment</th>";
							echo "<th>World Type</th>";
							echo "<th>Game Mode</th>";
							echo "</tr>";
							
							while ($row = mysql_fetch_array($queryInfo)) {
								echo "<tr>";
								echo "<td>$row[0]</td>";
								echo "<td>$row[1]</td>";
								echo "<td>$row[2]</td>";
								echo "<td>$row[3]</td>";
							}
							
							mysql_close($con);
							session_destroy();
						?>
                    </div>
                </div>
                <?php
                    include 'footer.php';
                ?>
            </div>
        </div>
    </body>
</html>

