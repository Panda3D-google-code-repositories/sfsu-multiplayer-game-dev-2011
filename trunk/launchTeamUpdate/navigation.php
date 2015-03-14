<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" type="text/css" href="css/navGuide.css" />
        <link rel="stylesheet" type="text/css" href="css/navDownload.css" />
        <link rel="stylesheet" type="text/css" href="css/navAbout.css" />
        <link rel="stylesheet" type="text/css" href="css/navSupport.css" />
	<?php
	    $filename = basename($_SERVER['SCRIPT_FILENAME']);
	?>
        <title>Beast Reality</title>
    </head>
    <body>

	<div class="HomeMenu">
		<a href="index.php" target="_self"><img
		<?php
		    if ($filename == 'index.php') {
			echo "src='images/home_button2.gif'";
		    } else {
			echo "src='images/home_button.gif'";
		    }
		?>
		style="border: 0;" alt="home button" /></a>
	</div>

	<div class="GuideMenu">
	    <div class="guide">
		<img width="105" height="50" 
		<?php
		    if ((strlen(stristr($filename, "gettingStarted")) > 0) ||
			(strlen(stristr($filename, "ui")) > 0) ||
			(strlen(stristr($filename, "learnMore")) > 0) ||
			(strlen(stristr($filename, "controls")) > 0) ||
			(strlen(stristr($filename, "skills")) > 0)) {
			echo "src='images/guide_button2.gif'";
		    } else {
			echo "src='images/guide_button.gif'";
		    }
		?>
		/>
					
			<ul>
				<li><a href="gettingStarted.php">Getting Started</a></li>
				<li><a href="ui.php">User Interface</a></li>
				<li><a href="learnMore.php">Learn More</a></li>
				<li><a href="controls.php">Controls</a></li>
				<li><a href="skills.php">Skills</a></li>
			</ul>
		</div>
	</div>
	
	<div class="DownloadMenu">
		<div class="download">
		<img width="130" height="50" 
		<?php
		    if ((strlen(stristr($filename, "gameClient")) > 0) ||
			(strlen(stristr($filename, "screenShots")) > 0) ||
			(strlen(stristr($filename, "conceptArt")) > 0) ||
			(strlen(stristr($filename, "video")) > 0) ||
			(strlen(stristr($filename, "docs")) > 0) ||
			(strlen(stristr($filename, "reqs")) > 0)) {
			echo "src='images/download_button2.gif'";
		    } else {
			echo
			"src='images/download_button.gif'";
		    }
		?>
		/>
		<ul>
		    <li><a href="gameClient.php">Game Client</a></li>
		    <li><a href="screenShots.php">Screen Shots</a></li>
		    <li><a href="conceptArt.php">Concept Art</a></li>
		    <li><a href="video.php">Video</a></li>
		    <li><a href="docs.php">Documentation</a></li>
		    <li><a href="reqs.php">Requirements</a></li>
		</ul>
		</div>		
	
	</div>
		<div class="AboutMenu">
		<div class="about">
		    <img width="107" height="50" 
		    <?php
		        if ((strlen(stristr($filename, "overview")) > 0) ||
			    (strlen(stristr($filename, "gameFeatures")) > 0) ||
			    (strlen(stristr($filename, "credits")) > 0)) {
			    echo "src='images/about_us_button2.gif'";
			} else {
			    echo
			    "src='images/about_us_button.gif'";
			}
		    ?>
		    />
			<ul>
				<li><a href="overview.php">Overview</a></li>
				<li><a href="gameFeatures.php">Game Features</a></li>
				<li><a href="credits.php">Credits</a></li>
			</ul>
		</div>
	</div>
    </div>
	
		<div class="SupportMenu">
		<div class="support">
			<img width="105" height="50" 
			<?php
			    if ((strlen(stristr($filename, "userDashboard")) > 0) ||
				(strlen(stristr($filename, "register")) > 0) ||
				(strlen(stristr($filename, "contactUs")) > 0) ||
				(strlen(stristr($filename, "faq")) > 0)) {
				echo "src='images/support_button2.gif'";
			    } else {
			        echo
			        "src='images/support_button.gif'";
			    }
			?>
			/>
			<ul>
				<li><a href="userDashboard.php">User Dashboard</a></li>
				<li><a href="register.php">Register</a></li>
				<li><a href="contactUs.php">Contact Us</a></li>
				<li><a href="faq.php">FAQ</a></li>
			</ul>
		</div>
	</div>
    </body>
</html>

