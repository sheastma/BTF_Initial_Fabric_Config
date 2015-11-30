<link rel="stylesheet" type="text/css" href="../../static/rr.css">

<body style = "background-color:#CCCCCA">
<img id="banner" style = "bg-color:CBCCCE" src="static/Cisco_emailHeader.png" alt="Banner Image"/>
<div style="width: 800px;height: 100px;position: absolute;top:0;bottom: 0;left: 0;right: 0;margin: auto;">
<h1>Route Reflectors</h1>
<form action="/IFC_config/fabric_config/rr" method="POST">
ASN: <input id = "ASN" type="text"><br>
%for spine in spines:
	Spine name: <input type="text" value={{spine["name"]}} readonly><br>
	Would you like to add Spine as Route Reflector? <input type="checkbox" id = {{spine["name"]}} value="Yes"><br>
%end
<input type="submit" value="Submit">
</div>
</body>
<script language="JavaScript" type="text/javascript" src="../../static/rr.js"></script>