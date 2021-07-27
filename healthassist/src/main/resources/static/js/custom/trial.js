var formDataObj;
var file;
var imageBase64OriginalWithB;
var imageBase64HeatMapWithB;
var imageBase64Original;
var imageBase64HeatMap;
var userAgreed = "";
var imageBase64Prefix = 'data:image/jpeg;base64,';
var uploadedFileName = "";
var diagnosis = "";

function onCxrSelect() {
    userAgreed = "";
    $('#disagree').show();
    $('#disagreeLabel').show();
    $('#agree').show();
    $('#agreeLabel').show();
    $('#userDataDiv').hide();
    $('#userConsentDiv').show();
    $('#userConsentLabel').html("");
    $('#selectFileBtn').attr("disabled", true);
    $('#selectFileBtn').attr("title", "Accept/Decline user consent");
    $('#proceedBtn').attr("disabled", true);
    $('#proceedBtn').attr("title", "Select an image file to proceed");
    $('#heatMapBtn').hide();
    $("#heatMapContainer").empty();
    $('#openMailModalBtn').hide();
    $("#analysisResultDiv").empty();
    $('#analysisResultDiv').hide();
    $('#agree').prop('checked', false);
    $('#disagree').prop('checked', false);
    $("input[type!='radio']").val("");
    $("input[type!='radio']").text("");
    $("input[type='radio']").prop('checked', false);
    $('#hdnSelectFileBtn').val("");
    formDataObj = new FormData();
    emailFormData = new FormData();
}

