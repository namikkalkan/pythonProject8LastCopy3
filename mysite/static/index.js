
function initMap() {

  var options = {
         zoom :12,
         center :{ lat: -37.844091, lng: 145.003759 }}
  // The map, centered at Uluru
  if (document.getElementById("map")){
      var map = new google.maps.Map(document.getElementById("map"), options);
      // listen for clicks
     /* google.maps.event.addListener(map,'click',function(event){
          addMarker({ coord:event.latLng

          });
          });*/
      // The marker, positioned at Uluru
      const marker = new google.maps.Marker({
        position: { lat: -37.844091, lng: 145.003759 },
        map: map,
      });


      var infoWindow = new google.maps.InfoWindow({
           content : "<div class ='box small' style='float:left'><img id='surf1' src='static/assets/surf.jpg'></div><div style='float:right; padding: 10px;'><b>Surf Board</b><br><b>$18.00</b>"
           });
           marker.addListener('click', function(){
           infoWindow.open(map,marker);
           });
      function test1(){alert("test1");}

      function addMarker(props){
        const marker = new google.maps.Marker({
            position: props.coord,
            map: map,
             });
        //icon :props.iconImg
        //check icon
        if (props.iconImg){
            marker.setIcon(props.iconImg);}

        if (props.content){
            var infoWindow = new google.maps.InfoWindow({
                content: props.content
               });
            marker.addListener('click', function(){
            infoWindow.open(map,marker);
            });
           }
        }




      // list of markers here
      var markers = [{
                  coord:{lat:-37.840658,lng:145.000981},
                  content : "<div class ='box small' style='float:left'><img id='surf1' src='static/assets/camping.jpg'></div><div style='float:right; padding: 10px;'><b>Soft Surf Board</b><br><b>$15.00</b>",
                  },
                  {coord:{lat:-37.864633,lng:144.988386},
                  content : "<div class ='box small' style='float:left'><img id='surf1' src='static/assets/board.jpg'></div><div style='float:right; padding: 10px;'><b>Soft Surf Board</b><br><b>$15.00</b>",
                  },
                 {coord:{lat:-37.839771,lng:144.921534},
                  content : "<div class ='box small' style='float:left'><img id='surf1' src='static/assets/board.jpg'></div><div style='float:right; padding: 10px;'><b>Soft Surf Board</b><br><b>$15.00</b>",
                  },


      ]

      // loop all markers

      for (var i =0 ; i < markers.length; i++){
        //if (markers[i].content =='training') {
        addMarker(markers[i]);}

/*
  addMarker ({coord:{lat:-37.840658,lng:145.000981},
              iconImg:'https://img.icons8.com/ios-filled/20/000000/basketball.png',
              content :'<a>traininng</a>'
              })

  addMarker ({coord:{lat:-37.844860,lng:144.990770}});
*/
}
  }


window.initMap = initMap;