<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" type="text/css" href="css/mainStyle.css" />
        <link rel="stylesheet" type="text/css" href="css/guideStyle.css" />
        <link rel="stylesheet" type="text/css" href="css/template.css" />
        <title>Beast Reality - Game Tips</title>
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
                        <p>The following are some papers which were provided by our professor,
                            if anyone interested are welcome to go through them.</p>

                        <ul style="color: white; margin-left: 40px; margin-top: 20px; font-family: 'Comic Sans MS'">
                            <li>Food Web Structure and Ecosystem Services: Insights from The Serengeti: <a href="documents/Dobson_2009_Phil_Trans_B_Food-web_structure_and_ecosystem_services-_insights_from_the_serengeti.pdf" target="_blank">
                                    click here</a></li>
                            <li>Food Webs: <a href="http://foodwebs.org/" target="_blank">click here</a></li>
                            <li>Food Webs - Jennifer A.Dunne: <a href="documents/Dunne2009Chapter_2_.pdf" target="_blank">click here</a></li>
                            <li>Scaling Up Feeding-Based Population Dynamics To Complex Ecological Networks: <a href="documents/Williams2007Chapter_1_.pdf" target="_blank">click here</a></li>
                            <li>Population Dynamics And Food Web Structure-Predicting
                                Measurable Food Web Properties With Minimal Detail And Resolution: <a href="documents/Sabo2005Chapter.pdf">click here</a></li>

                        </ul>
			<p><a href="learnMore.php" style="float: left; color: white; margin-top: 20px; font-size: 16px;">BACK ...</a></p>
                    </div>
                </div>
                <?php
                    include 'footer.php';
                ?>
            </div>
        </div>
    </body>
</html>