$(document).ready(function () {

    $(document).find('.carouselImage').each(function () {
        var imgClass = (this.width / this.height > 1) ? 'wide' : 'tall';
        $(this).addClass(imgClass);
    });

    formDataObj = new FormData();
    emailFormData = new FormData();

    $('#agree').click(function () {
        $('#disagree').hide();
        $('#disagreeLabel').hide();
        $('#userDataDiv').show();
        $('#userConsentDiv').hide();
        $('#userConsentLabel').removeClass("label-warning");
        $('#userConsentLabel').addClass("label-info");
        $('#userConsentLabel').html("User Data Consent : AGREED");
        $('#userConsentLabel').attr("title", "User Data Consent : AGREED");
        $('#selectFileBtn').attr("title", "Send User Data to proceed to file selection");
        userAgreed = true;
    });

    $('#disagree').click(function () {
        $('#agree').hide();
        $('#agreeLabel').hide();
        $('#userConsentDiv').hide();
        $('#userConsentLabel').removeClass("label-info");
        $('#userConsentLabel').addClass("label-warning");
        $('#userConsentLabel').html("User Data Consent : DISAGREED");
        $('#userConsentLabel').attr("title", "User Data Consent : DISAGREED");
        formDataObj.append('first_name', "NODATA");
        formDataObj.append('last_name', "NODATA");
        formDataObj.append('age', "NODATA");
        formDataObj.append('gender', "NODATA");
        formDataObj.append('location', "NODATA");
        $('#selectFileBtn').attr("disabled", false);
        $('#selectFileBtn').attr("title", "Select a file to upload");
    });

    $('#selectFileBtn').click(function () {
        $('#hdnSelectFileBtn').click();
    });

    var inputElement = document.getElementById("hdnSelectFileBtn");
    inputElement.addEventListener("change", handleFiles, false);

    function handleFiles() {

        var fileList = this.files;
        var uploadedFilePath = $('#hdnSelectFileBtn').val();
        uploadedFileName = uploadedFilePath.substring(uploadedFilePath.lastIndexOf("\\") + 1, uploadedFilePath.length);
        file = fileList[0];

        if (!uploadedFileName.endsWith(".jpg") && !uploadedFileName.endsWith(".jpeg")) {
            $("#errorDiv").html("Please enter a proper image file (.jpg or .jpeg)");
            $('#errModal').modal('show');
            $('#errorHeader').empty();
            $('#errorHeader').html("Incorrect File Type Selected!");
            $('#errorText').empty();
            $('#errorText').html("Please enter a proper image file (.jpg or .jpeg)");
        } else {
            $('#selectFileBtn').attr("disabled", true);
            $('#selectFileBtn').attr("title", "Image File Selected : " + uploadedFileName);
            $('#proceedBtn').removeAttr("disabled");
            $('#removeFile').show();
            $('#removeFile').attr("title", "Remove Selected File : " + uploadedFileName);
            $('#proceedBtn').attr("title", "Click to Begin Analysis!")
            $("#errorDiv").html("");
        }

        var url = "http://localhost:8081/meta/upload";
        var fileData = new FormData();
        fileData.append("file", file);

        $.ajax({
            type: "POST",
            url: url,
            data: fileData,
            enctype: 'multipart/form-data',
            processData: false,
            contentType: false,
            cache: false,
            success: function (data) {
                console.log(data);
                if (data.startsWith("File Uploaded")) {
                    console.log("Uploaded File Name : " + uploadedFileName);
                }
            }
        });


    }

    $('#removeFile').click(function () {
        file = "";
        $('#selectFileBtn').removeAttr("disabled");
        $('#selectFileBtn').attr("title", "Select an image file to proceed");
        $('#proceedBtn').attr("disabled", true);
        $('#proceedBtn').attr("title", "Select an image file to proceed");
        $('#removeFile').attr("disabled", true);
        $('#removeFile').attr("title", "No file is selected");
        $('#removeFile').css("cursor", "not-allowed");
        $('#removeFile').hide();
    });

    $('#heatMapBtn').click(function () {

        //Actual functionality
        imageBase64Original = imageBase64OriginalWithB.substring(2, imageBase64OriginalWithB.length - 1); // Comment while using Dummy Data
        imageBase64HeatMap = imageBase64HeatMapWithB.substring(2, imageBase64HeatMapWithB.length - 1); // Comment while using Dummy Data

        //Dummy image base64 // Uncomment the two statements while using Dummy Data
        //imageBase64Original = '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';
        //imageBase64HeatMap = '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';

        var imageStr = "<br/><div align=\"center\"><div class=\"col-md-4 imageShowDiv\"><img title=\"Original CXR\" src=\"" + imageBase64Prefix + imageBase64Original + "\"></div><div class=\"col-md-4 imageShowDiv\"><img title=\"Heat Map\" src=\"" + imageBase64Prefix + imageBase64HeatMap + "\"></div></div>";
        $("#heatMapContainer").empty();
        $("#heatMapContainer").append(imageStr);
        $("#openMailModalBtn").show();
    });


    $('#uploadBtn').click(function () {
        $('#hdnFileUploadBtn').click();
    });

    $("#uploadBtn").click(function () {

        //e.preventDefault(); // avoid to execute the actual submit of the form.

        var form = $("#uploadForm");
        var url = "http://localhost:8081" + form.attr('action');

        $.ajax({
            type: "POST",
            url: url,
            data: new FormData($("#uploadForm")),
            enctype: 'multipart/form-data',
            processData: false,
            contentType: false,
            cache: false,
            success: function (data) {
                console.log(data);
                if (data.startsWith("File Uploaded")) {
                    $('#proceedBtn').removeAttr("disabled");
                    $('#proceedBtn').attr("title", "Click to Begin Analysis!")
                }
            }
        });

    });

    $("#submitUserDataBtn").click(function () {
        validateUserData();
        $('#userConsentDiv').hide();
        $('#userDataDiv').hide();
        $('#selectFileBtn').removeAttr("disabled");
        $('#selectFileBtn').attr("title", "Select an image file to proceed")
    });

    function validateUserData() {
        var errorHeader = "The following data were not provided. Anonymous data will be saved."
        var errorText = "<ul>";
        var errorInData = false;
        if (userAgreed) {
            if ($("#firstNameText").val().trim() == "") {
                formDataObj.append('first_name', "NODATA");
                errorText = errorText + "<li>First Name</li>";
                errorInData = true;
            } else {
                formDataObj.append('first_name', btoa($("#firstNameText").val().trim()));
            }
            if ($("#lastNameText").val().trim() == "") {
                formDataObj.append('last_name', "NODATA");
                errorText = errorText + "<li>Last Name</li>";
                errorInData = true;
            } else {
                formDataObj.append('last_name', btoa($("#lastNameText").val().trim()));
            }
            if ($("#age").val().trim() == "") {
                formDataObj.append('age', "NODATA");
                errorText = errorText + "<li>Age</li>";
                errorInData = true;
            } else {
                formDataObj.append('age', $("#age").val());
            }
            if (!$("input[name='gender']:checked").val()) {
                formDataObj.append('gender', "NODATA");
                errorText = errorText + "<li>Gender</li>";
                errorInData = true;
            } else {
                formDataObj.append('gender', $("input[name='gender']:checked").val().trim());
            }
            if ($("#stateSelect option:selected").val().trim() == "") {
                formDataObj.append('location', "NODATA");
                errorText = errorText + "<li>Location</li>";
                errorInData = true;
            } else {
                formDataObj.append('location', $("#stateSelect option:selected").val());
            }

            errorText = errorText + "</ul>";
            if (errorInData) {
                $('#errModal').modal('show');
                $('#errorHeader').empty();
                $('#errorHeader').html(errorHeader);
                $('#errorText').empty();
                $('#errorText').html(errorText);
                errorInData = false;
            }
        }
    }

    $("#proceedBtn").on('click', function () {
        $("#overlay").show();
        $('#proceedBtn').attr("disabled", true);
        $('#proceedBtn').attr("title", "Analysis in progress...");
        $('#analysisResultDiv').empty();
        $('#analysisResultDiv').show();
        //$('#heatMapBtn').click(); // Uncomment while using Dummy Data
        formDataObj.append('imagefile', file);
        $.ajax({
            type: "POST",
            url: "http://192.168.0.100:5005/uploadImage",
            data: formDataObj,
            enctype: 'multipart/form-data',
            processData: false,
            contentType: false,
            cache: false,
            success: function (data) {
                console.log(data);
                $("#overlay").hide();
                $("#analysisResult").show();
                imageBase64OriginalWithB = data.Encoded_Image_Original; // Comment while using Dummy Data
                imageBase64HeatMapWithB = data.Encoded_Image_HeatMap; // Comment while using Dummy Data

                //alert(data.Predicted_Result);
                diagnosis = data.Predicted_Result;

                // Comment the if block while using Dummy Data
                if (data.Predicted_Result != "Normal") {

                    if (data.Predicted_Result == "Covid") {
                        $("#analysisResultDiv").removeClass("label-warning");
                        $("#analysisResultDiv").removeClass("label-info");
                        $("#analysisResultDiv").addClass("label-danger");
                        $("#analysisResultDiv").css("color", "white");
                        $("#analysisResultDiv").css("font-weight", "bold");
                    } else if (data.Predicted_Result == "Pneumonia") {
                        $("#analysisResultDiv").removeClass("label-danger");
                        $("#analysisResultDiv").removeClass("label-info");
                        $("#analysisResultDiv").addClass("label-warning");
                    }
                    $("#analysisResultDiv").empty();
                    $("#analysisResultDiv").append("DIAGNOSIS : Suspected " + data.Predicted_Result);
                    $("#heatMapBtn").show();
                    $('#heatMapBtn').attr("title", "Click to see heat map for " + data.Predicted_Result);
                } else {
                    $("#analysisResultDiv").removeClass("label-danger");
                    $("#analysisResultDiv").removeClass("label-warning");
                    $("#analysisResultDiv").addClass("label-info");
                    $("#analysisResultDiv").empty();
                    $("#analysisResultDiv").append("DIAGNOSIS : " + data.Predicted_Result);
                }
                $('#removeFile').hide();
                $('#proceedBtn').attr("title", "Analysis Done");
            },
            error: function (data) {
                console.log(data);
            }
        });

    });

    $("#sendEmailBtn").on('click', function () {
        var heatMapFileObj;

        emailFormData.append("recipientAddress", $("#emailAddress").val());
        emailFormData.append("recipientName", $("#name").val());
        emailFormData.append("fileName", uploadedFileName);
        emailFormData.append("recipient", $("input[name='recipient']:checked").val().trim());
        emailFormData.append("diagnosis", diagnosis);

        console.log(emailFormData);

        $.ajax({
            type: "POST",
            url: "http://localhost:8081/meta/sendEmail",
            data: emailFormData,
            enctype: 'multipart/form-data',
            processData: false,
            contentType: false,
            cache: false,
            success: function (data) {
                console.log(data);
                if(data == "Email Sent!") {
                	$('#emailModal').modal('hide');
                }
            },
            error: function (data) {
                console.log(data);
            }

        });
    });
    
    
    $("#infoDeskDivBtn").on('click', function () {
    	var popUpObj = window.open("http://localhost:8081/meta/infodesk", "ModalPopUp", "toolbar=no, scrollbars=no, location=no, statusbar=no, menubar=no, resizable=0, left=100px");
    	popUpObj.focus();
    });

});

