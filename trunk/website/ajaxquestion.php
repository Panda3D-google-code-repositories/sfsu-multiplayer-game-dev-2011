<?php
session_start();
require("includes/user.php");
require("includes/question.php");
require("includes/feedback.php");
$_SESSION['currentPage'] = "playGame";
if($_GET["from"]==0)
{

//$_SESSION["sid"]=1;
//$_SESSION["level"]="tough";

if($_GET["id"]==0)
{

$quesarr=QuestionController::getQuestionsCL($_SESSION["course"],$_SESSION["level"]);

$_SESSION["noofq"]=sizeof($quesarr);
$_SESSION["qindex"]=0;
//$_SESSION["quesarr"]=$quesarr;
$_SESSION["cans"]=0;
$_SESSION["wans"]=0;
$_SESSION["tans"]=0;
$_SESSION["ugold"]=0;
$_SESSION["qscompleted"]=false;
$_SESSION["quit"]=false;
}
if($_GET["id"]==2)
{
    $userinfo=unserialize($_SESSION['userinfo']);
    $uid=$userinfo->getUid();
    //$uid=1;
    $c=$_GET["comment"];
    $r=$_GET["rating"];
    $q=$_SESSION["qid"];
    FeedbackController::create_feedback ($q,$uid,$c,$r);

}

if($_SESSION["noofq"]>0)
{
   // $quesarr=$_SESSION["quesarr"];
   $quesarr=QuestionController::getQuestionsCL($_SESSION["course"],$_SESSION["level"]);
    $qindex=$_SESSION["qindex"];
    $ques=$quesarr[$qindex]->getQuestion();
    $type=$quesarr[$qindex]->getQType();
    $first=$quesarr[$qindex]->getFirst();
    $second=$quesarr[$qindex]->getSecond();
    $third=$quesarr[$qindex]->getThird();
    $fourth=$quesarr[$qindex]->getFourth();
    $answer=$quesarr[$qindex]->getAnswer();
    $timelimit=$quesarr[$qindex]->getTime();
    $qgold=$quesarr[$qindex]->getGold();
    $qid=$quesarr[$qindex]->getQuestId();

    $_SESSION["qid"]=$qid;
    $_SESSION["ans"]=$answer;
    $_SESSION["qgold"]=$qgold;

    $noofq=$_SESSION["noofq"];
    $_SESSION["noofq"]=$noofq-1;
    $_SESSION["qindex"]=$qindex+1;

 //<input type=\"button\" value=\"Quit Game\" id=\"quit_game\" onclick=\"next(1,1);\">

    $result= "
            <div >
                <a href=\"javascript:next(1,1);\"><img id=\"quitgame\" src=\"images/gquit.jpg\"  alt=\"Quit Game\" /></a>
            </div>
            <div id=\"drop_downs\">
                <label id=\"label_text\"> Course:".$_SESSION["course"]."</label>
                <label id=\"label_text\">Level:".$_SESSION["level"]."</label>
                <label id=\"label_text\">Gold Earned:".$_SESSION["ugold"]."</label>
            </div>
            <div id=\"write_question\">
                <br /><br />
                <div id=\"question\"><table width=\"100%\"><tr><td>".$ques." </td></tr></table>
                </div>
                <div id=\"choices\"> <form name=\"qform\">
                <table border=\"0\" cellpadding=\"10\">";

         if($type === "MC")
           $result=$result."<tr>
		            <td><input type=\"radio\" name=\"choice\" value=\"first\">".$first."</td>
		            <td><input type=\"radio\" name=\"choice\" value=\"second\">".$second."</td>
		              </tr>
		               <tr>
		           <td><input type=\"radio\" name=\"choice\" value=\"third\">".$third."</td>
		           <td><input type=\"radio\" name=\"choice\" value=\"fourth\">".$fourth."</td>
		                                   </tr>";
		           else
		              $result=$result."<tr>
		            <td><input type=\"radio\" name=\"choice\" value=\"first\">".$first."</td>
		            </tr><tr>
		            <td><input type=\"radio\" name=\"choice\" value=\"second\">".$second."</td>
           </tr>";
       $result=$result. "</table></div>



<script>timer(".$timelimit.");</script>
<div id=\"noa\"></div>
<a name=\"submit\" href=\"javascript:submitTimeout(0);\"><img id=\"qsubmit\"  src=\"images/qsubmit.jpg\"  alt=\"Submit\" /></a>
</form></div><div id=\"clock_time\"></div>";

       // <input type=\"button\" value=\"Submit\" name=\"submit\" onclick=\"submitTimeout(0);\">
//name=\"submitbutton\" id=\"submit_button\"/>
  //<script>addhandlers(document.qform);</script>";

        //$result=$_SESSION["ugold"];
  echo $result;
 }
else
{

$_SESSION["qscompleted"]=true;
echo "<script>location.replace(\"results.php\");</script>";
//header('Location:results.php' );
}

}
else
{
   $_SESSION["quit"]=true;

 echo "<script>location.replace(\"results.php\");</script>";
 //header('Location:results.php' );
}
?>
