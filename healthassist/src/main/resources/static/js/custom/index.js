/**
 * 
 */
var selectedType = "";
var selectedJvmFilterType = "";
var selectedALTUrl = "";
var timeSelectFilter = "";
var healthPercentage;
var healthyResources = [];
var unhealthyResources = [];

function onJvmTypeSelect(obj) {
	selectedType = $.trim(obj.value);
	if (selectedType != null && selectedType != ""
			&& selectedType != "Select JVM Type") {
		$("button#proceedBtn").prop("title", "Proceed for " + selectedType);
		$("select#JVMType").prop("title", "Selected JVM : " + selectedType);
		$("button#proceedBtn").prop("disabled", false);
		$("select#ALT-Url").prop("disabled", false);
		$("select#ALT-Url").prop("title", "Select an ALT URL");
		$("button#proceedBtn").removeClass("label label-default");
		$("button#proceedBtn").addClass("label label-primary");
		$("button#proceedBtn").css({
			"color" : "white"
		});

	} else {
		// $('#content').hide();
		/* $('#titleHeader').empty() */
		$("select#ALT-Url").prop("disabled", true);
		$("select#ALT-Url").prop("title", "Select JVM Type to enable");
		$('#MFCTypeShowDiv').empty();
		$('#MFCTypeShowDiv').hide();
		if (selectedALTUrl != null && selectedALTUrl != ""
				&& selectedALTUrl != "Select ALT Url") {
			$("button#proceedBtn").prop(
					"title",
					"Proceed for " + selectedType + " with URL : "
							+ selectedALTUrl);
		} else {
			$("button#proceedBtn").prop("title",
					"Please select a JVM and/or ALT Url to enable button");
		}
		$("button#proceedBtn").prop("disabled", true);
		$("button#proceedBtn").removeClass("label label-primary");
		$("button#proceedBtn").addClass("label label-default");
		$("button#proceedBtn").css({
			"color" : "darkgrey"
		});

	}
}

function onALTUrlSelect(obj) {
	selectedALTUrl = $.trim(obj.value);
	if (selectedALTUrl != null && selectedALTUrl != ""
			&& selectedALTUrl != "Select ALT Url") {
		$("button#proceedBtn")
				.prop(
						"title",
						"Proceed for " + selectedType + " with URL : "
								+ selectedALTUrl);
		$("select#ALT-Url").prop("title",
				"Selected ALT Url : " + selectedALTUrl);
		$("button#proceedBtn").prop("disabled", false);
		$("button#proceedBtn").removeClass("label label-default");
		$("button#proceedBtn").addClass("label label-primary");
		$("button#proceedBtn").css({
			"color" : "white"
		});

	} else {
		// $('#content').hide();
		/* $('#titleHeader').empty() */
		$('#MFCTypeShowDiv').empty();
		$('#MFCTypeShowDiv').hide();
		$("button#proceedBtn").prop("title",
				"Please select a JVM and/or ALT Url to enable button");
		$("button#proceedBtn").prop("disabled", true);
		$("button#proceedBtn").removeClass("label label-primary");
		$("button#proceedBtn").addClass("label label-default");
		$("button#proceedBtn").css({
			"color" : "darkgrey"
		});

	}
}

function onJvmTypeFilterSelect(obj) {
	selectedJvmFilterType = $.trim(obj.value);
	if (selectedJvmFilterType != null && selectedJvmFilterType != ""
			&& selectedJvmFilterType != "Select JVM Type") {
		$("button#proceedFilterBtn").prop("title",
				"Proceed for " + selectedJvmFilterType);
		$("select#JVMType").prop("title",
				"Selected JVM : " + selectedJvmFilterType);
		$("button#proceedFilterBtn").prop("disabled", false);
		$("select#timeFilter").prop("disabled", false);
		$("select#timeFilter").prop("title", "Select a Time Filter");
		$("button#proceedFilterBtn").removeClass("label label-default");
		$("button#proceedFilterBtn").addClass("label label-primary");
		$("button#proceedFilterBtn").css({
			"color" : "white"
		});

	} else {
		// $('#content').hide();
		/* $('#titleHeader').empty() */
		$("select#ALT-Url").prop("disabled", true);
		$("select#ALT-Url").prop("title", "Select JVM Type to enable");
		$('#MFCTypeShowDiv').empty();
		$('#MFCTypeShowDiv').hide();
		if (timeSelectFilter != null && timeSelectFilter != ""
				&& timeSelectFilter != "Select ALT Url") {
			$("button#proceedFilterBtn").prop(
					"title",
					"Proceed for " + selectedJvmFilterType + " with Filter : "
							+ timeSelectFilter);
		} else {
			$("button#proceedFilterBtn").prop("title",
					"Please select a JVM and/or Time Filter to enable button");
		}
		$("button#proceedFilterBtn").prop("disabled", true);
		$("button#proceedFilterBtn").removeClass("label label-primary");
		$("button#proceedFilterBtn").addClass("label label-default");
		$("button#proceedFilterBtn").css({
			"color" : "darkgrey"
		});

	}
}

