<!-- Filename	: guideLeftContent.php
     Description: This file manages the left vertical menu on 'GUIDE' section.
		  It uses php function to call the correct css classes in order
		  to create simple animation on the menu.
-->

<html>
<body>

<?php
    $filename_about = basename($_SERVER['SCRIPT_FILENAME']);
?>

    <ul>
        <li><a
            <?php
		#if the current file contains 'overview', then use 'overviewMenu_1' class.		
		if (strlen(stristr($filename_about, "overview")) > 0)  {
			echo "class='overviewMenu_1'"; 
                } else {
			echo "class='overviewMenu'";
                }
            ?>        
        href="overview.php" target="_self">Overview</a>
	</li>
			
        <li><a
            <?php
		if (strlen(stristr($filename_about, "gameFeatures")) > 0)  {
			echo "class='gameFeaturesMenu_1'";
                } else {
			echo "class='gameFeaturesMenu'";
                }
            ?>				
        href="gameFeatures.php" target="_self">Game Features</a>
	</li>
				
        <li><a
            <?php
		if (strlen(stristr($filename_about, "credits")) > 0)  {
			echo "class='creditsMenu_1'";
                } else {
			echo "class='creditsMenu'";
                }
            ?>        
        href="credits.php" target="_self">Credits</a>
	</li>
    </ul>

</body>
</html>