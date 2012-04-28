	App.Services = (function(lng, App, undefined) {
	/*
		TODO
		cargamos el servicio de obtener las categorias desde el servidor
	*/
	var serviceCategorias = function(nombre)
	{
		categoria = [];
		categoria.push("");
		categoria.push('categoria1');
		categoria.push('categoria2');
		return categoria;
		/*
		//Hacemos la peticion rest
		url ="http://127.0.0.1:8000/carga_categorias/";
		lng.Services.get(url,
		{
			nombre : nombre
		},
		function (response){
			console.error(response);
		}
		);*/
	};
	var serviceMarcas = function(nombre,categoria)
	{
		//Hacemos la peticion rest
		url ="http://127.0.0.1:8000/carga_categorias/";
		lng.Services.get(url,
		{
			nombre : nombre
		},
		function (response){
			console.error(response);
		}
		);
	};
    return {
		serviceCategorias: serviceCategorias,
		serviceMarcas: serviceMarcas
    };

})(LUNGO, App);