function onTimeSelect(obj) {
	timeSelectFilter = $.trim(obj.value);
	if (timeSelectFilter != null && timeSelectFilter != ""
			&& timeSelectFilter != "Select ALT Url") {
		$("button#proceedBtn").prop(
				"title",
				"Proceed for " + selectedType + " with Filter : "
						+ timeSelectFilter);
		$("select#ALT-Url").prop("title",
				"Selected ALT Url : " + timeSelectFilter);
		$("button#proceedBtn").prop("disabled", false);
		$("button#proceedBtn").removeClass("label label-default");
		$("button#proceedBtn").addClass("label label-primary");
		$("button#proceedBtn").css({
			"color" : "white"
		});

	} else {
		// $('#content').hide();
		/* $('#titleHeader').empty() */
		$('#MFCTypeShowDiv').empty();
		$('#MFCTypeShowDiv').hide();
		$("button#proceedBtn").prop("title",
				"Please select a JVM and/or Time Filter to enable button");
		$("button#proceedBtn").prop("disabled", true);
		$("button#proceedBtn").removeClass("label label-primary");
		$("button#proceedBtn").addClass("label label-default");
		$("button#proceedBtn").css({
			"color" : "darkgrey"
		});

	}
}

$(function() {
	/* Submit form using Ajax */
	$('button[id=proceedBtn]')
			.click(
					function(e) {

						// Prevent default submission of form
						e.preventDefault();
						$('#overlay').show();
						$
								.ajax({
									type : "GET",
									url : 'http://localhost:8081/'
											+ selectedALTUrl,
									data : {
										"JVM_Name" : selectedType
									},
									complete : function(res) {
										// console.log("STATUS : " +
										// JSON.parse(res).dependencies);
										$('#responsePre').show();
										$('#responsePre').html(
												JSON.stringify(
														res.responseJSON,
														undefined, 4));
										$('#searchDivIcon').show();
										$('#JVMTypeShowDiv').show();
										$('#JVMTypeShowDiv').empty().html(
												"JVM : " + selectedType
														+ "<br/>ALT URL : "
														+ selectedALTUrl);

										if (selectedALTUrl == "meta/health"
												|| selectedALTUrl == "meta/health/diagnostic") {
											$('#showChartButton').show();
											$('#JVMTypeShowDiv').show();
											$('#content').show();
											$('#content').css('top', '25%');
											$('#checkNowPill a').click();
											$('#showHealthyBtn').show();
											$('#showUnhealthyBtn').show();
											$('#searchDivIcon').show();
											$('#searchDivIcon').fadeIn(500);
											$('#searchDiv').fadeOut(500);
											showData(res.responseJSON);
										}
										$('#overlay').hide();
									},
									error : function(res) {
										alert(res)
									}
								});
					});

	$('button[id=proceedFilterBtn]').click(function(e) {

		// Prevent default submission of form
		e.preventDefault();
		$('#overlay').show();
		$.ajax({
			type : "GET",
			url : 'http://localhost:8081/meta/pastrecords',
			data : {
				"JVM_Name" : selectedJvmFilterType,
				"timeFrameInHours" : timeSelectFilter
			},
			complete : function(res) {
				$('#showTrendButton').show();
				$('#overlay').hide();
				showTrendChart(res);
			},
			error : function(res) {
				alert(res)
			}
		});
	});
});

