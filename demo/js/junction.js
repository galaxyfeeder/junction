var map;

var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
var directionsService;

var currentStation = {};
var currentBus = null;

var stationMarkers = [];
var busMarkers = [];
var routeDirections = [];
var completeRoute = [];

function initMap() {
	directionsService = new google.maps.DirectionsService();
	
	var helsinki = {lat: 60.167469, lng: 24.961435}; //lat: 60.167469, lng: 24.961435
	map = new google.maps.Map(document.getElementById('map'), {
		zoom: 13,
		center: helsinki
	});
	
	//parseLines(lines);
	$.get( "http://junction.westeurope.cloudapp.azure.com/api/line/?format=json", function( data ) {
		//$( ".result" ).html( data );
		//alert( "Load was performed." );
		console.log("init : ****************************");
		console.log(data);
		parseLines(data);
	});
}

function print() {
	var seconds = 0;
	for(i=0;i<routeDirections.length;i++) {
		console.log(i);
		var k = routeDirections[i];
		var routes = k.directions.routes;
		for (j=0;j<routes.length;j++) {
			var route = routes[j];
			var legs = route.legs;
			for(k=0;k<legs.length;k++) {
				var leg = legs[k];
				seconds += leg.duration.value;
			}
		}
	}
	return seconds;
}

function clearStations() {
	for(i=0;i<stationMarkers.length;i++) {
		stationMarkers[i].setMap(null);
	}
	stationMarkers = [];
}
function clearDirections() {
	for(i=0;i<routeDirections.length;i++) {
		routeDirections[i].setMap(null);
	}
	routeDirections = [];
}
function clearBuses() {
	for(i=0;i<busMarkers.length;i++) {
		busMarkers[i].setMap(null);
	}
	busMarkers = [];
}
function clearAll() {
	clearStations();
	clearDirections();
	hideCompleteRoute();
	clearBuses();
}

function parseBuses(text) {
	info = JSON.parse(text);
	addBuses(info);
}

function hideCompleteRoute() {
	for(i=0;i<completeRoute.length;i++) {
		completeRoute[i].setMap(null);
	}
	completeRoute = [];
}
function showCompleteRoute() {
	hideCompleteRoute();
	addDirections(true);
}

function addBuses(buses) {
	for(i=0;i<buses.length;i++) {
		var image = {
			url:'http://www.theedgeproperty.com.sg/sites/all/modules/analytic/images/icons/bus.png',
			//url:'http://www.nyfalls.com/assets/maps/icons/transportation-blue/busstop.png'
			//size: new google.maps.Size(100, 100),
		};
		
		var marker = new google.maps.Marker({
			position: {lat: parseFloat(buses[i].latitude), lng: parseFloat(buses[i].longitude)},
			//label: labels[i % labels.length],
			map: map,
			icon: image,
			load: buses[i].load,
			code: buses[i].code,
			max: buses[i].max_capacity,
			myid: buses[i].id,
		});
		console.log(buses[i]);
		google.maps.event.addListener(marker, "click", function(event) { //{# https://developers.google.com/maps/articles/phpsqlinfo_v3 #}
			// ?????????????????
			showBusControls(this);
			//showStationControls(this.myid);
		});
		busMarkers.push(marker);
	}
}
function parseText(text) {
	clearAll();
	//info = JSON.parse(text);
	
	//addStations(info.stations);
	addStations(text);
	
	addDirections(true);
	addDirections(false);
}
function addStations(stations) {
	var bounds = new google.maps.LatLngBounds(); //{# http://stackoverflow.com/questions/1556921/google-map-api-v3-set-bounds-and-center?noredirect=1&lq=1 #}
	
	for(i=0;i<stations.length;i++) {
		console.log(stations[i]);
		
		var image = {
			//url:'http://www.theedgeproperty.com.sg/sites/all/modules/analytic/images/icons/bus.png',
			url:'http://www.nyfalls.com/assets/maps/icons/transportation-blue/busstop.png'
			//size: new google.maps.Size(100, 100),
		};
		
		var marker = new google.maps.Marker({
			position: {lat: parseFloat(stations[i].station.latitude), lng: parseFloat(stations[i].station.longitude)},
			//label: labels[i % labels.length],
			map: map,
			icon: image,
			code: stations[i].station.code,
			load: stations[i].people_waiting,
			myid: stations[i].station.id,
			goto: 1
		});
		bounds.extend(marker.position);
		google.maps.event.addListener(marker, "click", function(event) { //{# https://developers.google.com/maps/articles/phpsqlinfo_v3 #}
			//console.log(stations.stations[i].id);
			//console.log(this.position.lat() + " - " + this.position.lng()); //{# http://stackoverflow.com/questions/6374329/get-latitude-and-longitude-of-marker-onclick #}
			//console.log(this.myid);
			showStationControls(this);
		});
		
		stationMarkers.push(marker);
	}
	map.fitBounds(bounds);
}
function showStationControls(station) {
	$(".item-title").text("Station "+station.code);
	$(".bus-control").hide();
	$(".station-control").show();
	/*$.get( "http://junction.westeurope.cloudapp.azure.com/api/station/" + station.myid + "/?format=json", function( data ) {
		var stops = data.stops;
		var somme = 0;
		for (i=0;i<stops.length;i++) {
			var stop = stops[i];
			somme += stop.people_waiting;
		}
		$("#station-count").html(somme);
		//parseLines(data);
	}); */
	currentBus = null;
	currentStation.id = station.myid;
	currentStation.load = station.load;
	$("#station-count").html(currentStation.load);
}
function showBusControls(bus) {
	$(".item-title").text("Bus " + bus.code);
	$(".bus-control").show();
	$(".station-control").hide();
	currentStation = {};
	currentBus = bus.code;
}

