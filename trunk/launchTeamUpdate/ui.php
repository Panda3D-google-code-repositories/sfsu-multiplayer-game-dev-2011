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
                        <p>The 2D interfaces in the game are designed in a very user friendly manner.
                            Just to make everyone familiar about what they are going to view like,
                            here are some of the screens and their related details.</p>
                        
                        <img style="margin-top: 15px; margin-bottom: 15px;" src="images/screenshots/login_6.png" alt="login screen" />
                        <p>The above screen is not much different from the regular login screens. If you are a new user click register
                            and then use that username and password and login into Beast Reality.</p>
                        <a href="ui_1.php" style="float: right; color: white; margin-top: 20px; font-size: 16px;">MORE ...</a>
                    </div>
                </div>
                <?php
                    include 'footer.php';
                ?>
            </div>
        </div>

    </body>
</html>

