<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" type="text/css" href="css/mainStyle.css" />
        <link rel="stylesheet" type="text/css" href="css/template.css" />
        <title>Beast Reality - Main Page</title>
        <script src='http://connect.facebook.net/en_US/all.js'></script>
        <script>
            FB.init({appId: '274607232578400', status: true, cookie: true, xfbml: true, oauth: true});
        </script>
    </head>
    <body>
        <div class = "contentWrapper">

            <div class = "header">
                
                    <?php
                    include 'navigation.php';
                    ?>
                
                <div class="content">
                    <div class="contentLeft">
                        <p>Like us!</p>
                        <div class="fb-like" data-href="http://smurf.sfsu.edu/~BeastReality/index.php" data-send="true" data-width="200" data-show-faces="true"></div>
                        <div class="fb-activity" data-site="http://smurf.sfsu.edu/~BeastReality/index.php" style="background:#CDFDA6" data-width="250" data-height="350" data-header="false" data-recommendations="false"></div>
                    </div>


                    <div class="contentRight">
                        <p>Beast Reality ver. 1.00: Coming soon ... </p>
                    </div>
                </div>

                <?php
                    include 'footer.php';
                ?>
            </div>
        </div>
        <div id='fb-root'></div>
            <p><a href="#" id="postToFeed" onclick="publishToFacebook(); return false;"></a></p>
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

