function createRequest(id, url) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            $('#' + id).fadeTo("normal", 0, function() {
                document.getElementById(id).innerHTML = xmlhttp.responseText;
            });

            $('#' + id).fadeTo("slow", 1, function() {

            });
        }
    }

    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}