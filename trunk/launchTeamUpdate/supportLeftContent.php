<!-- Filename	: supportLeftContent.php
     Description: This file manages the left vertical menu on 'GUIDE' section.
		  It uses php function to call the correct css classes in order
		  to create simple animation on the menu.
-->

<html>
<body>

<?php
    $filename_support = basename($_SERVER['SCRIPT_FILENAME']);
?>

    <ul>
        <li><a
            <?php
		#if the current file contains 'userDashboard', then use 'userDashboardMenu_1' class.		
		if (strlen(stristr($filename_support, "userDashboard")) > 0 ||
		    strlen(stristr($filename_support, "forgot")) > 0) {
			echo "class='userDashboardMenu_1'"; 
                } else {
			echo "class='userDashboardMenu'";
                }
            ?>        
        href="userDashboard.php" target="_self">User Dashboard</a>
	</li>
			
        <li><a
            <?php
		if (strlen(stristr($filename_support, "register")) > 0) {
			echo "class='registerMenu_1'";
                } else {
			echo "class='registerMenu'";
                }
            ?>				
        href="register.php" target="_self">register</a>
	</li>
				
        <li><a
            <?php
		if (strlen(stristr($filename_support, "contactUs")) > 0) {
			echo "class='contactUsMenu_1'";
                } else {
			echo "class='contactUsMenu'";
                }
            ?>        
        href="contactUs.php" target="_self">Contact Us</a>
	</li>
				
        <li><a
            <?php
		if (strlen(stristr($filename_support, "faq")) > 0) {
			echo "class='faqMenu_1'";
                } else {
			echo "class='faqMenu'";
                }
            ?>        
        href="faq.php" target="_self">faq</a>
	</li>
    </ul>

</body>
</html>