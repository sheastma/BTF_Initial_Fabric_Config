<link rel="stylesheet" type="text/css" href="../../static/ntp.css">

<body style = "background-color:#CCCCCA">
<img id="banner" style = "bg-color:CBCCCE" src="static/Cisco_emailHeader.png" alt="Banner Image"/>
<div style="width: 800px;height: 100px;position: absolute;top:0;bottom: 0;left: 0;right: 0;margin: auto;">
<h1>NTP</h1>
<form action="/IFC_config/fabric_config/ntp" method="POST">
NTP address or name: <input id = "ntp_addr" type="text" name="ntp_addr"><br>
<button id="dns_save" type="button">Save</button>
<input type="submit" value="Submit">
</div>
</body>
<script language="JavaScript" type="text/javascript" src="../../static/ntp.js"></script>