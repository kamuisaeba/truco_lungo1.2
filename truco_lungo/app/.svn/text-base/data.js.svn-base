App.Data = (function(lng, undefined) {
	//CONFIG: Data.Sql vamos incorporando las tablas de truco
	lng.Data.Sql.init(
	{
		name: 'bd_truco',
		version: '0',
		schema: [
			{
				name:'lista', 
				drop: false, 
				fields: 
				{
					id_lista: 'INTEGER PRIMARY KEY',
					nombre: 'TEXT not null',
					comentario: 'TEXT default null',
					estado: 'INTEGER DEFAULT 0',
					fecha: 'DATETIME',
					usuario: 'INTEGER' // Usuario propietario de la lista 
				}
			},
			{
				name: 'producto', 
				drop: false, 
				fields:
				{
					id_lista : 'integer',
					id_producto: 'INTEGER PRIMARY KEY',
					nombre: 'TEXT not null',
					categoria: 'TEXT',
					marca: 'TEXT',
					cantidad: 'integer'
				}
			},
		]
	});
/*
		Devolvemos todos los productos de una lista de la compra
	*/
	var productosLista= function(id){
		//select =" SELECT * FROM producto WHERE producto_lista.id_lista ="+id;
		//lng.Data.Sql.execute(select,function(result)
		lng.Data.Sql.select('producto',{id_lista : id},function(result){
			parameters = {
				el: '#listaProductos',
				template: 'productos-tmp',
				data: result
			};
			lng.View.Template.List.create(parameters);
		});
	 };
/*
		Contamos el numero de listas del sistema para mostrarlo
		en un boton.
	 */
	/*
		Iniciamos el boton con contador.
		Esto genera un <span class='bubble count'>valor</span>
		El cual no se actualiza. pero ya está soluciona con la función contadorListas()
	*/
	var IniciarContadorLista = function (){
		lng.Data.Sql.select('lista',null,function(result){
		lng.View.Element.count("#GoListas",result.length);
		});		
	};

	/*
		Actualiza el valor del contador con el selector que se genera
	*/
	var contadorListas = function () {
		lng.Data.Sql.select('lista',null,function(result){
			//console.error(lng.dom('#GoListas span'))
			//lng.dom('#GoListas span.bubble.count').html(""+result.length);
			if (result.length == 1){
				lng.View.Element.count("#GoListas",result.length);
			}
			lng.dom('#GoListas span.bubble.count').html(""+result.length);
		});
	};

	/*
		Cargamos las options del select categorias
	*/
	var cargarCategorias=function(nombre){
		res=App.Services.serviceCategorias(lng.dom('#nombreProducto').val());
        var msg="";
        //rellenamos los select
        for (i=0;i<res.length;i=i+1)
        {
            msg=msg+'<option>'+res[i]+'</option>';
        }
            lng.dom('select#categoria,select#editCategoria').html(msg);
      }
/*
		Devolvemos todas las listas del sistema
		//Todo: devolver un contador de los productos que hay en la lista
	*/
	var listas = function (){
		lng.Data.Sql.execute('select lista.id_lista,nombre,comentario, (select count(id_producto) from producto where producto.id_lista= lista.id_lista) as contador from lista',function(result){
			datos = [];
			for (i=0;i<result.rows.length;i=i+1){
				datos[i] ={
					nombre: result.rows.item(i).nombre,
					comentario:result.rows.item(i).comentario,
					id_lista:result.rows.item(i).id_lista,
					contador: result.rows.item(i).contador
				};
			}
			//console.error(result.rows.item);
			parameters = {
			el: '#item_lista',
			template: 'listas-tmp',
			data: datos
		};
		lng.View.Template.List.create(parameters);
		});		
	}; 
/*
	 insertamos una nueva lista
	*/
	var insert= function(tabla,data){
		lng.Data.Sql.insert(tabla,data);

	};
	
	/*
		Actualizamos la tabla
		@param {tabla} Tabla a actualizar
		@param {data} los datos a actualizar
		@param {where} where del update
	*/
	var update = function (tabla,data,where) {
		lng.Data.Sql.update(tabla,data,where);
	};
/*
		borrar la tabla
		@param {tabla} tabla a borrar
		@param {where} condiciones para borrar
	*/
	var remove = function (tabla,where){
		lng.Data.Sql.drop(tabla,where);
		contadorListas();
	};


/*
		si es válido, devolvemos true
		Si no, devolvemos false
	*/
	var validarLista = function(nombre,comentario)
	{
		//lng.Core.log("1","nombre: "+nombre+" comentario: "+comentario);
		var mensaje ="";
		if (nombre == '')//nombre es obligatorio
		{
			mensaje = mensaje + " \nEl campo nombre debe estar relleno";
			//mostramos el growl si falla
			lng.Sugar.Growl.notify("Error", mensaje, 'warning','error',2);
			return false;
		}
		return true;
	};

	/*
		Validar el formulario de productos
		@param {nombre} nombre del producto. Required
		@param {categoria} categoria del producto. Required
		@param {marca} marca del producto. Optional
		@param {cantidad} cantidad a comprar. Optional
	*/
	var validarProducto = function (nombre,categoria,marca,cantidad)
	{
		var res=true;
		var mensaje = "";
		if (nombre == '')
		{	
			mensaje = mensaje + " \nEl campo nombre debe estar relleno";
			res=false;
		}
		if (categoria == "")
		{
			mensaje = mensaje + "\nLa categoría debe estar rellena";
			res=false;
		}
		if (res == false)
		{
			lng.Sugar.Growl.notify("Error", mensaje, 'warning','error',2);
		}
		return res;
	}


	IniciarContadorLista();
	return {
		listas: listas, //listas de la compra que hay en el sistema
		insert: insert, //Insertar productos o listas en el sistema
		remove: remove, // Borra productos o listas
		update: update, // edita productos o listas
		productosLista : productosLista,
		validarLista: validarLista,
		validarProducto : validarProducto,
		cargarCategorias: cargarCategorias,
		contadorListas:contadorListas,
	};

})(LUNGO, App);
