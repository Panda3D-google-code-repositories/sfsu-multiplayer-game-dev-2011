<!--
To change this template, choose Tools | Templates
and open the template in the editor.
-->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title></title>
    </head>
    <body>
        <?php  require('course.php');
               require('question.php');
               $userID=3;?>
        <?php

        echo "status is::". $_GET['status'];
     if($_GET['status']=='Pending')      {
      $quesArr = QuestionController::getUserPendingQuestions($userID);
     }
     if($_GET['status']=='Approved'){
     $quesArr = QuestionController::getUserApprovedQuestions($userID);
     }
     if($_GET['status']=='Rejected'){
      $quesArr = QuestionController::getUserRejectedQuestions($userID);


     $numOfQuesPages = (int) (sizeof($quesArr) / $rowsPerPage);
if (sizeof($quesArr) % $rowsPerPage != 0) {
  $numOfQuesPages++;
}

if ($_GET['page'] == "") {
    $_GET['page'] = 1;

}
   }


    if ($quesArr[0] == null) {
                                            echo "<tr><td colspan='3'>No Questions written by you</td><td></td></tr>";
                                        } else {
                                            echo "<tr><th>Question Title</th><th>Course</th><th>Topic</th><th >Level</th><th>Date</th><th>Gold</th><th>Status</th></tr>";
                                            $page = ($_GET['page'] - 1) * $rowsPerPage;
                                            $endPage = $page + $rowsPerPage;
                                            for ( ; $page < $endPage; $page++) {
                                                if ($quesArr[$page] == null) {
                                                    break;
                                                }
                                                echo "<tr>";
                                                if ($quesArr[$page] != null) {
                                                    echo "<td id='question_text'><a href=#>".$quesArr[$page]->getTitle() ."</a></td><td>".
                                                        $quesArr[$page]->getCourseId()."</td><td>".
                                                        $quesArr[$page]->getTitle()." </td><td>".
                                                        $quesArr[$page]->getLevel()."</td><td>".
                                                        $quesArr[$page]->getQDate()."</td><td>".
                                                        $quesArr[$page]->getGold()."</td><td>".
                                                        $quesArr[$page]->getStatus()."</td>";
                                                }
                                                echo "</tr>";
                                            }
                                        }
             ?>
    </body>
</html>
