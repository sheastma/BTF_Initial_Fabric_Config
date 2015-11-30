<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
  <script language="JavaScript" type="text/javascript" src="/static/IFC_main.js"></script>
  <link rel="stylesheet" type="text/css" href="/static/IFC_main.css">

</head>
<body style = "background-color:#CCCCCA">
<img id="banner" style = "bg-color:CBCCCE" src="/static/Cisco_emailHeader.png" alt="Banner Image"/>
<div style = "width: 800px;height: 300px;position: absolute;top:0;bottom: 0;left: 0;right: 0;margin: auto;" id = "mn_content" class="container">
  <h2>Health Check</h2>
  <p>This table checks all the initial policies that all fabrics should have configured</p>            
  <table class="table">
    <thead>
      <tr class="info">
        <th>Policy</th>
        <th>Configured?</th>
		<th>Configure Now</th>
      </tr>
    </thead>
    <tbody>
	%if mgmt == "True":
      <tr class="success">
        <td>MGMT Connectivity</td>
        <td id = "1">True</td>
		<td id = "1"></td>
      </tr>
	%else:
	  <tr class="danger">
        <td>MGMT Connectivity</td>
		<td>False</td>
        <td id = "1"><button id = "mgmt_config" type="button" class="btn btn-primary">Configure</button></td>
      </tr>
	%end
	%if DNS == "True":
      <tr class="success">
        <td>DNS</td>
        <td id = "2">True</td>
		<td id = "2"></td>
      </tr>
	%else:
	  <tr class="danger">
        <td>DNS</td>
		<td>False</td>
        <td id = "2"><button id = "dns_config" type="button" class="btn btn-primary">Configure</button></td>
      </tr>
	%end
	%if NTP == "True":
      <tr class="success">
        <td>NTP</td>
        <td id = "3">True</td>
		<td></td>
      </tr>
	%else:
	  <tr class="danger">
        <td>NTP</td>
		<td>False</td>
        <td id = "3"><button id = "ntp_config" type="button" class="btn btn-primary">Configure</button></td>
      </tr>
	%end
	%if RR == "True":
      <tr class="success">
        <td>Route Reflectors</td>
        <td id = "4">True</td>
		<td></td>
      </tr>
	%else:
	  <tr class="danger">
        <td>Route Reflectors</td>
		<td>False</td>
        <td id = "4"><button id = "rr_config" type="button" class="btn btn-primary">Configure</button></td>
      </tr>
	%end
	%if RL == "True":
      <tr class="success">
        <td>Remote Location</td>
        <td id = "1">True</td>
		<td></td>
      </tr>
	%else:
	  <tr class="danger">
        <td>Remote Location</td>
		<td>False</td>
        <td id = "1"><button id = "rl_config" type="button" class="btn btn-primary">Configure</button></td>
      </tr>
	%end
    </tbody>
  </table>
</div>

</body>
</html>