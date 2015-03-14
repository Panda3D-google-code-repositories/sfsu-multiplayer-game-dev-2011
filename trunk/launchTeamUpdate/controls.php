<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" type="text/css" href="css/mainStyle.css" />
        <link rel="stylesheet" type="text/css" href="css/guideStyle.css" />
        <link rel="stylesheet" type="text/css" href="css/template.css" />
        <title>Beast Reality - Controls</title>
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
                    <div class="contentRight" style="color: white;">
                        <!-- TYPE YOUR CONTENT HERE -->
                        <table border="1" style="border-color: #fff;">
                                <tr>
                                        <th>Hotkey</th>
                                        <th>Function</th>
                                </tr>
                                <tr>
                                        <td>Esc</td>
                                        <td>Exit full screen mode</td>
                                </tr>
                                <tr>
                                        <td>CTR-f</td>
                                        <td>Switch to full screen mode</td>
                                </tr>
                                <tr>
                                        <td>Enter</td>
                                        <td>Send chat message</td>
                                </tr>
                                <tr>
                                        <td>p</td>
                                        <td>Display/hide online players</td>
                                </tr>
                                <tr>
                                        <td>n</td>
                                        <td>Display create new game pane</td>
                                </tr>
                                <tr>
                                        <td>Tap</td>
                                        <td>Toggle through entry fields</td>
                                </tr>
                                <tr>
                                        <td>a</td>
                                        <td>Display/hide list of other avatars</td>
                                </tr>
                                <tr>
                                        <td>s</td>
                                        <td>Display/hide Stats frame</td>
                                </tr>
                                <tr>
                                        <td>e</td>
                                        <td>Apply avatar effects</td>
                                </tr>
                                <tr>
                                        <td>w</td>
                                        <td>Display/hide weather frame</td>
                                </tr>
                                <tr>
                                        <td>q</td>
                                        <td>Display/hide Menu frame</td>
                                </tr>
                                <tr>
                                        <td>arrow_up/down/left/right</td>
                                        <td>Camera Control</td>
                                </tr>
                        </table>

                    </div>
                </div>
                <?php
                    include 'footer.php';
                ?>
            </div>
        </div>
    </body>
</html>

