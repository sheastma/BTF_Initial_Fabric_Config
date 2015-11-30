nodes = document.getElementById("nodes");
save = document.getElementById("mgmt_save");
nodes.addEventListener("change", function() {
	var strUser = nodes.options[nodes.selectedIndex].value;
	var xhr= new XMLHttpRequest();
	xhr.onreadystatechange = function() {
		if (xhr.readyState == 4) {
			alert(xhr.responseText);
			data = xhr.responseText.split(",");
			alert(data[2]);
			document.getElementById("nodeID").setAttribute("value",data[0]);
			document.getElementById("oobaddr").value = data[1];
			document.getElementById("oobDG").value = data[2];
		}
	}
	xhr.open("GET","/IFC_config/node_info/"+strUser,true);
	xhr.send();
});

save.addEventListener("click", function() {
	var strUser = nodes.options[nodes.selectedIndex].value;
	oobaddr = document.getElementById("oobaddr").value;
	oobDG = document.getElementById("oobDG").value;
	var xhr = new XMLHttpRequest();
	xhr.onreadystatechange = function() {
		if (xhr.readyState == 4) {
			alert("The following change to mgmt connection of the APIC and/or switches\
			will temporarily drop any ssh session you have using the previous mgmt \
            configurations");
			//data = xhr.responseText.split(",");
			//document.getElementById("nodeID").setAttribute("value",data[0]);
			//document.getElementById("oobaddr").setAttribute("value",data[1]);
			//document.getElementById("oobDG").setAttribute("value",data[2]);
		}
	}
	xhr.open("GET","/IFC_config/node_config/"+strUser+","+oobaddr+","+oobDG,true);
	xhr.send();
});