function addDirections(all) {
	var tmpStations = [];
	for(i=0; i<stationMarkers.length; i++) {
		var sm = stationMarkers[i];
		if(true || all) { // sm.myid != 2 ||
			tmpStations.push(sm);
		}
	}
	
	for(i=0; i<tmpStations.length - 1 ; i++) {
		var sm = tmpStations[i];
		var next = tmpStations[i+1];
		var travelMode = google.maps.DirectionsTravelMode.DRIVING;  
		var request = {
			origin: sm.position,
			destination: next.position,
			travelMode: travelMode
		};  
		var rendererOptions = {
			map: map,
			suppressMarkers : true,
			preserveViewport: true
		}
		if(all) {
			rendererOptions.polylineOptions = {strokeColor: "#111", strokeOpacity: 0.3, strokeWeight:5};
		}
		directionsService.route(request, function(response, status) {
			disp = new google.maps.DirectionsRenderer(rendererOptions);     
			disp.setMap(map);
			disp.setDirections(response);
			if (all) {
				completeRoute.push(disp);
			}else {
				routeDirections.push(disp);
			}
		});
	}
}

function parseLines(text) {
	//var tmp = JSON.parse(text);
	var tmp = text;
	for(i=0;i<tmp.length;i++) {
		var line = tmp[i];
		$(".lines").append("<li><a class='line' href='javascript:void(0)' data-id='" + line.id + "' data-linenumber='" + line.number + "' >" + line.number + "</a></li>");
	}
	
	$(".line").on("click", function() {
		$(".line-title").text($(this).data('linenumber') + " line");
		$(".line-control").show();
		
		$("#btn-show-complete").hide();
		$("#btn-hide-complete").show();
		
		$.get( "http://junction.westeurope.cloudapp.azure.com/api/line/" + $(this).data("id") + "/?format=json", function( data ) {
			//parseLines(data);
			parseText(data.stops);
			addBuses(data.buses);
		});
		
		//alert($(this).data("linenumber"));
		//parseText(stationsText);
		//parseBuses(buss);
	});
}

function getBusById(id) {
	//return busMarkers[0];
	for (i=0; i<busMarkers.length; i++) {
		if(busMarkers[i].myid == id) return busMarkers[i];
	}
	return;
}
function getStationById(id) {
	//return busMarkers[0];
	for (i=0; i<stationMarkers.length; i++) {
		if(stationMarkers[i].myid == id) return stationMarkers[i];
	}
	return;
}

// ---------------------------------------------------

var stationsText = '{ "stations" : [' +
'{ "name":"Solvik" , "lat":60.1680265 , "lng":24.9375109, "id":1 },' + //60.1680265,24.9375109 //ORIGINAL-60.201517-24.375928
'{ "name":"Louhosmäki" , "lat":60.165650 , "lng":24.936524, "id":2 },' + //60.165650, 24.936524 //ORIGINAL-60.202282-24.358088
'{ "name":"Evitskog" , "lat":60.1649276 , "lng":24.9288585, "id":3},' + //60.1649276,24.9288585 //ORIGINAL-60.20141-24.342
'{ "name":"", "lat":60.1619962, "lng":24.9289412, "id":4}]}'; 

var lines = '[{"name":"Lijn 14"},{"name":"Lijn 17"}]';

var buss = '[{"id":10,"lat":60.168067,"lng":24.934156},{"id":20,"lat":60.165238,"lng":24.929650},{"id":30,"lat":60.163039,"lng":24.928191}]';


$(".line-control").hide();
$(".station-control").hide();
$(".bus-control").hide();
$("#btn-show-complete").hide();


$("#btn-show-complete").on("click", function() {
	showCompleteRoute();
	$("#btn-show-complete").hide();
	$("#btn-hide-complete").show();		
});
$("#btn-hide-complete").on("click", function() {
	hideCompleteRoute();
	$("#btn-show-complete").show();
	$("#btn-hide-complete").hide();
});

$("#bus-load").slider();
$("#bus-load").on("slideStop", function(event) {
	console.log(event.value);
	if(event.value[1] < event.value[0]) { //max is less than min
		$("#bus-load").slider('setValue', [event.value[0], event.value[0]]);
	}
	if(event.value[0] > event.value[1]) { //min is greater than max
		$("#bus-load").slider('setValue', [event.value[1], event.value[1]]);
	}
});

function changeLoad(load) {
	currentStation.load = load;
	$("#station-count").html(load);
	getStationById(currentStation.id).load = load;
	//API REQUEST !!!!!
}

$("#station-less").on("click", function() {
	var tmp = currentStation.load -2;
	if (tmp < 0) tmp = 0;
	changeLoad(tmp);
});
$("#station-0").on("click", function() {
	changeLoad(0);
});
$("#station-more").on("click", function() {
	changeLoad(currentStation.load +2);
});
