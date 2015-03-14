<?php
/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
?>
<?PHP
/* LOGIN SEQUENCE
 * This php code must be included at the top of every page
 *
 */
session_start();
require('user.php');
require('course.php');
require('question.php');
if(session_is_registered('userinfo')) {
    /* user is logged in
     * retreive the user object created when checked
     */
   $userinfo=unserialize($_SESSION['userinfo']);
}
?>
<?PHP
$answer="";
$gold=0;
$choice= $_POST['correct_answer'];
    switch($choice) {
    case 1:   $answer="first"; break;
    case 2:   $answer="second"; break;
    case 3:   $answer="third"; break;
    case 4:   $answer="fourth"; break;
    default: break;
}
$userid=$userinfo->getUid();

$course=$_POST['course'];
if(preg_match('/^1/',$course)){
    switch($_POST['level']){
        case 'Easy': $gold=10;break;
        case 'Medium': $gold=20;break;
        case 'Tough': $gold=30; break;
    }
}


if(preg_match('/^2/',$course)){
    switch($_POST['level']){
        case 'Easy': $gold=40;break;
        case 'Medium': $gold=50;break;
        case 'Tough': $gold=60; break;
    }
}

if(preg_match('/^3/',$course)){
    switch($_POST['level']){
        case 'Easy': $gold=70;break;
        case 'Medium': $gold=80;break;
        case 'Tough': $gold=90; break;
    }
}

if(preg_match('/^4/',$course)){
    switch($_POST['level']){
        case 'Easy': $gold=100;break;
        case 'Medium': $gold=110;break;
        case 'Tough': $gold=120; break;
    }
}

if(preg_match('/^5/',$course)){
    switch($_POST['level']){
        case 'Easy': $gold=130;break;
        case 'Medium': $gold=140;break;
        case 'Tough': $gold=150; break;
    }
}

if(preg_match('/^6/',$course)){
    switch($_POST['level']){
        case 'Easy': $gold=160;break;
        case 'Medium': $gold=170;break;
        case 'Tough': $gold=180; break;
    }
}

if(preg_match('/^7/',$course)){
    switch($_POST['level']){
        case 'Easy': $gold=190;break;
        case 'Medium': $gold=200;break;
        case 'Tough': $gold=210; break;
    }
}

if(preg_match('/^8/',$course)){
    switch($_POST['level']){
        case 'Easy': $gold=220;break;
        case 'Medium': $gold=230;break;
        case 'Tough': $gold=240; break;
    }
}

$splitCourse=explode('-',$_POST['course']);
//echo $splitCourse[0] ." and ".$splitCourse[1];
$sid=CourseController::getSid($splitCourse[0],$splitCourse[1]);
//echo "sid was:: ".$sid;
$tid=CourseController::getTid($_POST['level'], $sid, $_POST['topic']);
$result = QuestionController::editQuestion($_POST['qid'], $tid, $_POST['title'], $_POST['level'], $_POST['question'], $gold, $_POST['first'], $_POST['second'], $_POST['third'], $_POST['fourth'], $answer, $_POST['time']);
//if ($result== true) {
    echo "<meta http-equiv='refresh' content='0;url=../questionaddedconfirmation.php'>";
//header("Location:questionaddedconfirmation.php");
//} else {
//}
?>