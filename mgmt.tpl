<link rel="stylesheet" type="text/css" href="../../static/mgmt.css">

<body style = "background-color:#CCCCCA">
<img id="banner" style = "bg-color:CBCCCE" src="static/Cisco_emailHeader.png" alt="Banner Image"/>
<div style="width: 800px;height: 100px;position: absolute;top:0;bottom: 0;left: 0;right: 0;margin: auto;">
<h1>Management Connectivity</h1>
 <select id = "nodes">
%for node in nodes:
    <option value={{node["name"]}}>{{node["name"]}}</option>
%end
</select><br>
<form action="/IFC_config/fabric_config/mgmt" method="POST">
Node ID: <input style="margin-right: 50px;" type="text" id = "nodeID" name="NodeID" value={{nodes[0]["id"]}} readonly><br>
OOB mgmt address (i.e. 10.10.10.10/24): <input id = "oobaddr" type="text" name="OOB mgmt address"><br>
OOB default gateway (i.e. 10.10.10.1): <input id = "oobDG" type="text" name="OOB default gatway"><br>
<button id="mgmt_save" type="button">Save</button>
<input type="submit" value="Submit">
</div>
</body>
<script language="JavaScript" type="text/javascript" src="../../static/mgmt.js"></script>