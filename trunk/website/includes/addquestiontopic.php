<?php require('course.php');?>
<?php if(isset($_GET['course'])&& isset($_GET['level'])){
    $splitCourse=explode('-',$_GET['course']);
    $sid=CourseController::getSid($splitCourse[0],1);
?>

<?php $courseTopicsArr = CourseController::getTopics($sid, $_GET['level']); ?>
<?php for($j=0; $j<sizeof($courseTopicsArr); $j++) { ?>
    <option class="topicOption"><?php echo $courseTopicsArr[$j]->getTopic(); ?></option>
<?php } }  ?>

