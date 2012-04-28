App.View = (function(lng, App, undefined) {
	/*
        Conjunto de listas de la compra.
        Todo: numero de productos de la lista
    */
	lng.View.Template.create(
	'listas-tmp',
	'<li id="{{id_lista}}">\
		<a href="#">\
		{{nombre}}\
        <span class="bubble count onright">{{contador}}</span>\
		<small>{{comentario}}</small>\
		</a>\
		</li>'
	);

    /*
        Conjunto de listas de la compra.
        Todo: numero de productos de la lista
    */
    lng.View.Template.create(
        'productos-tmp',
        '<li id="{{id_lista}}-{{id_producto}}">\
            <a href="#">\
            <span>{{nombre}}\
                <span>{{categoria}}</span>\
                <span>{{marca}}</span>\
                <span class="bubble count onright">{{cantidad}}</span>\
            </span>\
            </a>\
            </li>'
    );

    var cambiaTituloSection=function (section,titulo)
    {
        lng.dom('section#'+section+' span.title').html(titulo);    
    }  
    /*
    	Muestra el menú para una lista en concreto
    	//Muestra un mensaje de lista creada, y va hacia la sección dedicada a usar las listas
    	//var listaCreada = function
    */
    var returnToMain = function(message, icon) {
        lng.Sugar.Growl.show('Cargando ...',message, icon, true, 2);
        lng.Router.back();
    };

    var list = function(container, template, rows) {
        lng.View.Template.List.create({
            container_id: container,
            template_id: template,
            data: rows
        });
       // lng.View.Element.count('a[href="#' + container + '"]', rows.length);
    };

    /*
        Editar listas
    */
     var editLista = function(id) {
        lng.Data.Sql.select('lista', {id_lista:id}, function(result){
            if (result.length > 0) {

                var data = result[0];
                lng.Data.Cache.set('current_lista', data);
                lng.Router.section('forms');
                lng.Router.article('forms','editarLista');
                cambiaTituloSection('forms','Editando '+data.nombre)
                lng.dom('#editNombreLista').val(data.nombre);
                lng.dom('#editDescriptLista').val(data.comentario);
           }
        });
    }; 
    /*
        Editar productos. Actualiza los datos de la vista de productos
        TODO: permitir cambiar la lista
    */
    var editProducto = function (id){
        lng.Data.Sql.select('producto', {id_producto:id}, function(result){
            if (result.length > 0) {
                var data = result[0];
                lng.Router.section('forms');
                lng.Router.article('forms','editarProducto');
                cambiaTituloSection('forms','Editando producto');
                console.error("Nombre: "+data.nombre+" categoria: "+data.categoria+" cantidad: "+data.cantidad);
                 //rellenamos los select y marcamos el que tenemos seleccionado
                // Categoria debe estar relleno siempre
                //Marca puede tener ""
                lng.dom('#marca').val(data.marca);
                lng.dom('#editNombreProducto').val(data.nombre);
                //BUG: no carga la cantidad correcta (de hecho no marca nada)

                lng.dom('#editCantidad').val(""+data.cantidad);
                App.Data.cargarCategorias(data.nombre);
                lng.dom('#editCategoria').val(data.categoria);

           }
        });
    };

    return{
        returnToMain: returnToMain,
        list: list,
        editLista : editLista,
        editProducto : editProducto,
        cambiaTituloSection : cambiaTituloSection,
    };

})(LUNGO, App);