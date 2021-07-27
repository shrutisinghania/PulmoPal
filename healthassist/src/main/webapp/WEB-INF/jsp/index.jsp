<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"
	xmlns:th="http://www.thymleaf.org">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>PulmoPal | The Voyagers</title>

<!-- Latest compiled JavaScript -->
<script
	src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

<script
	src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

<!-- <script src="https://cdnjs.cloudflare.com/ajax/libs/jexcel/1.5.0/js/jquery.jexcel.min.js"></script> -->
<!-- <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jsgrid/1.5.3/jsgrid.min.js"></script> -->
<!-- <script src="/meta/js/custom/index.js" type="text/javascript"></script> -->
<script src="/meta/js/custom/trial.js" type="text/javascript"></script>
<!-- <script src="https://cdnjs.com/libraries/Chart.js"></script> -->
<!-- <script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script> -->


<link rel="stylesheet"
	href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"></link>
<link rel="stylesheet" href="/meta/css/custom/style.css"></link>
<link rel="stylesheet" href="/meta/css/dist/Chart.min.css"></link>
<!-- <link type="text/css" rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jsgrid/1.5.3/jsgrid.min.css" />
<link type="text/css" rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jsgrid/1.5.3/jsgrid-theme.min.css" /> -->
<!-- <link rel="stylesheet"
	href="https://cdnjs.cloudflare.com/ajax/libs/jexcel/1.5.0/css/jquery.jexcel.min.css"
	type="text/css" /> -->

