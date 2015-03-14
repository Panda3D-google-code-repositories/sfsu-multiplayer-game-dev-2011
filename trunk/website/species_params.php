<?php include "layout/header.php"; ?>
<?php include "layout/navleft3.php"; ?>
<style type="text/css">
.profile table {
	background-color: #FAEBD7;
	border-style: none solid solid none;
	width: 100%;
}

.profile table,td,th {
	border-color: #d5c8a4;
	border-width: 3px;
}

.profile td,th {
	border-style: solid none none solid;
	padding: 5px;
}

.stat {
	height: 25px;
	width: 200px;
}
</style>
<div class="content_container">
	<h1>Functional Parameters of species</h1>

	<?php
	 $biomass = $_POST['biomass'];
	 $rec_biomass = $_POST['rec_biomass'];

 	 $metabolism = $_POST['metabolism'];
	 $rec_metabolism = $_POST['rec_metabolism'];

	 $name = $_POST['name'];
	 $species_id = $_POST['species_id'];
	 $img_src = $_POST['img_src'];
	 $diet = $_POST['diet'];
	 $prey_list_animals = $_POST['prey_list_animals'];
	 $prey_list_plants = $_POST['prey_list_plants'];

	 //print $prey_list_animals;
	 //print $prey_list_plants;

     $con = mysql_connect("localhost:3306", "root", "newpwd");
     $db = mysql_select_db("BeastRealityDB", $con);
	 if (!$db) die('Could not connect' . mysql_error());

     $param_e_query = "SELECT prey_id, percent_manipulated FROM `predator_prey_ratio` WHERE parameter_type=4 AND predator_id = $species_id AND player_id = 1";
	 $param_d_query = "SELECT prey_id, percent_manipulated FROM `predator_prey_ratio` WHERE parameter_type=5 AND predator_id = $species_id AND player_id = 1";
	 $param_q_query = "SELECT prey_id, percent_manipulated FROM `predator_prey_ratio` WHERE parameter_type=6 AND predator_id = $species_id AND player_id = 1";
	 $param_a_query = "SELECT prey_id, percent_manipulated FROM `predator_prey_ratio` WHERE parameter_type=7 AND predator_id = $species_id AND player_id = 1";
	
//////////////////////
	 $no_of_rows_param_e = 0;
	 $params_e = array();
	 //print $param_e_query;
     $results_param_e_query = mysql_query($param_e_query);
     if (mysql_num_rows($results_param_e_query) == 0) {
        if ($prey_list_animals) {
            $temp_list = explode(',', $prey_list_animals);

            foreach ($temp_list as $value) {
                $temp = explode(':', $value);
                $node_list_2 = $temp[0];
                $species_name = $temp[1];
				
				//print $node_list_2;
				$query = "INSERT INTO `predator_prey_ratio` (`player_id`, `zone_id`, `parameter_type`, `predator_id`,`prey_id`, `percent_manipulated`) VALUES (1, 0, 4, $species_id, $node_list_2, 100.0)"; 
				//print $query;
				mysql_query($query);
				$no_of_rows_param_e++;
				$prey_id = $node_list_2;
				$param_e = 100.0;
				//print $prey_id." ".$param_e;
				array_push($params_e, array("prey_id" => $species_name, "percent"=>$param_e));
			}
		}
        if ($prey_list_plants) {
            $temp_list = explode(',', $prey_list_plants);

            foreach ($temp_list as $value) {
                $temp = explode(':', $value);
                $node_list_2 = $temp[0];
                $species_name = $temp[1];
				
				//print $node_list_2;
				$query = "INSERT INTO `predator_prey_ratio` (`player_id`, `zone_id`, `parameter_type`, `predator_id`,`prey_id`, `percent_manipulated`) VALUES (1, 0, 4, $species_id, $node_list_2, 100.0)"; 
				//print $query;
				mysql_query($query);
				$no_of_rows_param_e++;
				$prey_id = $node_list_2;
				$param_e = 100.0;
				//print $prey_id." ".$param_e;
				array_push($params_e, array("prey_id" => $species_name, "percent"=>$param_e));
			}
		}
	 }else{
     	while ($row = mysql_fetch_assoc($results_param_e_query)) {
			$prey_id = $row['prey_id'];
        	$percent = $row['percent_manipulated'];
			//print $prey_id." ".$percent;
			$no_of_rows_param_e++;
			$param_e = $percent;
			//print $prey_id." ".$param_e;
			$query = "Select species_name from animal_type where node_list = $prey_id";
			$results = mysql_query($query);
			if (mysql_num_rows($results) == 0) {
				$query = "Select species_name from plant_type where node_list = $prey_id";
				$results = mysql_query($query);

				$plant_name = mysql_fetch_assoc($results);

				$species_name = $plant_name['species_name'];
				array_push($params_e, array("prey_id" => $species_name, "percent"=>$param_e));
			}else{
				$animal_name = mysql_fetch_assoc($results);

				$species_name = $animal_name['species_name'];
				array_push($params_e, array("prey_id" => $species_name, "percent"=>$param_e));
			}
		 }
	 }
