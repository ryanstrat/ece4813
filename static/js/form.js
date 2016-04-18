var ctx;
var options = [];

$( document ).ready(function() {
	$('.input-daterange').datepicker({
		autoclose: true
	});

	$('#stockForm').submit(function(event){
		event.preventDefault();

		$.get("/api/prediction", $('#stockForm').serialize());
	});

	//ctx = document.getElementById("stockPrice").getContext("2d");
	//var stockChart = new Chart(ctx).Line([]], options);

});

function populateChart(data) {
	data = [];
	var stockChart = new Chart(ctx).Line(data, options);
}


