<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" type="text/css" href="css/mainStyle.css" />
        <link rel="stylesheet" type="text/css" href="css/guideStyle.css" />
        <link rel="stylesheet" type="text/css" href="css/template.css" />
        <title>Beast Reality - User Interface</title>
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
		    <div id="nGuide">
			    
			    <?php
				include 'guideLeftContent.php';
			    ?>
			    
                        </div>
		    </div>

                    <!-- ################################################################# -->
                    <!-- Content of right panel -->
                    <div class="contentRight" style="font-size: 13px;">
                        <!-- TYPE YOUR CONTENT HERE -->
                        
                        <img style="margin-top: 15px; margin-bottom: 15px;" src="images/screenshots/createWorld_6.png" alt="Create World screen" />
                        <p>When the player wants to create a new world then he should click on the create new world button, which leaves a popped
                            out screen as shown above and ask user to input world name, type of ecosystem they want to play in and they have an
                            option of making it a public or private world.</p>
                        <a href="ui_2.php" style="float: left; color: white; margin-top: 20px; font-size: 16px;">BACK ...</a>
                        <a href="ui_4.php" style="float: right; color: white; margin-top: 20px; font-size: 16px;">MORE ...</a>
                    </div>
                </div>
                <?php
                    include 'footer.php';
                ?>
            </div>
        </div>

    </body>
</html>

