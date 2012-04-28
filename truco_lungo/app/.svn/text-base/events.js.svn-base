App.Events = (function(lng,app, undefined) {

//TODO: Al volver atrás del mapa, borramos los eventos
/***************************************************
    main
*****************************************************/
    /*
        Evento al pulsar el menú listas
    */
    lng.dom('#GoListas').tap(function(event){
            App.Data.listas();
    });

    /*
        Al pulsar atras en la lista de la compra, modificamos
        el contador de esa lista
    */
    lng.dom('#detalleCompra header a').tap(function(event){
        App.Data.listas();
    });

/**************************************************
    listas
*************************************************+/
    /*
        Evento al pulsar el boton + en la seccion listas
        Ir al formulario para añadir listas
    */
    lng.dom('#GoAddLista').tap(function(event){
       //chapuza para poder ir al formulario
        lng.Router.section('forms');
        App.View.cambiaTituloSection('forms','Nueva Lista');
        lng.Router.article('forms','nuevaLista');
    });
    //Evento para ver el mapa
    lng.dom('#GoComprar').tap(function(event){
        App.Mapas.iniciar();
        App.View.cambiaTituloSection('mapas','Mapa de la compra');
        lng.Router.section('mapas');
        lng.Router.article('mapas','map');
        //App.Mapas.verMapa();
    });



    /*
        Al pulsar una lista, mostramos los detalles de la misma
    */
    lng.dom('#item_lista.list.scrollable.current').tap(function(event){
        //Guardamos en cache los datos de la lista
        var id_lista = lng.dom(this).attr('id');
        lng.Data.Cache.set('id_lista', {id_lista:id_lista});
        App.Data.productosLista(id_lista);
        lng.Router.section('detalleCompra');
        //TODO: buscar el nombre de la lista para ponerlo
        App.View.cambiaTituloSection('detalleCompra','Lista: '+id_lista);
    });
    /*
        Al pulsar largo una lista, me muestra un menu growl
        Actualmente no funciona.. cambiamos a tap
    */
    
    lng.dom('#item_lista.list.scrollable.current').longTap(function(event){
        //Guardamos en cache los datos de la lista
        var id_lista = lng.dom(this).attr('id');
        lng.Data.Cache.set('id_lista', {id_lista:id_lista});
        App.Notificaciones.menuLista(id_lista);
    });
   
    /*
        Crear nueva lista
        Entrada: nombre, comentario
        Salida:mensaje error o lista creada
    */
    lng.dom('#btnNuevaLista').tap(function(event) {
        nombre = lng.dom('#nombreLista').val();
        comentario = lng.dom('#descriptLista').val();
        datos={};
        if (App.Data.validarLista(nombre,comentario) == true)
        {
            if (comentario != '') //No sé por qué vacío ocupa un caracter
            {
                datos.comentario = comentario
            }
            datos.nombre=nombre;
            datos.estado=0;
            datos.fecha=Date('now');
            App.Data.insert('lista',datos);
             //Actualizamos el contador de listas.. No se actualiza, y no se por qué
            //Para actualizarlo, cogemos su actual valor y le sumamos uno

            App.Data.listas();
            App.Data.contadorListas();
            App.View.returnToMain("Creando la lista...", "loading");


        }
     });    
    /*
        Editar lista
    */
    lng.dom('#btnEditLista').tap(function(event) {
        //Como tenemos la lista en cache, simplemente sacamos los datos
        lista = lng.Data.Cache.get('current_lista');
        nombre = lng.dom('#editNombreLista').val();
        comentario = lng.dom('#editDescriptLista').val();        //Validamos los datos
        datos = {};
        if (App.Data.validarLista(nombre,comentario) == true)
        {
            datos.nombre = nombre;
            if (comentario != "")
            {
                datos.comentario = comentario;
            }    
            else 
            {
                datos.comentario = null;
            }      
            App.Data.update('lista',datos,{id_lista : lista.id_lista});
            App.View.returnToMain("Actualizando lista...", "loading");
        }
    });
/*********************************************************
    productos
**********************************************************/
    /*
        Cuando introducimos un nombre busca las categorias asociadas
    */
    lng.dom('#nombreProducto').on('change',function(){
        //Todo: responder, cargar y habilitar los selects
        App.Data.cargarCategorias(lng.dom('#nombreProducto').val());
    });

    /*
        Cuando introducimos un nombre busca las categorias asociadas
    */
    lng.dom('#editNombreProducto').on('change',function(){
        //Comprobamos la categoria que tenemos hasta ahora
        cat = lng.dom('#editCategoria').val();
        App.Data.cargarCategorias(lng.dom('#editNombreProducto').val());
        /*
        TODO:
            Si encontramos la categoria actual entre las categorias recien cargadas
            le asignamos el mismo valor
        */
        

    });
    /*
        Editar la lista
    */
    lng.dom('#GoEditar').tap(function(event) {
        //Cargamos los datos de la lista en cache
        lista = lng.Data.Cache.get('current_lista');
        App.View.editLista(lista);
    });


    /*
        Añadir un nuevo producto
    */
    lng.dom('#btnNuevoProducto','#btnNuevoProducto2').tap(function(event){
        nombre=lng.dom('#nombreProducto').val();
        categoria=lng.dom('#categoria').val();
        marca=lng.dom('#marca').val();
        cantidad=lng.dom('#cantidad').val();
        //alert('Nombre: '+nombre+" categoria: "+categoria+" marca: "+marca+" cantidad:"+cantidad);
        if (App.Data.validarProducto(nombre,categoria,marca,cantidad))
        {
            //Cargamos el id de la lista
            var datos = {};
            lista=lng.Data.Cache.get('id_lista');
            datos.id_lista=lista.id_lista;
            datos.nombre = nombre;
            datos.cantidad=cantidad;
            datos.categoria=categoria;
            if (marca != ''){datos.marca=marca;}
            //Insertamos, volvemos y refrescamos los datos
            App.Data.insert('producto',datos);
            App.Data.productosLista(datos.id_lista);
            App.View.returnToMain("Añadiendo producto...","loading");
            
        }
    });


    /*
        Boton añadir producto
    */
    lng.dom('#GoNuevoProducto').tap(function(event){
       //chapuza para poder ir al formulario
        lng.Router.section('forms');
        App.View.cambiaTituloSection('forms','nuevo producto');
        lng.Router.article('forms','nuevoProducto');
    });    

    /*

    */
    lng.dom('#btnEditarProducto').tap(function(event){
        nombre=lng.dom('#editNombreProducto').val();
        //BUG: no cambia el valor de categoria :S
        categoria=lng.dom('#editCategoria').val();
        marca=lng.dom('#marca').val();
        cantidad=lng.dom('#editCantidad').val();
         //alert('Nombre: '+nombre+" categoria: "+categoria+" marca: "+marca+" cantidad:"+cantidad);

        if (App.Data.validarProducto(nombre,categoria,marca,cantidad))
        {
         //alert('Nombre: '+nombre+" categoria: "+categoria+" marca: "+marca+" cantidad:"+cantidad);
          //Cargamos el id de la lista
            var datos = {};
            lista=lng.Data.Cache.get('id_producto');
            datos.nombre = nombre;
            datos.cantidad=cantidad;
            datos.categoria=categoria;
            if (marca != ''){datos.marca=marca;}
            //Insertamos, volvemos y refrescamos los datos
            where={
                id_lista : lista.id_lista,
                id_producto : lista.id_producto
            };
            App.Data.update('producto',datos,where);
            App.Data.productosLista(lista.id_lista);
            App.View.returnToMain("Actualizando producto...","loading");      
        }


    });

    /*
        Evento para cuando se cambia el valor de categoria
    */
    lng.dom('#categoria').on('change',function(){
        //Cambia el valor para nuevoProducto, pero no para editarProducto
        // :S
        //alert("cambiando categoria a "+lng.dom('#categoria').val());
    });

    lng.dom('#editCategoria').on('change',function(){
        //Cambia el valor para nuevoProducto, pero no para editarProducto
        // :S
        //alert("cambiando editCategoria a "+lng.dom('#editCategoria').val());
    });
    /*
    */
    lng.dom('#listaProductos li').tap(function(event){
        //Guardamos en cache los datos de la lista
        var split_id = lng.dom(this).attr('id').split('-');
        id_lista=split_id[0];
        id_producto=split_id[1];
        lng.Data.Cache.set('id_producto', {id_lista:id_lista,id_producto:id_producto});
        App.Notificaciones.menuProducto(id_lista,id_producto);
    });
    lng.dom('#btnInstructions').tap(function(event){
        App.Mapas.miRuta();
    });

/*
Eventos de mapas
*/
        //Posicionar al usuario (con un marcador)
        LUNGO.dom('#buscame').tap(function(event) {
        });

        LUNGO.dom('#cleanMarker').tap(function(event) {
           // App.Mapas.borrarMarcadores();
        });

})(LUNGO);