//////////////////////
//////////////////////
	 $no_of_rows_param_d = 0;
	 $params_d = array();
	 //print $param_d_query;
     $results_param_d_query = mysql_query($param_d_query);
     if (mysql_num_rows($results_param_d_query) == 0) {
        if ($prey_list_animals) {
            $temp_list = explode(',', $prey_list_animals);

            foreach ($temp_list as $value) {
                $temp = explode(':', $value);
                $node_list_2 = $temp[0];
                $species_name = $temp[1];
				
				//print $node_list_2;
				$query = "INSERT INTO `predator_prey_ratio` (`player_id`, `zone_id`, `parameter_type`, `predator_id`,`prey_id`, `percent_manipulated`) VALUES (1, 0, 5, $species_id, $node_list_2, 100.0)"; 
				//print $query;
				mysql_query($query);
				$no_of_rows_param_d++;
				$prey_id = $node_list_2;
				$param_d = 100.0;
				//print $prey_id." ".$param_d;
				array_push($params_d, array("prey_id" => $species_name, "percent"=>$param_d));
			}
		}
        if ($prey_list_plants) {
            $temp_list = explode(',', $prey_list_plants);

            foreach ($temp_list as $value) {
                $temp = explode(':', $value);
                $node_list_2 = $temp[0];
                $species_name = $temp[1];
				
				//print $node_list_2;
				$query = "INSERT INTO `predator_prey_ratio` (`player_id`, `zone_id`, `parameter_type`, `predator_id`,`prey_id`, `percent_manipulated`) VALUES (1, 0, 5, $species_id, $node_list_2, 100.0)"; 
				//print $query;
				mysql_query($query);
				$no_of_rows_param_d++;
				$prey_id = $node_list_2;
				$param_d = 100.0;
				//print $prey_id." ".$param_d;
				array_push($params_d, array("prey_id" => $species_name, "percent"=>$param_d));
			}
		}
	 }else{
     	while ($row = mysql_fetch_assoc($results_param_d_query)) {
			$prey_id = $row['prey_id'];
        	$percent = $row['percent_manipulated'];
			//print $prey_id." ".$percent;
			$no_of_rows_param_d++;
			$param_d = $percent;
			//print $prey_id." ".$param_d;
			$query = "Select species_name from animal_type where node_list = $prey_id";
			$results = mysql_query($query);
			if (mysql_num_rows($results) == 0) {
				$query = "Select species_name from plant_type where node_list = $prey_id";
				$results = mysql_query($query);

				$plant_name = mysql_fetch_assoc($results);

				$species_name = $plant_name['species_name'];
				array_push($params_d, array("prey_id" => $species_name, "percent"=>$param_d));
			}else{
				$animal_name = mysql_fetch_assoc($results);

				$species_name = $animal_name['species_name'];
				array_push($params_d, array("prey_id" => $species_name, "percent"=>$param_d));
			}
		 }
	 }
