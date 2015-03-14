<?php
/**
 * Database functionality
 *
 * This file contains the functions for database functionality for
 * our both modules, i.e. QuestionBank and
 * User.
 * include_once(db.php) to use them.
 *
 * @version 0.1
 *          Version History:
 *          0.1  Surabhi created
 *@author   Surabhi Nigam
 */
?>

<?php

/*mysql_connect("thecity.sfsu.edu:9898", "team1", "Pi2aixie") or die(mysql_error());
mysql_select_db("team1db") or die(mysql_error());*/

$con=mysql_connect("thecity.sfsu.edu:9898", "team1", "Pi2aixie") or die("Query failed with error: ".mysql_error());
mysql_select_db("team1db") or die("Query failed with error: ".mysql_error());
#if(!$con){
   # die('Could not connect: '. mysql_error());
#}


#
# Manori's functions
#This function fetches all the pending questions for the validator from Question Bank

function getPendingQuestions() {
	$sql = "select * from QuestionBank where status='Pending'";
    
	$result = mysql_query($sql) or die("Query failed with error: ".mysql_error());

	$resultArr = array();

	while ($row = mysql_fetch_array($result)) {
        array_push($resultArr, $row);
    }

    sort($resultArr);

    return $resultArr;
}

#This function approves the question in the Question Bank by updating the status, vid and vdate
function updateApprovedQuestionV($vid,$ts,$qid,$uid) {
	$sql1 = "UPDATE QuestionBank SET vid='".$vid."',vdate='".$ts."',status='Approved' where qid='".$qid."'";
	$sql2 = "UPDATE User SET qCreated=qCreated+1 WHERE uid='".$uid."'";
	$result1 = mysql_query($sql1) or die("Query failed with error: ".mysql_error());
	$result2 = mysql_query($sql2) or die("Query failed with error: ".mysql_error());
	return $result1;

}

#This function rejects the question in the Question Bank by updating the status, vid and vdate
function updateRejectedQuestionV($vid,$ts,$qid) {
	$sql = "UPDATE QuestionBank SET vid='".$vid."',vdate='".$ts."',status='Rejected' where qid='".$qid."'";

	$result = mysql_query($sql) or die("Query failed with error: ".mysql_error());
	return $result;

}

#This function fetches all of the question details for a particular question in the Question Bank
//function getQuestionInfo($qid) {
//    $sql = "SELECT * FROM QuestionBank WHERE qid='".$qid."'";
//    $result = mysql_query($sql) or die("Query failed with error: ".mysql_error());
//
//	$resultArr = array();
//
//	while ($row = mysql_fetch_array($result)) {
//        array_push($resultArr, $row);
//    }
//
//    return $resultArr;
//}

#This function fetches all the feedbacks, their reviewer and rating for a question from the Question Bank
function getAllFeedbacks($qid) {
	$sql = "SELECT * FROM FeedbackBank WHERE qid='".$qid."'";

	$result = mysql_query($sql) or die("Query failed with error: ".mysql_error());

	$resultArr = array();

	while ($row = mysql_fetch_array($result)) {
        array_push($resultArr, $row);
    }

    sort($resultArr);

    return $resultArr;
}

    #Given a user_id, return username.
    function get_username_by_user_id($uid) {
        $sql = "SELECT username FROM user WHERE user_id ='".$uid."'";
        $result = mysql_query($sql) or die("Query failed with error: ".mysql_error());
        $username = mysql_fetch_row($result);
        $username1 = $username[0];
        return $username1;
    }


####Sindhu's functions



function get_user_id_by_username($username) {
    $username = mysql_real_escape_string($username);
    $result = mysql_query("SELECT uid FROM User WHERE username = '"
        . $username . "'");
    if (mysql_num_rows($result) > 0)
        return mysql_result($result, 0);
    else
        return null;
}

