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
    if(form.Cname.value == '') {
        alert("Character name required!");
        form.Cname.focus();
        return false;
    }
    
    var _email = form.Email.value;
    var _atPos = _email.indexOf('@');
    var _dotPos = _email.lastIndexOf('.');
    
    if (_atpos < 1 || _dotpos < _atpos+2 || _dotpos+2 >= _email.length)
    {
        alert("Not a valid e-mail address");
        form.Email.focus();
        return false;
    }
    return true;
}

//-->

</script>