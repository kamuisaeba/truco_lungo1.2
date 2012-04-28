App.Mapas = (function(lng, App, undefined) {

        var _to = {};
        var _mipos={};//mi posicion
        var _map =null; //Instancia del mapa
        var _marcadores = new Array();
    var geoposicion = function (longitude,latitude){
        if (longitude && latitude){
            _mipos.latitude = latitude;
            _mipos.longitude = longitude;
        }
        else{
            if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(function(position) {
                alert("posicionando");
                        _mipos.latitude = position.coords.latitude;
                        _mipos.longitude = position.coords.longitude;
                    });
            }
            else {alert("no puedes geolocalizr");}
        }
    };
    var getPosicion = function (){
        //Hay que convertirlo a un valor de google valido
        return _mipos;
    };
       // var _to = { latitude: 59.327383, longitude: 18.06747 };
    var verMapa = function (){
        //    LUNGO.Sugar.GMap.center(_mipos);
    };
    var marcador = function (latlng){    
            var myMarkerLatLng = new CM.LatLng(latlng.lat(),latlng.lng());
            var myMarker = new CM.Marker(myMarkerLatLng, {
                title: "This is the Village of Naurod"
            });
            _map.setCenter(myMarkerLatLng, 14);
            _map.addOverlay(myMarker);
            _marcadores.push(myMarker);
            CM.Event.addListener(myMarker,'click',function(latlng){
                //App.Notificaciones.menuMarcador(myMarker);
            });
    };
    var iniciar= function(){
        var cloudmade = new CM.Tiles.CloudMade.Web({key: '8ee2a50541944fb9bcedded5165f09d9'});
        _map = new CM.Map('map_div', cloudmade);
        _map.setCenter(new CM.LatLng(51.514, -0.137), 15);
        CM.Event.addListener(_map, 'click', function(latlng) {
            marcador(latlng);
        });
    };
    var miRuta = function(){
        //TODO: que sea una lista scrollable
        var directions = new CM.Directions(_map, 'instrucciones', '8ee2a50541944fb9bcedded5165f09d9');
        var waypoints = [];
        var i;
        for (i=0;i<_marcadores.length;i=i+1){
            var location=_marcadores[i].getLatLng();
            waypoints.push(location);
        };
    // = [new CM.LatLng(51.52039, -0.1485), new CM.LatLng(51.5203, -0.135)];
        directions.loadFromWaypoints(waypoints);        
    };

    //Aun no funciona :S
    var borrarMarcador= function(marker){
        console.error(marker);
        _map.removeOverlay(marker);
    };
	return {
        geoposicion : geoposicion,
        verMapa : verMapa,
        getPosicion: getPosicion,
        marcador: marcador,
        iniciar: iniciar,
        miRuta: miRuta,
        borrarMarcador: borrarMarcador
	};
})(LUNGO,App);