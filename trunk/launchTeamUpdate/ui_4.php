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
                        
                        <img style="margin-top: 15px; margin-bottom: 15px;" src="images/screenshots/animal_6.png" alt="In-World screen" />
                        <p>Finally, we made it to our destination and its time that we make it more diverse and balanced.</p>
                        <a href="ui_3.php" style="float: left; color: white; margin-top: 20px; font-size: 16px;">BACK ...</a>
                        
                    </div>
                </div>
                <?php
                    include 'footer.php';
                ?>
            </div>
        </div>

    </body>
</html>

