<!-- Filename	: guideLeftContent.php
     Description: This file controls the left vertical menu on 'GUIDE' section.
		  It uses php function to call the correct css classes in order
		  to create simple animation on the menu.
-->

<html>
<body>

<?php
    $filename_guide = basename($_SERVER['SCRIPT_FILENAME']);
?>

    <ul>
        <li><a
            <?php
		if (strlen(stristr($filename_guide, "gettingStarted")) > 0) {
			echo "class='gettingMenu_1'"; 
                } else {
			echo "class='gettingMenu'";
                }
            ?>        
        href="gettingStarted.php" target="_self">Getting Started</a>
	</li>
			
        <li><a
            <?php
		if (strlen(stristr($filename_guide, "ui")) > 0) {
			echo "class='uiMenu_1'";
                } else {
			echo "class='uiMenu'";
                }
            ?>				
        href="ui.php" target="_self">User Interface</a>
	</li>
				
        <li><a
            <?php
		if (strlen(stristr($filename_guide, "learnMore")) > 0) {
			echo "class='learnMoreMenu_1'";
                } else {
			echo "class='learnMoreMenu'";
                }
            ?>        
        href="learnMore.php" target="_self">Learn More</a>
	</li>
				
        <li><a
            <?php
		if (strlen(stristr($filename_guide, "controls")) > 0) {
			echo "class='controlsMenu_1'";
                } else {
			echo "class='controlsMenu'";
                }
            ?>        
        href="controls.php" target="_self">Controls</a>
	</li>
				
        <li><a
            <?php
                if (strlen(stristr($filename_guide, "skills")) > 0) {
			echo "class='skillsMenu_1'";
                } else {
			echo "class='skillsMenu'";
                }
            ?>        
        href="skills.php" target="_self">Skills</a>
	</li>
    </ul>

</body>
</html>