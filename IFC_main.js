document.onload = function(){
fab = document.getElementById('DNS_config');

fab.addEventListener("click", function() {
alert("here")
	popupWindow = window.open(
		'/IFC_config/test','popUpWindow','height=300,width=400,left=10,top=10,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no,status=yes')
});
}