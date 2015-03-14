<?php
	session_start();
	$charName = $_SESSION['charName'];
?>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" type="text/css" href="css/mainStyle.css" />
        <link rel="stylesheet" type="text/css" href="css/supportStyle.css" />
        <link rel="stylesheet" type="text/css" href="css/template.css" />
        <link rel="stylesheet" type="text/css" href="css/userDashboard.css" />
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
                    <div class="contentRight"  style="color: #fff;">
                        <!-- TYPE YOUR CONTENT HERE -->
                        <h2 style="margin-left: 210px; margin-bottom: 20px;">Change Password</h2>

                        <form action="userDashboardChangePassword.php" method="post" >
                            <fieldset>
                                <legend>Change Password Form</legend>
                                <p><label for="Cname">Character Name :</label><?php echo $charName ?></p><br />
                                <p><label for="newPname">Password</label> <input type="text" size="14" maxlength="100" name="newPname" id="newPname" /></p><br />
                                	 
                                <label>&nbsp; </label><input type="submit" value="Sent" class="submit" /><br />
                            

                                
                            </fieldset>
                        </form>
                    </div>
                </div>
                
                <?php
                    include 'footer.php';
                ?>
            </div>
        </div>
    </body>
</html>

