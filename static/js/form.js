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

	updateGraph($("#companySelect").val());

	$("#companySelect").change(function(event){
		updateGraph($("#companySelect").val());
	})

});



function updateGraph(company) {
	src = "https://chart.yahoo.com/z?s=" + company + "&t=6m&q=l&l=on&z=s&p=m50"
	$("#stockGraph").attr('src',src);
}