//////////////////////
//////////////////////
	 $no_of_rows_param_q = 0;
	 $params_q = array();
	 //print $param_q_query;
     $results_param_q_query = mysql_query($param_q_query);
     if (mysql_num_rows($results_param_q_query) == 0) {
        if ($prey_list_animals) {
            $temp_list = explode(',', $prey_list_animals);

            foreach ($temp_list as $value) {
                $temp = explode(':', $value);
                $node_list_2 = $temp[0];
                $species_name = $temp[1];
				
				//print $node_list_2;
				$query = "INSERT INTO `predator_prey_ratio` (`player_id`, `zone_id`, `parameter_type`, `predator_id`,`prey_id`, `percent_manipulated`) VALUES (1, 0, 6, $species_id, $node_list_2, 100.0)"; 
				//print $query;
				mysql_query($query);
				$no_of_rows_param_q++;
				$prey_id = $node_list_2;
				$param_q = 100.0;
				//print $prey_id." ".$param_q;
				array_push($params_q, array("prey_id" => $species_name, "percent"=>$param_q));
			}
		}
        if ($prey_list_plants) {
            $temp_list = explode(',', $prey_list_plants);

            foreach ($temp_list as $value) {
                $temp = explode(':', $value);
                $node_list_2 = $temp[0];
                $species_name = $temp[1];
				
				//print $node_list_2;
				$query = "INSERT INTO `predator_prey_ratio` (`player_id`, `zone_id`, `parameter_type`, `predator_id`,`prey_id`, `percent_manipulated`) VALUES (1, 0, 6, $species_id, $node_list_2, 100.0)"; 
				//print $query;
				mysql_query($query);
				$no_of_rows_param_q++;
				$prey_id = $node_list_2;
				$param_q = 100.0;
				//print $prey_id." ".$param_q;
				array_push($params_q, array("prey_id" => $species_name, "percent"=>$param_q));
			}
		}
	 }else{
     	while ($row = mysql_fetch_assoc($results_param_q_query)) {
			$prey_id = $row['prey_id'];
        	$percent = $row['percent_manipulated'];
			//print $prey_id." ".$percent;
			$no_of_rows_param_q++;
			$param_q = $percent;
			//print $prey_id." ".$param_q;
			$query = "Select species_name from animal_type where node_list = $prey_id";
			$results = mysql_query($query);
			if (mysql_num_rows($results) == 0) {
				$query = "Select species_name from plant_type where node_list = $prey_id";
				$results = mysql_query($query);

				$plant_name = mysql_fetch_assoc($results);

				$species_name = $plant_name['species_name'];
				array_push($params_q, array("prey_id" => $species_name, "percent"=>$param_q));
			}else{
				$animal_name = mysql_fetch_assoc($results);

				$species_name = $animal_name['species_name'];
				array_push($params_q, array("prey_id" => $species_name, "percent"=>$param_q));
			}
		 }
	 }
