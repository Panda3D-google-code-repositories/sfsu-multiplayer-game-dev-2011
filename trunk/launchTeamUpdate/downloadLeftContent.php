<!-- Filename	: guideLeftContent.php
     Description: This file video the left vertical menu on 'GUIDE' section.
		  It uses php function to call the correct css classes in order
		  to create simple animation on the menu.
-->

<html>
<body>

<?php
    $filename_download = basename($_SERVER['SCRIPT_FILENAME']);
?>

    <ul>
        <li><a
            <?php
		#if the current file contains 'gameClient', then use 'gameClientMenu_1' class.		
		if (strlen(stristr($filename_download, "gameClient")) > 0) {
			echo "class='gameClientMenu_1'"; 
                } else {
			echo "class='gameClientMenu'";
                }
            ?>        
        href="gameClient.php" target="_self">Game Client</a>
	</li>
			
        <li><a
            <?php
		if (strlen(stristr($filename_download, "screenShots")) > 0) {
			echo "class='screenshotsMenu_1'";
                } else {
			echo "class='screenshotsMenu'";
                }
            ?>				
        href="screenShots.php" target="_self">Screen Shots</a>
	</li>
				
        <li><a
            <?php
		if (strlen(stristr($filename_download, "conceptArt")) > 0) {
			echo "class='conceptArtMenu_1'";
                } else {
			echo "class='conceptArtMenu'";
                }
            ?>        
        href="conceptArt.php" target="_self">Learn More</a>
	</li>
				
        <li><a
            <?php
		if (strlen(stristr($filename_download, "video")) > 0) {
			echo "class='videoMenu_1'";
                } else {
			echo "class='videoMenu'";
                }
            ?>        
        href="video.php" target="_self">video</a>
	</li>
				
        <li><a
            <?php
                if (strlen(stristr($filename_download, "docs")) > 0) {
			echo "class='docMenu_1'";
                } else {
			echo "class='docMenu'";
                }
            ?>        
        href="docs.php" target="_self">Documentation</a>
	</li>
	
	<li><a
            <?php
                if (strlen(stristr($filename_download, "reqs")) > 0) {
			echo "class='reqsMenu_1'";
                } else {
			echo "class='reqsMenu'";
                }
            ?>        
        href="reqs.php" target="_self">Requirement</a>
	</li>
    </ul>

</body>
</html>