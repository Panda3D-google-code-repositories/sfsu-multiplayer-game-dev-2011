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
                        
                        <img style="margin-top: 15px; margin-bottom: 15px;" src="images/screenshots/pveLobby_6.png" alt="PVE Lobby screen" />
                        <p>When a user chooses a World from the Main Lobby, they enter the chosen World's World Lobby.
                            In this lobby users can see the current on-line players and are able to communicate with them via Chat.
                            Moreover, a player can also see the list of available World, either 'Open World' or 'Closed World'.</p>
                        <a href="ui_1.php" style="float: left; color: white; margin-top: 20px; font-size: 16px;">BACK ...</a>
                        <a href="ui_3.php" style="float: right; color: white; margin-top: 20px; font-size: 16px;">MORE ...</a>
                    </div>
                </div>
                <?php
                    include 'footer.php';
                ?>
            </div>
        </div>

    </body>
</html>

