<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" type="text/css" href="css/mainStyle.css" />
        <link rel="stylesheet" type="text/css" href="css/guideStyle.css" />
        <link rel="stylesheet" type="text/css" href="css/template.css" />
        <title>Beast Reality - Getting Started</title>
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
                    <div class="contentRight">
                        <!-- TYPE YOUR CONTENT HERE -->
		
                        <p>Welcome Players, here is what every player has to know a little about Beast Reality.
					   This Game has been developed to make you have fun and at the same time educational. 
					   All you have to know is how to take good care of your environment and balance it.</p>
                        <br />
                        <p>Beast Reality provides you with two modes of Game play:</p>
                        <p>1. PVP:</p>
                        <div class="subContent">
                            <p>“Player versus Player”, where in player makes a team of even number and play against
						same number of players. Here it’s all about destroying the opponent’s environment 
						and trying to balance yours.</p>
                        </div>
                        <p>2. PVE:</p>
                        <div class="subContent">
                            <p>“Player versus Environment”, this is more kind of nurturing game where
						you should start building the environment and balance it. Once you get 
						hold of it, you will work together with your neighbor. The player who 
						creates the world can decide on number of environments that are going to exist.</p> 
                            <br />
                            <a href="gettingStarted1.php" style="float: right; color: white;">CONTINUE ...</a>
                        </div>

                    </div>
                </div>
                <?php
                    include 'footer.php';
                ?>
            </div>
    </body>
</html>