function get_user_id_by_username_password($username,$password) {
    $uname= mysql_real_escape_string($username);
        $result = mysql_query("SELECT uid FROM User WHERE username = '"
            . $username . "' AND password='".$password."'");
        if (mysql_num_rows($result) > 0)
        return mysql_result($result, 0);
        else
        return null;
}

//function get_username_by_user_id($id) {
//    $uname= mysql_real_escape_string($id);
//    $result = mysql_query("SELECT username From User WHERE uid = '"
//            .$id."'");
//    if (mysql_num_rows($result) > 0)
//        return mysql_result($result, 0);
//    else
//        return null;
//}

function create_user ($fname,$lname,$uname,$email,$password,$image_name){
        $fname = mysql_real_escape_string($fname);
        $lname = mysql_real_escape_string($lname);
        $uname = mysql_real_escape_string($uname);
        $email = mysql_real_escape_string($email);
        $password = mysql_real_escape_string($password);
        $image_name = mysql_real_escape_string($image_name);
        //$gender = mysql_real_escape_string($gender);
        mysql_query("INSERT INTO User(first_name,last_name,username,email,password,pic) VALUES ('" . $fname
            . "', '" .$lname."','".$uname."','".$email ."','" . $password . "','".$image_name."')");
    }

    function obtain_user($uname){
    $sql = "SELECT * FROM User WHERE username='".$uname."'";
    $result = mysql_query($sql) or die("Query failed with error: ".mysql_error());
    return( mysql_fetch_array($result));
}

function getQuestionsCL($course,$level)
     {
    $sql = "SELECT QuestionBank.qid,QuestionBank.type,QuestionBank.question,QuestionBank.gold,QuestionBank.timelimit,QuestionBank.first,QuestionBank.second,QuestionBank.third,QuestionBank.fourth,QuestionBank.answer FROM QuestionBank,CourseBank,TopicBank WHERE CourseBank.sid='".$course."' AND CourseBank.sid=TopicBank.sid AND TopicBank.tid=QuestionBank.tid AND QuestionBank.level='".$level."' AND QuestionBank.status='Approved'";
    $result = mysql_query($sql);

    $resultArr = array();

    while ($row = mysql_fetch_array($result)) {
        array_push($resultArr, $row);
    }

    sort($resultArr);

    return $resultArr;

     }

     function create_feedback($qid,$reviewer,$comment,$rating){
        $comment = mysql_real_escape_string($comment);

        mysql_query("INSERT INTO FeedbackBank(qid,reviewer,comment,rating) VALUES (" . $qid
            . ", " .$reviewer.",'".$comment."',".$rating.")");
    }

    function getPlayerRankings()
	     {
	         $result=mysql_query("SELECT * FROM User ORDER BY gold DESC");
	         $resultArr = array();

	    while ($row = mysql_fetch_array($result)) {
	        array_push($resultArr, $row);
	    }
	     return $resultArr;
     }

##Surabhi' functions


function getUserQuestions($userId) {
    $sql = "SELECT * FROM QuestionBank WHERE uid='".$userId."' ORDER BY qid DESC";
    $result = mysql_query($sql);

    $resultArr = array();

    while ($row = mysql_fetch_array($result)) {
        array_push($resultArr, $row);
    }

    return $resultArr;
}

/**
 *
 * @param <type> $userID
 * @return <type>
 * returns the array of rows of pending questions of a particular user.
 *
 * function to be used in viewquestions.php
 */
function getUserPendingQuestions($userID){
    $sql = "SELECT * FROM QuestionBank WHERE uid='".$userID."' AND status='Pending' ORDER BY qid DESC";
    $result = mysql_query($sql);

    $resultArr = array();

    while ($row = mysql_fetch_array($result)) {
        array_push($resultArr, $row);
    }

    //sort($resultArr);

    return $resultArr;
}


