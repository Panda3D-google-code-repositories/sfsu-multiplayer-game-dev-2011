<?php
    $q_filter_cat = $_GET['cat'];
    $q_filter_class = $_GET['class'];
    $q_filter_av = $_GET['av'];
    $q_filter_sort = $_GET['sort'];
    $q_filter_show = $_GET['show'];

    $con = mysql_connect("smurf.sfsu.edu", "BeastReality", "beastreality");
    $db = mysql_select_db("BeastRealityDB", $con);

    $query = "SELECT `species_id`, `name`, `cost`, `description`, `category`, `biomass`, `diet_type`, `metabolism`, `node_list`, `trophic_level`, `unlock`, (

                SELECT GROUP_CONCAT(`node_list`, ':',`species_name`
                ORDER BY `species_name`)
                FROM `carnivore`
                JOIN `animal_type` ON `prey_id` = `animal_type_id`
                WHERE `predator_id` = `species`.`species_id`
                ) AS `prey_list`, (

                SELECT GROUP_CONCAT(`node_list`, ':',`species_name`
                ORDER BY `species_name`)
                FROM `herbivore`
                JOIN `plant_type` ON `herbivore`.`plant_type_id` = `plant_type`.`plant_type_id`
                WHERE `herbivore`.`animal_type_id` = `species`.`species_id`
                ) AS `prey_list_p`, (

                SELECT GROUP_CONCAT(`node_list`, ':',`species_name`
                ORDER BY `species_name`)
                FROM `carnivore`
                JOIN `animal_type` ON `predator_id` = `animal_type_id`
                WHERE `prey_id` = `species`.`species_id`
                ) AS `predator_list`, (

                SELECT GROUP_CONCAT(`node_list`, ':',`species_name`
                ORDER BY `species_name`)
                FROM `herbivore`
                JOIN `animal_type` ON `herbivore`.`animal_type_id` = `animal_type`.`animal_type_id`
                WHERE `herbivore`.`plant_type_id` = `species`.`species_id`
                ) AS `predator_list_p`
           FROM ((

                SELECT `animal_type_id` AS `species_id`, `species_name` AS `name`, `cost`, `description`, `category`, `max_biomass` AS `biomass`, `diet_type`, `metabolism`, `node_list`, `trophic_level`, `unlock`
                FROM `animal_type`
                WHERE `animal_type_id`
                NOT IN (54, 58, 62, 76, 78, 79, 81, 84)
                )
                UNION (

                SELECT `plant_type_id` AS `species_id`, `species_name` AS `name`, `cost`, `description`, `category`, `max_biomass` AS `biomass`, 3 AS `diet_type`, 0 AS `metabolism`, `node_list`, `trophic_level`, `unlock`
                FROM `plant_type`
                WHERE `plant_type_id`
                NOT IN (1006)
                )) AS `species`";

    if ($q_filter_cat) {
        $query .= " WHERE";

        if ($q_filter_cat == "animal") {
            $query .= " (`category` = \"Small Animal\" OR `category` = \"Large Animal\")";
        } else if ($q_filter_cat == "animal_s") {
            $query .= " `category` = \"Small Animal\"";
        } else if ($q_filter_cat == "animal_l") {
            $query .= " `category` = \"Large Animal\"";
        } else if ($q_filter_cat == "bird") {
            $query .= " `category` = \"Bird\"";
        } else if ($q_filter_cat == "insect") {
            $query .= " `category` = \"Insect\"";
        } else if ($q_filter_cat == "plant") {
            $query .= " `category` = \"Plant\"";
        } else if ($q_filter_cat == "resource") {
            $query .= " `category` = \"Resource\"";
        }
    }

    if ($q_filter_class) {
        if ($q_filter_cat) {
            $query .= " AND";
        } else {
            $query .= " WHERE";
        }

        if ($q_filter_class == "carnivore") {
            $query .= " `diet_type` = 1";
        } else if ($q_filter_class == "herbivore") {
            $query .= " `diet_type` = 2";
        } else if ($q_filter_class == "omnivore") {
            $query .= " `diet_type` = 0";
        } else if ($q_filter_class == "producer") {
            $query .= " `diet_type` = 3";
        }
    }

    if ($q_filter_av) {
        if ($q_filter_cat || $q_filter_class) {
            $query .= " AND";
        } else {
            $query .= " WHERE";
        }

        if ($q_filter_av == "yes") {
            $query .= " `unlock` > 0";
        } else if ($q_filter_av == "no") {
            $query .= " `unlock` = 0";
        }
    }

    if ($q_filter_show) {
        if ($q_filter_cat || $q_filter_class || $q_filter_av) {
            $query .= " AND";
        } else {
            $query .= " WHERE";
        }

        $query .= " `name` LIKE '$q_filter_show%'";
    }

    $temp_type = "";
    $temp_order = "";

    if ($q_filter_sort) {
        $temp = explode('_', $q_filter_sort);
        $temp_type = $temp[0];
        $temp_order = $temp[1];

        if ($temp_type == "name") {
            $query .= " ORDER BY `name`";

            if ($temp_order == "desc") {
                $query .= " DESC";
            }
        } else {
            if ($temp_type == "node") {
                $query .= " ORDER BY ABS(`node_list`)";
            } else if ($temp_type == "species") {
                $query .= " ORDER BY `species_id`";
            } else if ($temp_type == "biomass") {
                $query .= " ORDER BY `biomass`";
            } else if ($temp_type == "price") {
                $query .= " ORDER BY `cost`";
            } else if ($temp_type == "available") {
                $query .= " ORDER BY `unlock`";
            }

            if ($temp_order == "desc") {
                $query .= " DESC";
            }

            $query .= ", `name`";
        }
    } else {
        $query .= " ORDER BY `name`";
    }

    $result = mysql_query($query);

    if ($q_filter_show) {
        echo "<h2>$q_filter_show</h2>";
    } else {
        if ($temp_type == "name" && $temp_order == "desc") {
            echo "<h2>Z-A</h2>";
        } else {
            echo "<h2>A-Z</h2>";
        }
    }

    if (mysql_num_rows($result) == 0) {
        echo "
                <div align=\"center\">
                <i>No Results</i>
                </div>
                <br />
            ";

        return;
    }

    while ($row = mysql_fetch_assoc($result)) {
        $species_id = $row['species_id'];
        $name = $row['name'];

        $cost = number_format($row['cost']);
        $description = $row['description'];
        $category = $row['category'];
        $biomass = number_format($row['biomass']);

        $diet = $row['diet_type'];
        if ($diet == 0) {
            $diet = "Omnivore";
        } else if ($diet == 1) {
            $diet = "Carnivore";
        } else if ($diet == 2) {
            $diet = "Herbivore";
        } else {
            $diet = "Producer";
        }

        $metabolism = $row['metabolism'];
        if ($metabolism == 0) {
            $metabolism = "Unknown";
        }

        $node_list = $row['node_list'];
        $trophic_level = $row['trophic_level'];

        $unlock = $row['unlock'];
        if ($unlock > 0) {
            $unlock = "Lv " . $unlock;
        } else {
            $unlock = "No";
        }

        $prey_list = "None";

        $prey_list_a = $row['prey_list'];
		$prey_list_animals = $prey_list_a;
        if ($prey_list_a) {
            $temp_list = explode(',', $prey_list_a);
            $lastElement = end($temp_list);

            $prey_list_a = "";
            foreach ($temp_list as $value) {
                $temp = explode(':', $value);
                $node_list_2 = $temp[0];
                $species_name = $temp[1];

                $prey_list_a .= "<a href=\"javascript:void(0);\" onclick=\"getSpecies('" . str_replace("'", "\'", $species_name) . "');\" title=\"Node ID(s): " . $node_list_2 . "\">" . $species_name . "</a>";

                if ($value != $lastElement) {
                    $prey_list_a .= ", ";
                }
            }
        }

        $prey_list_p = $row['prey_list_p'];
		$prey_list_plants = $prey_list_p;
        if ($prey_list_p) {
            $temp_list = explode(',', $prey_list_p);
            $lastElement = end($temp_list);

            $prey_list_p = "";
            foreach ($temp_list as $value) {
                $temp = explode(':', $value);
                $node_list_2 = $temp[0];
                $species_name = $temp[1];

                $prey_list_p .= "<a href=\"javascript:void(0);\" onclick=\"getSpecies('" . str_replace("'", "\'", $species_name) . "');\" title=\"Node ID(s): " . $node_list_2 . "\">" . $species_name . "</a>";

                if ($value != $lastElement) {
                    $prey_list_p .= ", ";
                }
            }
        }

        if ($prey_list_a) {
            $prey_list = $prey_list_a;

            if ($prey_list_p) {
                $prey_list .= "<br /><br />" . $prey_list_p;
            }
        } else if ($prey_list_p) {
            $prey_list = $prey_list_p;
        }

        $predator_list = "None";

        $predator_list_a = $row['predator_list'];
        if ($predator_list_a) {
            $temp_list = explode(',', $predator_list_a);
            $lastElement = end($temp_list);

            $predator_list_a = "";
            foreach ($temp_list as $value) {
                $temp = explode(':', $value);
                $node_list_2 = $temp[0];
                $species_name = $temp[1];

                $predator_list_a .= "<a href=\"javascript:void(0);\" onclick=\"getSpecies('" . str_replace("'", "\'", $species_name) . "');\" title=\"Node ID(s): " . $node_list_2 . "\">" . $species_name . "</a>";

                if ($value != $lastElement) {
                    $predator_list_a .= ", ";
                }
            }
        }

        $predator_list_p = $row['predator_list_p'];
        if ($predator_list_p) {
            $temp_list = explode(',', $predator_list_p);
            $lastElement = end($temp_list);

            $predator_list_p = "";
            foreach ($temp_list as $value) {
                $temp = explode(':', $value);
                $node_list_2 = $temp[0];
                $species_name = $temp[1];

                $predator_list_p .= "<a href=\"javascript:void(0);\" onclick=\"getSpecies('" . str_replace("'", "\'", $species_name) . "');\" title=\"Node ID(s): " . $node_list_2 . "\">" . $species_name . "</a>";

                if ($value != $lastElement) {
                    $predator_list_p .= ", ";
                }
            }
        }

        if ($predator_list_a) {
            $predator_list = $predator_list_a;

            if ($predator_list_p) {
                $predator_list .= "<br /><br />" . $predator_list_p;
            }
        } else if ($predator_list_p) {
            $predator_list = $predator_list_p;
        }

        if (strpos($node_list, ',')) {
            $temp_list = explode(',', $node_list);
            $lastElement = end($temp_list);

            $total = 0;

            $node_list = "";
            foreach ($temp_list as $value) {
                $temp = explode(':', $value);
                $node_id = $temp[0];
                $amount = $temp[1];

                $node_list .= $node_id;
                if ($value != $lastElement) {
                    $node_list .= ", ";
                }

                $total += intval($amount);
            }

            $description .= "<br /><br />";
            $predator_list = "* Predators of ";

            foreach ($temp_list as $value) {
                $temp = explode(':', $value);
                $node_id = $temp[0];
                $amount = $temp[1];

                $name_ = "Unknown";
                switch (intval($node_id)) {
                    case 2:
                        $name_ = "Plant Juices";
                        break;
                    case 3:
                        $name_ = "Fruits and Nectar";
                        break;
                    case 4:
                        $name_ = "Grains and Seeds";
                        break;
                    case 7:
                        $name_ = "Trees and Shrubs";
                        break;
                }
                $description .= str_pad(round(intval($amount) / $total * 100), 2, '0', STR_PAD_LEFT) . "% <a href=\"javascript:void(0);\" onclick=\"getSpecies('" . str_replace("'", "\'", $name_) . "');\" title=\"Node ID(s):$node_id\">" . $name_ . "</a>";
                $predator_list .= "<a href=\"javascript:void(0);\" onclick=\"getSpecies('" . str_replace("'", "\'", $name_) . "');\" title=\"Node ID(s):$node_id\">" . $name_ . "</a>";

                if ($value != $lastElement) {
                    $description .= "<br />";
                    $predator_list .= ", ";
                }
            }

            $predator_list = "<i>$predator_list</i>";
        }

        if ($category == "Plant") {
            $img_src = "images/plant/$name.jpg";
        } else {
            $img_src = "images/animal/$name.jpg";
        }

       echo "
            <div class=\"top\"><a href=\"#\">Top</a></div>
            <div id=\"$name\" class=\"profile\">
					
            <table cellspacing=\"0\">
                <tr>
                    <th class=\"name\" colspan=\"4\"><a href=\"javascript:void(0);\" onclick=\"getSpecies('" . str_replace("'", "\'", $name) . "');\">$name</a></th>
                </tr>
                <tr>
                    <td class=\"species_img\" rowspan=\"3\"><img src=\"$img_src\" alt=\"\" class=\"screen_shot\"/></td>
                    <td class=\"stat\"><b>Species ID</b> - $species_id</td>
                    <td class=\"stat\"><b>Node ID(s)</b> - $node_list</td>
                    <td class=\"stat\"><b>Price</b> - $cost G</td>
                </tr>
                <tr>
                    <td class=\"stat\"><b>Class</b> - $diet</td>
                    <td class=\"stat\"><b>Category</b> - $category</td>
                    <td class=\"stat\"><b>Available</b> - $unlock</td>
                </tr>
                <tr>
                    <td class=\"stat\"><b>Biomass</b> - $biomass</td>
                    <td class=\"stat\"><b>Metabolism</b> - $metabolism</td>
                    <td class=\"stat\"><b>Trophic Level</b> - $trophic_level</td>
                </tr>
                <tr>
                    <td class=\"description\" colspan=\"4\"><b>Description</b><br />$description</td>
                </tr>
                <tr>
                    <td class=\"prey\" colspan=\"4\"><b>Prey(s)</b><br />$prey_list</td>
                </tr>
                <tr>
                    <td class=\"predator\" colspan=\"4\"><b>Predator(s)</b><br />$predator_list</td>
                </tr>
                <tr>
                    <td class=\"edit\" colspan=\"4\">
					<form method=\"post\" action=\"species_params.php\">
						<input type=\"hidden\" name=\"name\" value=\"$name\" />
						<input type=\"hidden\" name=\"species_id\" value=\"$species_id\" />
						<input type=\"hidden\" name=\"img_src\" value=\"$img_src\" />
						<input type=\"hidden\" name=\"diet\" value=\"$diet\" />

						<input type=\"hidden\" name=\"biomass\" value=\"$biomass\" />
						<input type=\"hidden\" name=\"rec_biomass\" value=\"$biomass\" />

						<input type=\"hidden\" name=\"metabolism\" value=\"$metabolism\" />
						<input type=\"hidden\" name=\"rec_metabolism\" value=\"$rec_metabolism\" />

						<input type=\"hidden\" name=\"prey_list_animals\" value=\"$prey_list_animals\" />
						<input type=\"hidden\" name=\"prey_list_plants\" value=\"$prey_list_plants\" />

						<input type=\"submit\" class=\"edit_button\"  value=\"EDIT\" /><br />
					</form>
					</td>
                 </tr>
            </table>
				
            </div>
            <br />
        ";
    }
?>
