const marcarEntradaSalida = async (parametro)=>{

    var formData = new FormData();
    formData.append("csrfmiddlewaretoken", csrf_token);
    formData.append("accion", parametro);
      // Obtener la hora actual
    var fecha = new Date();
    var hora = fecha.getHours();
    var minutos = fecha.getMinutes();
    var segundos = fecha.getSeconds();

    // Agregar la hora actual al FormData
    formData.append("hora", hora + ":" + minutos + ":" + segundos);

    var year = fecha.getFullYear();
    var month = fecha.getMonth() + 1; // Los meses van de 0 a 11, por lo tanto se suma 1
    var day = fecha.getDate();
  
    // Formatear la fecha en el formato deseado (ejemplo: AAAA-MM-DD)
    var fechaFormateada = year + "-" + month.toString().padStart(2, "0") + "-" + day.toString().padStart(2, "0");
  
    // Agregar la fecha actual al FormData
    formData.append("fecha", fechaFormateada);

    const url = urlPOST;
    const fetchUrl = await fetch(url, {
        method: "POST",
        body: formData,
    });
    const response = await fetchUrl.json();
    if (response.success) {
        KTApp.unblock('#bloque-principal')      
        Swal.fire({
        title: "Exito!",
        text: response.msg,
        icon: "success",
        buttonsStyling: false,
        confirmButtonText: "Aceptar",
        customClass: {
            confirmButton: "btn font-weight-bold btn-primary",
        },
        }).then((result) => {
        });
    } else {
        KTApp.unblock('#bloque-principal')      
        Swal.fire({
        title: "Error!",
        text: response.msg,
        icon: "error",
        buttonsStyling: false,
        confirmButtonText: "Aceptar",
        customClass: {
            confirmButton: "btn font-weight-bold btn-light",
        },
        });
    }
}

$('#btn-entrada').on('click', function(){
    marcarEntradaSalida('entrada')
})

$('#btn-salida').on('click', function(){
    marcarEntradaSalida('salida')
})

var table = $('#tabla_marcaciones').DataTable({
    serverSide: true,
    scrollX: true,
    pageLength: 50,
    paging:true,
    sAjaxSource: urlDatosEmpleado,
    sServerMethod: "POST",
    columnDefs: [
        {
            "targets": '_all',
            "className": "text-center",
        }
    ],  
    columns: [
            { data: 0, name: 'identificacion'},
            { data: null, name: 'nombre',
                render: function(data, type, row, meta) {
                    return  `${data[1]} ${data[2]? data[2]:''}`
                }
            },
            { data: 3, name: 'hora_entrada'},  
            { data: 4, name: 'fecha_entrada'},  
            { data: 5, name: 'hora_salida'},
            { data: 6, name: 'fecha_salida'},
    ],
})
