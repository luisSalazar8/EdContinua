console.log(localStorage.getItem("codigoevento"));

const ce=localStorage.getItem("codigoevento");
$("#id_cod_evento").val(ce);
$("#id_cod_evento").prop("disabled",true);

$("#id_nombre_evento").val(ce);
$("#id_nombre_evento").prop("disabled",true);

$("#id_valor_evento").val(ce);
$("#id_valor_evento").prop("disabled",true);


$(document).on('click', '#hack', function () {
    
    $("#id_cod_evento").prop("disabled",false);

    $("#id_nombre_evento").prop("disabled",false);

    $("#id_valor_evento").prop("disabled",false);
    
  });