function showChart(obj) {
    var graphUrl = "";
    var graphType = "";
    var disease = "";
    
    if (obj.id == 'maleDistributionBtn') {
        graphUrl = "http://192.168.0.100:5007/maleDist";
    } else if (obj.id == 'femaleDistributionBtn') {
        graphUrl = "http://192.168.0.100:5007/femaleDist";
    } else if (obj.id == 'covidCasesDistributionBtn') {
    	graphUrl = "http://192.168.0.100:5006/getIndiaGraph";
    	disease = "Covid";
    	graphType = "India";
    } else if (obj.id == 'pneumoniaCasesDistributionBtn') {
        graphUrl = "http://192.168.0.100:5006/getIndiaGraph";
        disease = "Pneumonia";
    	graphType = "India";
    } else if (obj.id == 'covidCasesDistributionAgeBtn') {
    	graphUrl = "http://192.168.0.100:5007/ageDist";
    	disease = "Covid";
    	graphType = "Age";
    } else if (obj.id == 'pneumoniaCasesDistributionAgeBtn') {
        graphUrl = "http://192.168.0.100:5007/ageDist";
        disease = "Pneumonia";
    	graphType = "Age";
    }

	if(graphType == "India" || graphType == "Age") {
        $("#overlay").show();
		
		$.ajax({
	        type: "GET",
	        url: graphUrl+"?disease="+disease,
            processData: false,
            contentType: false,
            cache: false,
	        success: function (data) {
	            console.log(data);
	            var imageBase64IndiaGraphWithB;
	            
	            if( graphType == "India" ) {
	            	imageBase64IndiaGraphWithB = data.Encoded_Graph;
	            } else if( graphType == "Age" ) {
	            	imageBase64IndiaGraphWithB = data.Encoded_Image_Graph;
	            }
	            
	            var imageBase64IndiaGraphStr = imageBase64IndiaGraphWithB.substring(2, imageBase64IndiaGraphWithB.length - 1);
	            var imageStr = "<br/><div align=\"center\"><div class=\"imageShowDiv\"><img src=\"" + imageBase64Prefix + imageBase64IndiaGraphStr + "\"></div>";
	            $("#chartDiv").empty();
	            $("#chartDiv").append(imageStr);
        		$("#overlay").hide();
	        },
	        error: function (data) {
	            console.log(data);
	        }
	
	    });
	} else {
        $("#overlay").show();
	    $.ajax({
	        type: "GET",
	        url: graphUrl,
	        cache: false,
	        success: function (data) {
	            console.log(data);
	            var imageBase64GraphWithB = data.Encoded_Image_Graph;
	            var imageBase64GraphStr = imageBase64GraphWithB.substring(2, imageBase64GraphWithB.length - 1);
	            var imageStr = "<br/><div align=\"center\"><div class=\"imageShowDiv\"><img src=\"" + imageBase64Prefix + imageBase64GraphStr + "\"></div>";
	            $("#chartDiv").empty();
	            $("#chartDiv").append(imageStr);
        		$("#overlay").hide();
	        },
	        error: function (data) {
	            console.log(data);
	        }
	
	    });
    }
}