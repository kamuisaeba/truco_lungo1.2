//Clase para las notificaciones sugar. Actualmente no se usa
App.Notificaciones = (function(lng, App,undefined) {

	var notificacionError = function (titulo,mensaje,icono,tiempo){};
	var mensajeOk = function(){};

 
	/*
		Menu para las listas
		@param idlista es el id de la lista pulsada       
	*/
    var menuLista = function(id_lista){
    	options = [
            {
                name : 'Ir',
                icon : 'file',
                callback : function (){
                    App.Data.productosLista(id_lista);
                    lng.Router.section('detalleCompra');
                    //TODO: buscar el nombre de la lista para ponerlo

                    lng.dom('section#detalleCompra span.title').html('Lista: '+id_lista);    
                    lng.Sugar.Growl.hide();
                }
            },
           {
               //2ª opcion para editar una lista
                name: 'Editar',
                icon: 'pencil',
                callback: function(){
                    lng.Sugar.Growl.hide();
                    App.View.editLista(id_lista);
                }
            },
            {
                name: 'Borrar',
                icon: 'trash',
                callback: function(){
                    seguro('lista',{id_lista:id_lista});

                }
            },
            {
                name: 'Cancelar.',
                icon: 'close',
                callback: function() {
                    lng.Sugar.Growl.hide();
                }
            }
        ];
        lng.Sugar.Growl.option('MENÚ LISTA', options);
	};

	var menuProducto = function (id_lista,id_producto){
        var options = [
           {
                name: 'Editar',
                icon: 'pencil',
                callback: function(){
                    lng.Sugar.Growl.hide();
                    App.View.editProducto(id_producto);
                }
            },
            {
                name: 'Borrar',
                icon: 'trash',
                callback: function(){
                    seguro('producto',{id_lista:id_lista,id_producto:id_producto},id_lista);

                }
            },
            {
                name: 'Cancelar.',
                icon: 'close',
                callback: function() {
                    lng.Sugar.Growl.hide();
                }
            }
        ];
        lng.Sugar.Growl.option('MENÚ PRODUCTOS', options);		
	};

    var menuMarcador=function(marker){
        var options = [
                {
                    name:"Borrar",
                    icon:"trash",
                    callback: function(){
                        App.Mapas.borrarMarcador(marker);
                    }
                },
                {
                name: 'Cancelar.',
                icon: 'close',
                callback: function() {
                    lng.Sugar.Growl.hide();
                }
            }
        ];
        lng.Sugar.Growl.option('MENÚ MAPAS', options);  
    };

/*
    Pregunta si borrar o no
*/
    var seguro = function(tabla,where,id_lista) {
        var options = [
            {
                name: '...Sí, Borrar!',
                icon: 'check',
                color: 'green',
                callback: function(){
                    App.Data.remove(tabla,where);
                    //Actualizamos las listas
                    if (tabla=='producto')
                        App.Data.productosLista(id_lista);

                    if (tabla=='lista'){
                        App.Data.listas();
                        App.Data.contadorListas();
                    }            
                    lng.Sugar.Growl.hide(); 
                }
            },
            {
                name: '...No.',
                icon: 'close',
                color: 'red',
                callback: function() {
                    lng.Sugar.Growl.hide();
                }
            }
        ];
        lng.Sugar.Growl.option('¿Borrar?', options);
    };


	return {
		menuLista : menuLista,
		menuProducto: menuProducto,
		seguro : seguro,
        menuMarcador: menuMarcador,
	};
})(LUNGO,App);