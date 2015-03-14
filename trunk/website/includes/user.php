<?php
require_once("newDB.php");

class User {
    private $uid = "";
    private $username = "";
    private $password = "";
    private $first_name = "";
    private $last_name = "";
    private $email = "";
    private $bday = "";
    //private $gender = "";
    private $level = "";
    private $expe ="";
    private $gold = "";
    private $role = "";
    private $isBanned = "";
    private $deaths = "";
    private $bugkills = "";
    private $qcreated = "";
    private $avatar = "";

    public function getUid() {
        return $this->uid;
    }

    public function getUserName() {
        return $this->username;
    }

    public function getPassword() {
        return $this->password;
    }

    public function getFirstName() {
        return $this->first_name;
    }

    public function getLastName() {
        return $this->last_name;
    }

    public function getEmail() {
        return $this->email;
    }

    public function getBday() {
        return $this->bday;
    }

    //public function getGender() {
      //  return $this->gender;
    //}

    public function getLevel() {
        return $this->level;
    }

    public function getExp() {
        return $this->expe;
    }

    public function getGold() {
        return $this->gold;
    }

    public function getRole() {
        return $this->role;
    }

    public function getIsBanned() {
        return $this->isBanned;
    }

    public function getDeaths() {
        return $this->deaths;
    }

    public function getBugKills() {
        return $this->bugkills;
    }

    public function getQCreated() {
        return $this->qcreated;
    }

    public function getAvatar() {
        return $this->avatar;
    }



     public function setUid($uid) {
        $this->uid = $uid;
    }

    public function setUserName($username) {
        $this->username=$username;
    }

    public function setPassword($password) {
        $this->password=$password;
    }

    public function setFirstName($first_name) {
        $this->first_name=$first_name;
    }

    public function setLastName($last_name) {
        $this->last_name=$last_name;
    }

    public function setEmail($email) {
        $this->email=$email;
    }

    public function setBday($bday) {
        $this->bday=$bday;
    }

    //public function setGender($gender) {
      //  $this->gender=$gender;
    //}

    public function setLevel($level) {
        $this->level=$level;
    }

    public function setExp($expe) {
        $this->expe=$expe;
    }

    public function setGold($gold) {
        $this->gold=$gold;
    }

    public function setRole($role) {
        $this->role=$role;
    }

    public function setIsBanned($isBanned) {
        $this->isBanned=$isBanned;
    }

    public function setDeaths($deaths) {
        $this->deaths=$deaths;
    }

    public function setBugKills($bugkills) {
        $this->bugkills=$bugkills;
    }

    public function setQCreated($qcreated) {
        $this->qcreated=$qcreated;
    }

    public function setAvatar($avatar) {
        $this->avatar=$avatar;
    }

}

class UserController {
/* MHS: format todo to conform to phpdocu standard
 * MHS: todo should indicate what needs to be done
 * MHS: basic planned functionality should be included in todo header
 */
    /**
     * Constructor for question controller
     * @todo to be written
     * @return
     */
    public function __construct() {

    }

    /**
     * Returns an instantiation of a new user object.
     * @return Question instatiation of a user object
     */
    public static function getUser() {
        return new User();
    }

    public static function get_user_id_by_username($username)
    {
        return(get_user_id_by_username($username));
    }

    public static function get_user_id_by_username_password($username,$password)
    {
        return (get_user_id_by_username_password($username,$password));

    }

    public static function create_user ($fname,$lname,$uname,$email,$password,$image_name){
         create_user ($fname,$lname,$uname,$email,$password,$image_name);
    }

    public static function obtain_user($uname)
    {
        $userinfo=obtain_user($uname);
        $myUser = UserController::getUser();
        $myUser->setUid($userinfo['user_id']);
        $myUser->setUserName($userinfo['username']);
        $myUser->setPassword($userinfo['password']);
        $myUser->setFirstName($userinfo['first_name']);
        $myUser->setLastName($userinfo['last_name']);
        $myUser->setEmail($userinfo['email']);
//        $myUser->setBday($userinfo['bday']);
//        $myUser->setLevel($userinfo['level']);
//        $myUser->setExp($userinfo['exp']);
//        $myUser->setGold($userinfo['gold']);
//        $myUser->setRole($userinfo['role']);
//        $myUser->setIsBanned($userinfo['isBanned']);
//        $myUser->setDeaths($userinfo['deaths']);
//        $myUser->setBugkills($userinfo['bugkills']);
//        $myUser->setQCreated($userinfo['qcreated']);
//        $myUser->setAvatar($userinfo['pic']);
//        $myUser->setExp($userinfo['exp']);
        return $myUser;
    }

    public static function getPlayerRankings()
	    {
	        $playerinfo =getPlayerRankings() ;

			$playerinfoObj = array();

	        for ($i = 0; $i < sizeof($playerinfo); $i++) {
	            $plrObj = UserController::getUser();

	                        $plrObj->setUserName($playerinfo[$i]['username']);
	                        $plrObj->setGold($playerinfo[$i]['gold']);
	            array_push($playerinfoObj, $plrObj);
	        }

	        return $playerinfoObj;

    }

	/**
	 *Manori's function for getting the username given the reviewer Id
	 */
    public static function get_username_by_id($uid) {
        $reviewername=get_username_by_user_id($uid);
        return $reviewername;
    }

	public static function get_user($user,$first_name, $last_name, $email, $bday , $level, $expe,
	            $gold,$role,$isBanned,$deaths,$bugkills,$qcreated,$password , $imagePath )
	    {
	         $userObj = UserController::getUser();
	         $userObj->setUserName($user);
	         $userObj->setFirstName($first_name);
	         $userObj->setLastName($last_name);
	         $userObj->setEmail($email);
	         $userObj->setBday($bday);
	         $userObj->setLevel($level);
	         $userObj->setExp($expe);
	         $userObj->setGold($gold);
	         $userObj->setRole($role);
	         $userObj->setIsBanned($isBanned);
	         $userObj->setDeaths($deaths);
	         $userObj->setBugKills($bugkills);
	         $userObj->setQCreated($qcreated);
	         $userObj->setPassword($password);
	         $userObj->setAvatar($imagePath);
	         return $userObj;

	    }

	    public static function update_image($uname , $imagePath)
	    {
	        update_image($uname , $imagePath);
	    }

	    public static function update_user ($fname,$lname,$uname,$email,$bday){
	         update_user ($fname,$lname,$uname,$email,$bday);
	    }
	    public static function update_password ($uname,$newpassword){
	         update_password ($uname,$newpassword);
	    }

	     public static function update_gold ($uname,$totalGold){
	         update_gold ($uname,$totalGold);
	    }

		public static function update_expe ($uname,$exper){
	         update_expe($uname,$exper);
	    }

}