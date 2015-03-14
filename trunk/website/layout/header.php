<?php
// php login sessions, cookies, etc should be declared here so once a user entered in their info in the login area. they won't have to re-enter their info and
// the website will keep track of what they may do on the website.
$siteroot="/~debugger/wb/";
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
    <head>
        <title>World of Balance</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta http-equiv="Content-Language" content="en-US" />
        <meta name="author" content="Gary Ng,Ryan Tam,Qianjun Yang,Jun Wang,Oren Antebi" />
        <meta name="copyright" content="&copy; 2012 SFSU" />
        <meta name="keywords" content="SFSU,World of Balance" />
        <meta name="rating" content="general" />
        <meta name="revisit-after" content="7 days" />
        <link rel="stylesheet" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.22/themes/base/jquery-ui.css" type="text/css" />

        <link rel="stylesheet" href="css/style.css" type="text/css" />

        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.min.js"></script>
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.22/jquery-ui.min.js"></script>

        <script type="text/javascript" src="js/lib/modal.popup.js"></script>
        <script type="text/javascript" src="js/lib/popup_species.js"></script>

        <script type="text/javascript" src="js/script.js"></script>
        <script type="text/javascript" src="js/navigationbar.js"></script>
    </head>

    <body id="top">
	<div id="layout">
            <div id="header">
		<div id="navbar">
                    <?php
                    // include the navigation bar html here. we could put the javascript code in a .js file in the js folder.
                    ?>

                    <ul id="navdropdown">
                    <li><a href="index.php" onmouseover="mopen('m1')" onmouseout="mclosetime()">Home</a>
                    </li>
                    <li><a href="javascript:void(0);" onclick="mtoggle('m2')" onmouseover="mopen('m2')" onmouseout="mclosetime()">About</a>
                        <div id="m2" onmouseover="mcancelclosetime()" onmouseout="mclosetime()">
                            <a href="about_game_features.php">Game Features</a>
                            <a href="about_credits.php">Credits</a>
                        </div>
                    </li>
                    <li><a href="javascript:void(0);" onclick="mtoggle('m3')" onmouseover="mopen('m3')" onmouseout="mclosetime()">Guide</a>
                        <div id="m3" onmouseover="mcancelclosetime()" onmouseout="mclosetime()">
                            <a href="guide_getting_started.php">Getting Started</a>
                            <a href="guide_user_interface.php">User Interface</a>
                            <a href="guide_controls.php">Controls</a>
                            <a href="guide_game_tips.php">Game Tips</a>
                            <a href="guide_species.php">Species</a>
                        </div>
                    </li>
                    <li><a href="javascript:void(0);" onclick="mtoggle('m6')" onmouseover="mopen('m6')" onmouseout="mclosetime()">Downloads</a>
                        <div id="m6" onmouseover="mcancelclosetime()" onmouseout="mclosetime()">
                            <a href="download_game_client.php">Game Client</a>
                            <a href="download_screen_shots.php">Images</a>
                            <a href="download_videos.php">Videos</a>
                        </div>
                    </li>
                    <li><a href="javascript:void(0);" onclick="mtoggle('m7')" onmouseover="mopen('m7')" onmouseout="mclosetime()">Support</a>
                        <div id="m7" onmouseover="mcancelclosetime()" onmouseout="mclosetime()">
                        <a href="support_contact.php">Contact Us</a>
                        <a href="support_faq.php">FAQ</a>
                        </div>
                    </li>
                    <a href="#"></a>
                    </ul>
                    <div style="clear:both"></div>
                </div>
            </div>
            <div id="wrapper">
                
