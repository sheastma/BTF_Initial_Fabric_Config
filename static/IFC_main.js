window.onload = function(){
mgmt = document.getElementById('mgmt_config');
dns = document.getElementById('dns_config');
ntp = document.getElementById('ntp_config');
rr = document.getElementById('rr_config');
rl = document.getElementById('rl_config');

mgmt.addEventListener("click", function() {
alert("here")
	popupWindow = window.open(
		'/IFC_config/mgmt','popUpWindow','height=300,width=400,left=10,top=10,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no,status=yes')
});
dns.addEventListener("click", function() {
alert("here")
	popupWindow = window.open(
		'/IFC_config/dns','popUpWindow','height=300,width=400,left=10,top=10,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no,status=yes')
});
ntp.addEventListener("click", function() {
alert("here")
	popupWindow = window.open(
		'/IFC_config/ntp','popUpWindow','height=300,width=400,left=10,top=10,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no,status=yes')
});
rr.addEventListener("click", function() {
alert("here")
	popupWindow = window.open(
		'/IFC_config/rr','popUpWindow','height=300,width=400,left=10,top=10,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no,status=yes')
});
rl.addEventListener("click", function() {
alert("here")
	popupWindow = window.open(
		'/IFC_config/rl','popUpWindow','height=300,width=400,left=10,top=10,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no,status=yes')
});
}
