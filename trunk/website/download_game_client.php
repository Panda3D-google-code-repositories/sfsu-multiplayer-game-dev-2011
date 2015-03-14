<?php include "layout/header.php"; ?>
<?php include "layout/leftnav3.php"; ?>
    <div class="content_container">
        <center>
            <table>
                <tr>
                    <td><img src="images/download.png" /></td>
                    <td><h1>Game Client</h1></td>
                </tr>
            </table>
            <div style="margin: 5px 20px 50px 20px;">
                <div class="tip" style="">
                    <center><b>INSTRUCTION</b></center>
                    <i style="color: red;"><br />Click on the link to have the download window open, then click on
                        "Save" to start downloading. Execute setup file from wherever it is stored,
                        and you’ll be able to play the game right away.</i>
                </div>
                <table width="450px" style="text-align: center;" cellpadding="5">
                    <tr><th colspan="3"><br />DOWNLOAD GAME CLIENT<br /><i>Last Updated: June 06, 2012</i></th></tr>
                    <tr>
                        <td align="left" width="50%"><b>Platform</b></td>
                        <td width="50%"><b>Size</b></td>
                        <td align="left" width="50%"><b>Link</b></td>
                    </tr>
                    <tr>
                        <td align="left">Microsoft Windows</td>
                        <td><?php echo round(filesize("download/World_of_Balance_1.32.exe") / 1048576, 2) ?> MB</td>
                        <td align="left"><a href="download/World_of_Balance_1.32.exe">World_of_Balance_1.32.exe</a></td>
                    </tr>
                    <tr>
                        <td align="left">Mac OS X</td>
                        <td><?php echo round(filesize("download/World_of_Balance_1.32.dmg") / 1048576, 2) ?> MB</td>
                        <td align="left"><a href="download/World_of_Balance_1.32.dmg">World_of_Balance_1.32.dmg</a></td>
                    </tr>
                </table>
            </div>
        </center>
    </div>
<?php include "layout/footer2.php"; ?>