//////////////////////
//////////////////////
	 $no_of_rows_param_a = 0;
	 $params_a = array();
	 //print $param_a_query;
     $results_param_a_query = mysql_query($param_a_query);
     if (mysql_num_rows($results_param_a_query) == 0) {
        if ($prey_list_animals) {
            $temp_list = explode(',', $prey_list_animals);

            foreach ($temp_list as $value) {
                $temp = explode(':', $value);
                $node_list_2 = $temp[0];
                $species_name = $temp[1];
				
				//print $node_list_2;
				$query = "INSERT INTO `predator_prey_ratio` (`player_id`, `zone_id`, `parameter_type`, `predator_id`,`prey_id`, `percent_manipulated`) VALUES (1, 0, 7, $species_id, $node_list_2, 100.0)"; 
				//print $query;
				mysql_query($query);
				$no_of_rows_param_a++;
				$prey_id = $node_list_2;
				$param_a = 100.0;
				//print $prey_id." ".$param_a;
				array_push($params_a, array("prey_id" => $species_name, "percent"=>$param_a));
			}
		}
        if ($prey_list_plants) {
            $temp_list = explode(',', $prey_list_plants);

            foreach ($temp_list as $value) {
                $temp = explode(':', $value);
                $node_list_2 = $temp[0];
                $species_name = $temp[1];
				
				//print $node_list_2;
				$query = "INSERT INTO `predator_prey_ratio` (`player_id`, `zone_id`, `parameter_type`, `predator_id`,`prey_id`, `percent_manipulated`) VALUES (1, 0, 7, $species_id, $node_list_2, 100.0)"; 
				//print $query;
				mysql_query($query);
				$no_of_rows_param_a++;
				$prey_id = $node_list_2;
				$param_a = 100.0;
				//print $prey_id." ".$param_a;
				array_push($params_a, array("prey_id" => $species_name, "percent"=>$param_a));
			}
		}
	 }else{
     	while ($row = mysql_fetch_assoc($results_param_a_query)) {
			$prey_id = $row['prey_id'];
        	$percent = $row['percent_manipulated'];
			//print $prey_id." ".$percent;
			$no_of_rows_param_a++;
			$param_a = $percent;
			//print $prey_id." ".$param_a;
			$query = "Select species_name from animal_type where node_list = $prey_id";
			$results = mysql_query($query);
			if (mysql_num_rows($results) == 0) {
				$query = "Select species_name from plant_type where node_list = $prey_id";
				$results = mysql_query($query);

				$plant_name = mysql_fetch_assoc($results);

				$species_name = $plant_name['species_name'];
				array_push($params_a, array("prey_id" => $species_name, "percent"=>$param_a));
			}else{
				$animal_name = mysql_fetch_assoc($results);

				$species_name = $animal_name['species_name'];
				array_push($params_a, array("prey_id" => $species_name, "percent"=>$param_a));
			}
		 }
	 }
