<link rel="stylesheet" type="text/css" href="../../static/rl.css">

<body style = "background-color:#CCCCCA">
<img id="banner" style = "bg-color:CBCCCE" src="static/Cisco_emailHeader.png" alt="Banner Image"/>
<div style="width: 800px;height: 100px;position: absolute;top:0;bottom: 0;left: 0;right: 0;margin: auto;">
<h1>Remote Location</h1>
<form action="/IFC_config/fabric_config/rl" method="POST">
Host Name(or IP address): <input id = "rl_addr" type="text" name="rl_addr"><br>
<select id = "rl_proto" name = "rl_proto" >
    <option value= "SCP">SCP</option>
	<option value= "FTP">FTP</option>
	<option value= "TFTP">TFTP</option>
</select><br>
Remote Path: <input id = "remote_path" name = "remote_path" type="text"><br>
Remote Port: <input id = "remote_port" name = "remote_port" type="text"><br>
Username: <input id = "rl_user" name = "rl_user" type="text"><br>
Password: <input id = "rl_pwd" name = "rl_pwd" type="password"><br>
<input type="submit" value="Submit">
</div>
</body>
<script language="JavaScript" type="text/javascript" src="../../static/rl.js"></script>