<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" type="text/css" href="css/mainStyle.css" />
        <link rel="stylesheet" type="text/css" href="css/supportStyle.css" />
        <link rel="stylesheet" type="text/css" href="css/template.css" />
        <link rel="stylesheet" type="text/css" href="css/userDashboard.css" />
	<script type="text/javascript">
function checkRegisterForm(form) {
<!--
    if(form.Uname.value == '') {
        alert("Username required!");
        form.Uname.focus();
        return false;
    }
    if(form.Pword.value == '') {
        alert("Password required!");
        form.Uname.focus();
        return false;
    }
    if(form.Email.value == '') {
        alert("Email required!");
        form.Email.focus();
        return false;
    }
    
    var _email = form.Email.value;
    var _atPos = _email.indexOf('@');
    var _dotPos = _email.lastIndexOf('.');
    
    if (_atPos < 1 || _dotPos < _atPos+2 || _dotPos+2 >= _email.length)
    {
        alert("Not a valid e-mail address");
        form.Email.focus();
        return false;
    }

    if(form.Cname.value == '') {
        alert("Character name required!");
        form.Cname.focus();
        return false;
    }
    
    return true;
}
//-->
</script>
        <title>Beast Reality - User Dashboard</title>
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
		    <div id="nSupport">
			    
			    <?php
				include 'supportLeftContent.php';
			    ?>
			    
                        </div>
		    </div>

                    <!-- ################################################################# -->
                    <!-- Content of right panel -->
                    <div class="contentRight"  style="color: #fff;">
                        <!-- TYPE YOUR CONTENT HERE -->
                        <h2 style="margin-left: 220px; margin-bottom: 20px;">Register</h2>

                        <form name="registerForm" action="submitRegister.php" onsubmit="return checkRegisterForm(this);" method="post" >
                            <fieldset>
                                <legend>Registration Form</legend>
                                <p><label for="Uname">Username</label> <input type="text" size="14" maxlength="100" name="Uname" id="Uname" /></p><br />
                                <p><label for="Pword">Password</label> <input type="password" size="14" maxlength="100" name="Pword" id="Pword" /></p><br />
                                <p><label for="Email">E-mail</label> <input type="text" size="14" maxlength="100" name="Email" id="Email" /></p><br />
                                <p><label for="Cname">Character Name</label> <input type="text" size="14" maxlength="100" name="Cname" id="Cmail" /></p><br />
                                <label>&nbsp; </label><input type="submit" value="Submit" class="submit" />
                                <input type="reset" value="Reset" class="submit" />
                            </fieldset>
                        </form>
                    </div>
                </div>
                <?php
                    include 'footer.php';
                ?>
            </div>
        </div>
    </body>
</html>