function showData(res) {
	console.log(res);
	var dep = res.dependencies;
	console.log(dep);
	var healthyCount = 0;
	var unhealthyCount = 0;
	var totalResources = dep.length;
	for ( var data in dep) {
		if (dep[data].healthy == true) {
			healthyCount++;
			healthyResources.push(dep[data].id);
		} else {
			unhealthyCount++;
			unhealthyResources.push(dep[data].id);
		}
	}
	$('#showHealthyBtn').html("HEALTHY RESOURCES : " + healthyCount);
	$('#showUnhealthyBtn').html("UNHEALTHY RESOURCES : " + unhealthyCount);

	var healthyStr = "<ul class=\"list-group\">"
	for ( var resource in healthyResources) {
		healthyStr = healthyStr
				+ "<li class=\"list-group-item\" style=\"background-color: #87EE86; width: auto;\"><strong>"
				+ healthyResources[resource] + "</strong></li>"
	}
	healthyStr = healthyStr + "</ul>";

	var unhealthyStr = "<ul class=\"list-group\">"
	for ( var resource in unhealthyResources) {
		unhealthyStr = unhealthyStr
				+ "<li class=\"list-group-item\"  style=\"background-color: #FA6253; width: auto;\"><strong>"
				+ unhealthyResources[resource] + "</strong></li>"
	}
	unhealthyStr = unhealthyStr + "</ul>";

	$('#healthyResources').html(healthyStr);
	$('#unhealthyResources').html(unhealthyStr);
	healthPercentage = (healthyCount / totalResources) * 100;
	representData();
}

function showTrendChart(res) {
	$('#trendContainer').show();
	var respObj = res.responseJSON;
	console.log(respObj);
	$('#trendHeader').html("Health Trend for " + selectedJvmFilterType);
	var dataArray = [];
	console.log(respObj[selectedJvmFilterType]);
	console.log(respObj[selectedJvmFilterType].length);
	for (var i = 0; i < respObj[selectedJvmFilterType].length; i++) {
		var obj = respObj[selectedJvmFilterType][i];
		var healthPercentage = obj.HealthPercentage;
		var value = obj.Timestamp;
		dataArray.push({
			x : value,
			y : healthPercentage
		});
	}

	var chart = new CanvasJS.Chart("trendContainer", {
		zoomEnabled : true,

		title : {
			text : "Health Trend of " + selectedJvmFilterType
		},
		axisX : {
			valueFormatString : "YYYY-MM-DD hh:mm:ss",
			title : "Time"

		},
		axisY : {
			valueFormatString : "0.00#",
			title : "Health %"
		},

		data : [ {
			type : "line",
			xValueType : "dateTime",
			dataPoints : dataArray
		} ]
	});

	chart.render();
}

/*function showTrend() {
	$('#trendContainer').show();
}*/

function showSearchDiv() {
	if ($('#searchDiv').is(":visible")) {
		$('#searchDiv').fadeOut(500);
	} else {
		$('#searchDiv').fadeIn(500);
		$('#searchDivIcon').fadeIn(500);
	}
}

function showFilterDiv() {
	if ($('#filterDiv').is(":visible")) {
		$('#filterDiv').fadeOut(500);
	} else {
		$('#filterDiv').fadeIn(500);
		$('#filterDivIcon').fadeOut(500);
	}
}

function toggleJVMTypeShow() {
	//if ($('#filterDiv').is(":visible")) {
		$('#JVMTypeShowDiv').hide();
	//}
}

/*
 * $(document).click(function() { if($('#searchDivIcon').is(":visible")) {
 * //$('#searchDiv').fadeOut(500); } else {
 *//** * searchDivIcon is not visible ** */
/*
 * if($('#content').is(":visible")) { $('#searchDiv').fadeOut(500);
 * $('#searchDivIcon').fadeIn(500); } } });
 */

/*
 * $(window).click(function() { if($('#searchDiv').is(":visible")) {
 * $('#searchDiv').fadeOut(500); } else { $('#searchDiv').fadeIn(500);
 * $('#searchDivIcon').fadeOut(500); } });
 */

function representData() {
	var healthy = healthPercentage;
	var unhealthy = 100 - healthy;
	$('#chartHeader').html("Health Chart for " + selectedType);
	var chart = new CanvasJS.Chart("chartContainer", {
		animationEnabled : true,
		title : {
			text : "Health Chart for " + selectedType
		},
		data : [ {
			type : "pie",
			startAngle : 240,
			yValueFormatString : "##0.00\"%\"",
			indexLabel : "{label} {y}",
			dataPoints : [ {
				y : healthy,
				label : "Healthy"
			}, {
				y : unhealthy,
				label : "Unhealthy"
			} ]
		} ]
	});
	chart.render();
}