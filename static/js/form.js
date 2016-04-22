var ctx;
var options = [];
var progress = 0;

$( document ).ready(function() {
	$('.input-daterange').datepicker({
		autoclose: true
	});

	$('#stockForm').submit(function(event){
		event.preventDefault();

		$("#output").hide();

		$("#progress-container").show();
		var progressBarUpdater = window.setInterval(advanceProgressBar, 250);

		$.get("/api/prediction", $('#stockForm').serialize())
		.done(function(data){
			console.log(data);
			$("#progress-container").hide();
			progress = 0;
			advanceProgressBar();
			window.clearInterval(progressBarUpdater);

			displayResult(data);
		});

	});

	updateGraph($("#companySelect").val());

	$("#companySelect").change(function(event){
		updateGraph($("#companySelect").val());
	})

});



function updateGraph(company) {
	src = "https://chart.yahoo.com/z?s=" + company + "&t=6m&q=l&l=on&z=s&p=m50"
	$("#stockGraph").attr('src',src);
}

function advanceProgressBar() {
	$bar = $("div.progress-bar");
	if(progress > 100) progress = 100;
	$bar.css("width", progress + "%");
	progress = progress + 2.5;
}

function displayResult(data) {
	$output = $("#output");
	$outputHeader = $("#output h3");
	$outputText = $("#outputText");
	$outputIcon = $("#output .glyphicon");

	if (data > 0) {
		$outputText.text("Stocks will be rising!");
		$outputHeader.removeClass("text-danger").addClass("text-success");
		$outputIcon.removeClass("glyphicon-triangle-bottom").addClass("glyphicon-triangle-top")
	} else {
		$outputText.text("Stocks will be falling");
		$outputHeader.removeClass("text-success").addClass("text-danger");
		$outputIcon.removeClass("glyphicon-triangle-top").addClass("glyphicon-triangle-bottom")
	}
	$output.show();
}