//////////////////////
    // Parameter Type
    //public static final short PARAMETER_K = 0;	//Plants Carrying capacity >0
    //public static final short PARAMETER_R = 1;	//Plants Growth rate 0-1
    //public static final short PARAMETER_X = 2;	//Plants Metabolic rate 0-1
    //public static final short PARAMETER_X_A = 3;	//Animals
    //public static final short PARAMETER_E = 4; //Animals assimilationEfficiency
    //public static final short PARAMETER_D = 5; //Animals predatorInterference
    //public static final short PARAMETER_Q = 6; //Animals functionalResponseControl
    //public static final short PARAMETER_A = 7; //Animals relativeHalfSaturationDensity

     echo "
		<div class=\"profile\">
             <table cellspacing=\"0\">
                <tr>
					<th class=\"stat\">Parameter</th>
 					<th class=\"stat\">Prey</th>
                    <th class=\"stat\">Value</th>
                    <th class=\"stat\">Recommended Value</th>
					<th class=\"stat\">Resources</th>
                </tr>
                <tr>
					<td class=\"stat\"><input type=\"radio\" name=\"param\" value=\"Biomass\" />Biomass</td>
					<td class=\"stat\" align=\"center\">-</td>
                    <td class=\"stat\">$biomass</td>
                    <td class=\"stat\">$rec_biomass</td>
					<td class=\"stat\"></td>
                </tr>
                <tr>
					<td class=\"stat\"><input type=\"radio\" name=\"param\" value=\"metabolic_rate\" />Metabolic Rate</td>
					<td class=\"stat\" align=\"center\">-</td>
                    <td class=\"stat\">$metabolism</td>
                    <td class=\"stat\">$rec_metabolism</td>
					<td class=\"stat\"></td>
                </tr>
		";
     
	 //print 	$no_of_rows_param_e;      
	 for($i = 0; $i< $no_of_rows_param_e ; $i++){  
		$prey_id =  $params_e[$i]['prey_id']; 
		$percent = $params_e[$i]['percent'];
		if($i ==0 ){  
			echo "			
				<tr>
					<td class=\"stat\"><input type=\"radio\" name=\"param\" value=\"param_e\"/>Assimilation efficiency</td>
					<td class=\"stat\" align=\"center\">$prey_id</td>
                    <td class=\"stat\">$percent</td>
                    <td class=\"stat\">$rec_param_e</td>
					<td class=\"stat\"></td>
                </tr>
			";
		}else{
			echo "			
				<tr>
					<td class=\"stat\" ></td>
					<td class=\"stat\" align=\"center\">$prey_id</td>
                    <td class=\"stat\">$percent</td>
                    <td class=\"stat\">$rec_param_e</td>
					<td class=\"stat\"></td>
                </tr>
			";
		}
	}

	 //print 	$no_of_rows_param_d;      
	 for($i = 0; $i< $no_of_rows_param_d ; $i++){  
		$prey_id =  $params_d[$i]['prey_id']; 
		$percent = $params_d[$i]['percent'];
		if($i ==0 ){  
			echo "			
				<tr>
					<td class=\"stat\"><input type=\"radio\" name=\"param\" value=\"param_d\"/>Predator Interference</td>
					<td class=\"stat\" align=\"center\">$prey_id</td>
                    <td class=\"stat\">$percent</td>
                    <td class=\"stat\">$rec_param_d</td>
					<td class=\"stat\"></td>
                </tr>
			";
		}else{
			echo "			
				<tr>
					<td class=\"stat\" ></td>
					<td class=\"stat\" align=\"center\">$prey_id</td>
                    <td class=\"stat\">$percent</td>
                    <td class=\"stat\">$rec_param_d</td>
					<td class=\"stat\"></td>
                </tr>
			";
		}
	}

	 //print 	$no_of_rows_param_q;      
	 for($i = 0; $i< $no_of_rows_param_q ; $i++){  
		$prey_id =  $params_q[$i]['prey_id']; 
		$percent = $params_q[$i]['percent'];
		if($i ==0 ){  
			echo "			
				<tr>
					<td class=\"stat\"><input type=\"radio\" name=\"param\" value=\"param_q\"/>Functional Response Control</td>
					<td class=\"stat\" align=\"center\">$prey_id</td>
                    <td class=\"stat\">$percent</td>
                    <td class=\"stat\">$rec_param_q</td>
					<td class=\"stat\"></td>
                </tr>
			";
		}else{
			echo "			
				<tr>
					<td class=\"stat\" ></td>
					<td class=\"stat\" align=\"center\">$prey_id</td>
                    <td class=\"stat\">$percent</td>
                    <td class=\"stat\">$rec_param_q</td>
					<td class=\"stat\"></td>
                </tr>
			";
		}
	}

	 //print 	$no_of_rows_param_a;      
	 for($i = 0; $i< $no_of_rows_param_a ; $i++){  
		$prey_id =  $params_a[$i]['prey_id']; 
		$percent = $params_a[$i]['percent'];
		if($i ==0 ){  
			echo "			
				<tr>
					<td class=\"stat\"><input type=\"radio\" name=\"param\" value=\"param_a\"/>Relative Half Saturation Density</td>
					<td class=\"stat\" align=\"center\">$prey_id</td>
                    <td class=\"stat\">$percent</td>
                    <td class=\"stat\">$rec_param_a</td>
					<td class=\"stat\"></td>
                </tr>
			";
		}else{
			echo "			
				<tr>
					<td class=\"stat\" ></td>
					<td class=\"stat\" align=\"center\">$prey_id</td>
                    <td class=\"stat\">$percent</td>
                    <td class=\"stat\">$rec_param_a</td>
					<td class=\"stat\"></td>
                </tr>
			";
		}
	}
	echo "          
		</table>
		</div>
		</br></br>
      ";


	 ?>
	<br />
</div>
<?php include "layout/footer2.php"; ?>