</head>
<body>
	<!-- <div id="header"
		class="navbar navbar-default navbar-fixed-top toolHeader">
		<div class="navbar-header"></div>
		<span class="toolTitle">Health Assist (Placeholder)</span>
	</div> -->

	<div id="overlay">
		<!-- <img src="images/spinner.gif"> -->
		<img src="images/WeepyBreakableCaiman-small.gif">
	</div>
	<div id="headerBanner">
		<img src="images/header.jpg">
		<div id="headerImg" align="center">PULMOPAL</div>
	</div>
	<div id="mainDiv" class="container-fluid">

		<div class="container-fluid" id="content">

			<br>
			<div class="row" align="center" style="top: 57%; position: fixed">
				<div id="cxrAnalysis" class="col-sm-4" onclick="onCxrSelect()">
					<img src="images/cxr.jpg" data-toggle="modal"
						data-target="#imageModal" class="img-thumbnail"
						style="height: 75%; width: 75%;"><br /> <span
						class="landingFont">CXR Analysis </span>
				</div>
				<div id="statsDiv" class="col-sm-4">
					<img src="images/stats.jpg" data-toggle="modal"
						data-target="#statsModal" class="img-thumbnail"
						style="height: 75%; width: 75%;"><br /> <span
						class="landingFont">Pulmo Stats </span>
				</div>
				<div id="infoDeskDivBtn" class="col-sm-4">
					<img src="images/educate-yourself.jpg" class="img-thumbnail"
						style="height: 75%; width: 75%;"><br /> <span
						class="landingFont">InfoDesk </span>
				</div>
			</div>

		</div>

	</div>

	<div id="imageModal" class="modal fade" role="dialog"
		data-backdrop="static">
		<div id="imageModalDialog" class="modal-dialog">
			<div class="modal-content" id="imageModalContent">
				<div class="modal-header" align="center">
					<button type="button" class="close" data-dismiss="modal">&times;</button>
					<h3 id="imageHeader" class="modal-title pull-center">CXR
						Analysis</h3>
				</div>
				<div id="imageModalBody" class="modal-body" style="height: 400px">
					<div class="row" align="center">
						<button id="selectFileBtn" class="btn btn-md btn-primary col-sm-1"
							disabled>Select File</button>
						<button id="removeFile" title="No file is selected"
							style="display: none;" class="btn btn-md btn-danger col-sm-2">
							<i class="glyphicon glyphicon-remove-circle"></i>Remove Selected
							File
						</button>

						<button id="proceedBtn" class="btn btn-md btn-success col-sm-1"
							disabled title="Select an image file to proceed">
							Proceed <i class="glyphicon glyphicon-forward"></i>
						</button>

						<button id="heatMapBtn" class="btn btn-md btn-warning col-sm-1"
							title="Click to see heat map" style="display: none;">
							Show Heat Map <i class="glyphicon glyphicon-forward"></i>
						</button>

						<button id="openMailModalBtn" class="btn btn-md btn-info col-sm-1"
							title="Click to see heat map" style="display: none;"
							data-toggle="modal" data-target="#emailModal">
							Send an email <i class="glyphicon glyphicon-envelope"></i>
						</button>

						<h4>
							<label id="userConsentLabel" class="label pull-right"></label>
						</h4>

					</div>

					<br>
					<div id="userConsentDiv" class="row" align="center">
						<h3>
							<label class="label label-md label-info">Do you agree to
								provide details for statistical data analysis?</label>
						</h3>
						<br> <input type="radio" id="agree" name="agree"
							value="Agree"> <label id="agreeLabel" for="agree">Agree</label>&nbsp;&nbsp;
						<input type="radio" id="disagree" name="disagree" value="Disagree">
						<label id="disagreeLabel" for="disagree">Disagree</label>

					</div>
					<br>
					<h2 id="analysisResultDiv" class="row" align="center"></h2>
					<div class="row" align="center">
						<div id="userDataDiv" style="display: none">
							<input id="hdnSelectFileBtn" type="file" name="file"
								style="display: none" /> First Name <input id="firstNameText"
								placeholder="Enter First Name"><br /> Last Name <input
								id="lastNameText" placeholder="Enter Last Name"><br />
							Age (in Years)&nbsp;<input id="age" type="number"
								placeholder="Enter Age"><br /> Gender <input
								type="radio" id="male" name="gender" value="Male"> <label
								for="male">Male</label> <input type="radio" id="female"
								name="gender" value="Female"> <label for="female">Female</label>
							<input type="radio" id="other" name="gender" value="Other">
							<label for="other">Other</label><br> State <select
								id="stateSelect" name="state">
								<option value="" disabled selected="selected">Select
									State</option>
								<option value="Andaman and Nicobar Islands">Andaman and
									Nicobar Islands</option>
								<option value="Andhra Pradesh">Andhra Pradesh</option>
								<option value="Arunachal Pradesh">Arunachal Pradesh</option>
								<option value="Assam">Assam</option>
								<option value="Bihar">Bihar</option>
								<option value="Chandigarh">Chandigarh</option>
								<option value="Chhattisgarh">Chhattisgarh</option>
								<option value="Delhi">Delhi</option>
								<option value="Goa">Goa</option>
								<option value="Gujarat">Gujarat</option>
								<option value="Haryana">Haryana</option>
								<option value="Himachal Pradesh">Himachal Pradesh</option>
								<option value="Jammu and Kashmir">Jammu and Kashmir</option>
								<option value="Jharkhand">Jharkhand</option>
								<option value="Karnataka">Karnataka</option>
								<option value="Kerala">Kerala</option>
								<option value="Ladakh">Ladakh</option>
								<option value="Lakshadweep">Lakshadweep</option>
								<option value="Madhya Pradesh">Madhya Pradesh</option>
								<option value="Maharashtra">Maharashtra</option>
								<option value="Manipur">Manipur</option>
								<option value="Meghalaya">Meghalaya</option>
								<option value="Mizoram">Mizoram</option>
								<option value="Nagaland">Nagaland</option>
								<option value="Odisha">Odisha</option>
								<option value="Puducherry">Puducherry</option>
								<option value="Punjab">Punjab</option>
								<option value="Rajasthan">Rajasthan</option>
								<option value="Sikkim">Sikkim</option>
								<option value="Tamil Nadu">Tamil Nadu</option>
								<option value="Telangana">Telangana</option>
								<option value="Tripura">Tripura</option>
								<option value="Uttar Pradesh">Uttar Pradesh</option>
								<option value="Uttarakhand">Uttarakhand</option>
								<option value="West Bengal">West Bengal</option>
							</select><br>
							<button id="submitUserDataBtn" class="btn btn-success">Send
								User Data</button>
						</div>
					</div>

					<br />
					<div class="row" align="center">
						<div id="infoDiv"></div>
					</div>
					<br />
					<div class="row" align="center">
						<div id="heatMapContainer"></div>
					</div>

				</div>
			</div>

		</div>
	</div>


	<div id="errModal" class="modal fade" role="dialog"
		data-backdrop="static">
		<div class="modal-dialog" id="errModalDialog">
			<div class="modal-content" id="errModalContent">
				<div class="modal-header" align="center">
					<button type="button" class="close" data-dismiss="modal">&times;</button>
					<h2 class="modal-title">
						<i class="glyphicon glyphicon-warning-sign"></i> Error!
					</h2>
				</div>
				<div class="modal-body">
					<h3>
						<span class="label label-md label-danger" id="errorHeader"></span>
					</h3>
					<label id="errorText"></label>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
				</div>
			</div>

		</div>
	</div>

	<div id="emailModal" class="modal fade" role="dialog"
		data-backdrop="static">
		<div class="modal-dialog">
			<!-- Modal content-->
			<div class="modal-content">
				<div class="modal-header" align="center">
					<button type="button" class="close" data-dismiss="modal">&times;</button>
					<h4 class="modal-title">Send Email</h4>
				</div>
				<div class="modal-body">
					<h5>
						<label class="label label-md label-info">Recipient's Name?
						</label>
					</h5>
					<input type="email" id="name">
					<h5>
						<label class="label label-md label-info">Recipient E-mail
							ID? </label>
					</h5>
					<input type="email" id="emailAddress">
					<h5>
						<label class="label label-md label-info">Recipient is self
							or doctor? </label>
					</h5>
					<input type="radio" name="recipient" id="doctor" value="Doctor">Doctor
					<input type="radio" name="recipient" id="self" value="Self">Self
					<br> <br>
					<button id="sendEmailBtn" class="btn btn-md btn-success">
						Send <i class="glyphicon glyphicon-send"></i>
					</button>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
				</div>
			</div>

		</div>
	</div>

	<div id="statsModal" class="modal fade" role="dialog"
		data-backdrop="static">
		<div class="modal-dialog" id="statsModalContent">
			<div class="modal-content">
				<div class="modal-header" align="center">
					<button type="button" class="close" data-dismiss="modal">&times;</button>
					<h3 class="modal-title">Stats</h3>
				</div>
				<div class="modal-body">
					<div class="container">
						<button type="button" class="btn btn-info chartButton"
							onclick="showChart(this)" id="femaleDistributionBtn">Female
							Distribution</button>
						<button type="button" class="btn btn-info chartButton"
							onclick="showChart(this)" id="maleDistributionBtn">Male
							Distribution</button>
						<button type="button" class="btn btn-info chartButton"
							onclick="showChart(this)" id="covidCasesDistributionBtn">Covid
							Cases Distribution (India)</button>
						<button type="button" class="btn btn-info chartButton"
							onclick="showChart(this)" id="pneumoniaCasesDistributionBtn">Pneumonia
							Cases Distribution (India)</button>
						<button type="button" class="btn btn-info chartButton"
							onclick="showChart(this)" id="covidCasesDistributionAgeBtn">Covid
							Cases Distribution By Age (India)</button>
						<button type="button" class="btn btn-info chartButton"
							onclick="showChart(this)" id="pneumoniaCasesDistributionAgeBtn">Pneumonia
							Cases Distribution By Age (India)</button>
						<div id="chartDiv"></div>
					</div>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
				</div>
			</div>

		</div>
	</div>

	<div id="infoDeskModal" class="modal fade" role="dialog"
		data-backdrop="static">
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal">&times;</button>
				</div>
				<div id="infoDeskModalBody" class="modal-body"></div>
			</div>

		</div>
	</div>

</body>
<!-- Footer -->
<div class="footer-bottom">

	<div class="container89">

		<div class="row99">
			<div class="col-xs-12 col-sm-6 col-md-6 col-lg-6 custom-footer">


				<i class="glyphicon glyphicon-cog"></i> 2020 | PulmoPal<sup> <i
					class="glyphicon glyphicon-copyright-mark"></i></sup>
			</div>

			<div class="col-xs-12 col-sm-6 col-md-6 col-lg-6">

				<div class="design custom-footer">

					<i class="glyphicon glyphicon-wrench"></i> <span
						title="Designed Developed & Maintained by KOL Platform Dev Team.">
						Designed Developed & Maintained by "The Voyagers". </span>

				</div>

			</div>

		</div>

	</div>
</div>
<!-- FOOTER END -->
</html>