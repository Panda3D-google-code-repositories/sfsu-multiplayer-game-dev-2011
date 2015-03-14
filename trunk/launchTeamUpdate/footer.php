<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title></title>
        <link rel="stylesheet" type="text/css" href="css/template.css" />
    </head>
    <body>
        <div class="bottom">
            <p>Copyright &copy;
            <?php
            $startYear = 2011;
            $thisYear = date('y');
            if ($startYear == $thisYear) {
                echo $startYear;
            } else {
                echo "{$startYear}&#8211;{$thisYear}";
            }
            ?>
            San Francisco State University - Department of Computer Science. All Rights Reserved.</p>
            <a href="http://www.panda3d.org" target="_blank"><img src="images/thumbnails/panda3dv2e.png" alt="panda 3d logo" /></a>
            <a href="http://www.python.org" target="_blank"><img src="images/thumbnails/python-logo.png" alt="python logo" /></a>
            <a href="http://www.sfsu.edu" target="_blank"><img src="images/thumbnails/sfsu.jpg" alt="sfsu logo" /></a>
        </div>

    </body>
</html>
