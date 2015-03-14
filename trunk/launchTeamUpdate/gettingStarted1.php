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
		<!--                        
			<div id="navGuide">
			
                            <ul class="top-level">
                -->
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
                        <div class="textContent">
                            <p>When you enter Beast Reality you will have to do the following:</p>
                            <div class="subContent">
                                <p>You have to pick one of the two exciting modes of game play (PVP, PVE).</p>
                                <p>If chosen PVP, then you have to join a game.</p>
                                <p>If chosen PVE, then have to select a world to join.</p>
                                <p>Once you join your game gets started.</p>
                            </div>

                            <br />
                            <p>At the beginning of game every player has is the following to start with:</p>
                            <div class="subContent">
                                <p>An environment.</p>
                                <p>9 different zones within the environment.</p>
                                <p>A minimum of six water sources randomly placed in zones.</p>
                                <p>Random set of plants.</p>
                                <p>Fixed amount of currency.</p>
                            </div>
                        </div>
                    </div>
                </div>
                <?php
                    include 'footer.php';
                ?>
            </div>
        </div>

    </body>
</html>

