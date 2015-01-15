$(document).ready(function (){

  // create a LatLng object containing the coordinate for the center of the map
  var latlng = new google.maps.LatLng(47.654463, 9.625980);

  // prepare the map properties
  var options = {
    zoom: 15,
    center: latlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    navigationControl: true,
    mapTypeControl: false,
    scrollwheel: false,
    disableDoubleClickZoom: true
  };

  // initialize the map object
  var map = new google.maps.Map(document.getElementById('google_map'), options);

  // add Marker
  var marker1 = new google.maps.Marker({
    position: latlng, map: map
  });

  // add listener for a click on the pin
  google.maps.event.addListener(marker1, 'click', function() {
    infowindow.open(map, marker1);
  });

  // add information window
  var infowindow = new google.maps.InfoWindow({
    content:  '<div class="info"><strong>Ernährungsberatung Michaela Tauch</strong><br>Holzhäusern 33<br> 88069 Tettnang</div>'
  });  
});