function getUserApprovedQuestions($userID){
    $sql = "SELECT * FROM QuestionBank WHERE uid='".$userID."' AND status='Approved' ORDER BY qid DESC";
    $result = mysql_query($sql);

    $resultArr = array();

    while ($row = mysql_fetch_array($result)) {
        array_push($resultArr, $row);
    }

    //sort($resultArr);

    return $resultArr;
}

function getUserRejectedQuestions($userID){
    $sql = "SELECT * FROM QuestionBank WHERE uid='".$userID."' AND status='Rejected' ORDER BY qid DESC";
    $result = mysql_query($sql);

    $resultArr = array();

    while ($row = mysql_fetch_array($result)) {
        array_push($resultArr, $row);
    }

    //sort($resultArr);

    return $resultArr;
}

function getCourseList(){
   $sql = "SELECT * FROM CourseBank ";
   $result = mysql_query($sql);
   $resultArr = array();

    while ($row = mysql_fetch_array($result)) {
        array_push($resultArr, $row);
    }


    return $resultArr;
}

function getSid($course, $section){
    $sql = "SELECT sid FROM CourseBank WHERE course='".$course."'";
//    $sql = "SELECT sid FROM CourseBank WHERE course='".$course."' AND section='".$section."'";
   $result = mysql_query($sql);
   if (mysql_num_rows($result) > 0)
        return mysql_result($result, 0);
        else
        return null;
}


function getDistinctCourseList(){
   $sql = "SELECT DISTINCT cid FROM CourseBank ";
   $result = mysql_query($sql);
   $resultArr = array();
   while ($row = mysql_fetch_array($result)) {
        array_push($resultArr, $row);
    }

   return $resultArr;
}


/*function getCourseTopics($schedule){
    $sql = "SELECT topic FROM CourseBank WHERE schedule='".$schedule. "'";
   $result = mysql_query($sql);
   $row = mysql_fetch_array($result);
   return $row;
}*/

function getTopics($sid, $level){
    $sql = "SELECT topic FROM TopicBank WHERE sid='".$sid."' AND level='".$level."'";
   $result = mysql_query($sql);
   $resultArr = array();
   while ($row = mysql_fetch_array($result)) {
        array_push($resultArr, $row);
    }

   return $resultArr;
}

function getTid($level, $sid, $topic){
    $sql = "SELECT tid FROM TopicBank WHERE sid='".$sid."' AND level='".$level."' AND topic='".$topic."'";
   $result = mysql_query($sql);
   if (mysql_num_rows($result) > 0)
        return mysql_result($result, 0);
        else
        return null;
}


function makeQuestion1($uid, $tid, $title, $type, $level, $question, $gold, $first, $second, $third, $fourth, $answer, $timelimit){
    $addTime = date("Y-m-d");
    $sql = "INSERT INTO questions(question_type, question, correctanswer, option1, option2, option3, option4, hint, points, username, timelimit, level, created_date, course, topic)
            VALUES ('".$type."', '".$question."', '".$answer."', '".$first."', '".$second."', '".$third."', '".$fourth."', '".$question."', '".$question."', '".$question."', '".$question."', '".$question."', '".$question."')";
      if (mysql_query($sql)) {
        return mysql_insert_id();
    } else {
        return -1;
    }
}


