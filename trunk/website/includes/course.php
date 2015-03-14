<?php
/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
require_once("newDB.php");

class Course {
    private $schedule;
    private $cId;
    private $section;
    private $topic;

public function getSchedule() {
        return $this->schedule;
    }

public function getCId() {
        return $this->cId;
    }

    public function getSection() {
        return $this->section;
    }
 public function getTopic() {
        return $this->topic;
    }

    public function setSchedule($courseSchedule){
        $this->schedule=$courseSchedule;
    }

public function setCId($courseID) {
        $this->cId = $courseID;
    }

public function setSection($courseSection) {
        $this->section = $courseSection;
    }

    public function setTopic($courseTopic) {
        $this->topic = $courseTopic;
    }
}
class CourseController {
    /**
     * Constructor for question controller
     * @todo to be written
     * @return
     */
    public function __construct() {

    }

  /**
     * Returns an instantiation of a new question object.
     * @return Question instatiation of a question object
     */
    public static function getCourse() {
        return new Course();
    }

    public static function getCourseList() {
    $courseDataArr = getCourseList();
        $courseObjArr = array();

        for ($i = 0; $i < sizeof($courseDataArr); $i++) {
            $courseObj = CourseController::getCourse();

            $courseObj->setSchedule($courseDataArr[$i]['sid']);
            $courseObj->setCId($courseDataArr[$i]['course']);
           $courseObj->setSection($courseDataArr[$i]['section']);

             array_push($courseObjArr, $courseObj);
        }

        return $courseObjArr;
    }

    public static function getDistinctCourseList(){
        $courseDistinctArray = array();
        $courseDistinctArray=getDistinctCourseList();
        return $courseDistinctArray;
    }

/*public static function getCourseTopics($schedule){
    $courseTopics=getCourseTopics();
    $courseTopicsArray=split(',', $courseTopics);
    return $courseTopicsArray;

}*/


public static function getTopics($sid, $level){
 /*  $courseTopicsArr=getTopics($courseID, $level);
return $courseTopicsArr;*/
    $courseTopicArr = getTopics($sid, $level);
    //echo "course array is: $courseTopicArr[0] and $cousreTopicsArr[1]";
        $courseObjArr = array();

        for ($i = 0; $i < sizeof($courseTopicArr); $i++) {
            $courseObj = CourseController::getCourse();

            //$courseObj->setSchedule($courseDataArr[$i]['schedule']);
            $courseObj->setTopic($courseTopicArr[$i]['topic']);
           //$courseObj->setSection($courseDataArr[$i]['section']);

             array_push($courseObjArr, $courseObj);
        }
       //echo "  array is ::::::". $courseObjArr[0]->getTopic()." and ". $courseObjArr[1]->getTopic();
        return $courseObjArr;
}

public static function getQuestionCourse($tid){
//echo "tid is:". $tid ;
$questionSid=getQuestionSid($tid);
//echo "question sid is". $questionSid;
$courseDataArr = getCourseSection($questionSid);
//echo "course is: ". $courseDataArr;
$courseObj = CourseController::getCourse();
$courseObj->setSection($courseDataArr['section']);
$courseObj->setCId($courseDataArr['course']);
//$questionCourse=$courseDataArr['course']."-".$courseDataArr['section'];
//echo "course & section is::".$questionCourse=$courseDataArr['course']."-".$courseDataArr['section'];
return $courseObj;
}

public static function getSid($course, $section){
   $sid=getSid($course, $section);
   return $sid;
}

public static function getTid($level, $sid, $topic){

$tid=getTid($level, $sid, $topic);
return $tid;
}



}



?>
