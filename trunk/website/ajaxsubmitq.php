<?PHP
    session_start();
    require('includes/user.php');
    require('includes/question.php');
//    require('includes/db.php');
//    $_SESSION['currentPage'] = "store_validateQuestions.php";
//    if(session_is_registered('userinfo')) {
        $userinfo=unserialize($_SESSION['userinfo']);
//    }else {
//        header("Location:signin.php");
//    }
//    $_SESSION['currentPage']='playGame';
    if($_GET["id"]==0)
    {
         $subans=$_GET["answer"];
         if($subans == $_SESSION["ans"])
         {
             $awnser="T";
             $ca=$_SESSION["cans"];
             $_SESSION["cans"]=$ca+1;
             $ugold=$_SESSION["ugold"];
             $_SESSION["ugold"]=$ugold+$_SESSION["qgold"];
         }
         else
         {
             $awnser="F";
             $wa=$_SESSION["wans"];
             $_SESSION["wans"]=$wa+1;
         }
         $result = QuestionController::updateQuestionLog($_SESSION["qid"],$userinfo->getUid(),$awnser);
         //echo $result;
    }
    else
    {
        $ta=$_SESSION["tans"];
        $_SESSION["tans"]=$ta+1;
    }
    
    echo"<div id=\"feedback\"><br><b>&nbsp &nbsp Please provide feedback on this question</b><br>
         <form name=\"fform\">
        <table align=\"left\"><tr><td>&nbsp   Comments:</td>
         <td><textarea class=\"feedback_text\" name=\"comtext\" rows=\"2\" cols=\"20\"></textarea>
        </td></tr><tr><td>&nbsp   Rating:</td><td>&nbsp <select name=\"rating\">
          <option value=\"1\">1<option value=\"2\">2<option value=\"3\">3
          <option value=\"4\">4<option value=\"5\" selected=\"selected\">5<option value=\"6\">6
          <option value=\"7\">7<option value=\"8\">8<option value=\"9\">9
          <option value=\"10\">10</select></td></tr><tr><td></td><td></td></tr>
        <tr><td></td><td>&nbsp<a href=\"javascript:next(2,0);\"><img src=\"images/post.jpg\"  alt=\"Post Feedback\" />
       &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
<a href=\"javascript:next(1,0);\"><img src=\"images/skip.jpg\"  alt=\"Skip Feedback\" />
 
           </td></tr></table> </form>  </div>";

//<input type=\"button\" value=\"Post Feedback\" onclick=\"next(2,0);\">
         // <input type=\"button\" value=\"Skip Feedback\" onclick=\"next(1,0);\">

?>