function getThisQuestion($quesID){
    $sql="SELECT * FROM QuestionBank WHERE qid='".$quesID."'";
    $result = mysql_query($sql);
    $row = mysql_fetch_array($result);
    return $row;
     }


     function editQuestion($qid, $tid, $title, $type, $level, $question, $gold, $first, $second, $third, $fourth, $answer, $timelimit){

    $sql="UPDATE QuestionBank SET tid='".$tid."',title='".$title."',type='".$type."', level='".$level."', question='".$question."', gold='".$gold."', first='".$first."', second='".$second."', third='".$third."', fourth='".$fourth."', answer='".$answer."', timelimit='".$timelimit."'  WHERE qid='".$qid."'";
    $result = mysql_query($sql);
    if (mysql_query($sql)) {
        return true;
    } else {
        return false;
    }
     }

     function getQuestionSid($tid){

   $sql = "SELECT sid FROM TopicBank WHERE tid='".$tid."'";
   $result = mysql_query($sql);
   //$row = mysql_fetch_array($result);
    //return $row;
   if (mysql_num_rows($result) > 0)
        return mysql_result($result, 0);
        else
        return null;
     }

  function getCourseSection($questionSid){
   $sql = "SELECT course, section FROM CourseBank WHERE sid='".$questionSid."'";
   $result = mysql_query($sql);
   $row = mysql_fetch_array($result);
    return $row;
   /*if (mysql_num_rows($result) > 0)
        return mysql_result($result, 0);
        else
        return null;*/

     }

   function getQuestionTopic($tid){
   $sql = "SELECT topic FROM TopicBank WHERE tid='".$tid."'";
   $result = mysql_query($sql);
   if (mysql_num_rows($result) > 0)
        return mysql_result($result, 0);
        else
        return null;
     }

//ishita's functions
function update_user ($fname,$lname,$uname,$email,$bday){
        //$fname = mysql_real_escape_string($fname);
        //$lname = mysql_real_escape_string($lname);
        $uname = mysql_real_escape_string($uname);
       // $email = mysql_real_escape_string($email);
       // $bday = mysql_real_escape_string($bday);

       mysql_query(" UPDATE User SET first_name ='".$fname."',last_name ='".$lname."',email = '".$email."', bday = '".$bday."' WHERE username = '".$uname."'");

    }
      function update_password ($uname,$newPassword){

       $uname = mysql_real_escape_string($uname);
       mysql_query(" UPDATE User SET password ='".$newPassword."'  WHERE username = '".$uname."'");

    }
    function update_image ($uname,$imagePath){

       $uname = mysql_real_escape_string($uname);
       mysql_query(" UPDATE User SET pic ='".$imagePath."'  WHERE username = '".$uname."'");

    }
    function update_gold ($uname,$totalGold){

       $uname = mysql_real_escape_string($uname);
       mysql_query(" UPDATE User SET gold ='".$totalGold."'  WHERE username = '".$uname."'");

    }

    function update_expe($uname,$exper) {
        $uname = mysql_real_escape_string($uname);
        mysql_query(" UPDATE User SET exp = '".$exper."' WHERE username = '".$uname."'");
    }

    function update_questionLog($qid,$uid,$status) {
        $addTime = date("Y-m-d H:i:s.000");
        $sql = "INSERT INTO QuestionsLog(qid, uid, date, status) VALUES ('".$qid."', '".$uid."', '".$addTime."', '".$status."')";
        if (mysql_query($sql)) {
            return "T";
        } else {
            return "F";
        }
    }

    function get_questionLog($uid) {
        $sql = "SELECT * FROM QuestionsLog WHERE uid='".$uid."'";
        $result = mysql_query($sql);
        return $result;
    }

    function get_FriendsList($uid) {
        $sql = "SELECT * FROM friendlist WHERE flid='".$uid."'";
        $result = mysql_query($sql) or die("Query failed with error: ".mysql_error());
        if(mysql_num_rows($result) == 1)
            return $result;
        else {
            $sql = "Insert into friendlist(flid, friends) values($uid,'')";
            $result2 = mysql_query($sql) or die("Query failed with error: ".mysql_error());
            $sql = "SELECT * FROM friendlist WHERE flid='".$uid."'";
            $result = mysql_query($sql) or die("Query failed with error: ".mysql_error());
            return $result;
        }
    }

    function get_autoCompleteFriends($queryString) {
        $sql = "select uid, first_name, last_name, username from User where (first_name LIKE '%$$queryString%' or last_name LIKE '%$queryString%' or username LIKE '%$queryString%')";
        $result = mysql_query($sql);
        $row = mysql_fetch_array($result);
        return $row;
    }
?>