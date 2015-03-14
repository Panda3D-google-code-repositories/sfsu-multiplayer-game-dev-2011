<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:fb="https://www.facebook.com/2008/fbml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" type="text/css" href="css/mainStyle.css" />
        <title>Beast Reality - Main Page</title>
        <script src='http://connect.facebook.net/en_US/all.js'></script>
        <script>
            FB.init({appId: '274607232578400', status: true, cookie: true, xfbml: true, oauth: true});
        </script>

    </head>
    <body>
    	<?php 
    		include 'template.php';
		?>
		
        <div class="content">
        	        	
        	<!-- Content of left panel -->
        	<div class="contentLeft">
        		<p>Like us!</p>
        		<div class="fb-like" data-href="https://thecity.sfsu.edu/~kvk118/BR/index.php" data-send="true" data-width="400" data-show-faces="true"></div>
        		<div class="fb-activity" data-site="https://thecity.sfsu.edu/~kvk118/BR/index.php" data-width="230" data-height="280" data-header="false" data-recommendations="false"></div>
        	</div>
        	
        	<!-- Content of right panel -->
        	<div class="contentRight">
        		<div class="released">
        			<h3>Beast Reality ver. 1.0.0 will be released soon ...</h3>
        		</div>
        	</div>
        </div>
        <div id='fb-root'></div>
        <p><a href="#" id="postToFeed" onclick='publishToFacebook(); return false;'></a></p>
        <div id="successMsg"></div>
        <script>
            var name = "";
            var body = "<?php echo htmlspecialchars($_GET["msg"]); ?>";

            function publishToFacebook()
            {
                FB.login(function(response) {
                    if (response.authResponse) {
                        FB.api('/me', function(response) {
                            name = response.name;
                            FB.api('/me/feed', 'post',
                            {
                                message: body,
                                link: "http://smurf.sfsu.edu/~BeastReality/",
                                picture: "http://smurf.sfsu.edu/~BeastReality/images/beastReality1.png",
                                name: "Beast Reality",
                                description: "Multiplayer Online Gamification for Ecosystem Nurturing against Species Invasions Research"
                            },
                            function(response) {
                                if (response && !response.error) {
                                    alert("Hi "+name+", status posted on your wall");
                                    document.location.href = "http://www.facebook.com";
                                }
                            });
                        });
                    }
                }, {scope: 'publish_stream'});
            }
            <?php
                if(!empty($_GET["msg"]))
                {
            ?>
            document.getElementById("postToFeed").click();
            <?php
                }
            ?>
        </script>
        <script>(function(d, s, id) {
		  var js, fjs = d.getElementsByTagName(s)[0];
		  if (d.getElementById(id)) return;
		  js = d.createElement(s); js.id = id;
		  js.src = "//connect.facebook.net/en_US/all.js#xfbml=1";
		  fjs.parentNode.insertBefore(js, fjs);
		}(document, 'script', 'facebook-jssdk'));</script>
    </body>
</html>

