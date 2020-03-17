console.log(localStorage.getItem("codigoevento"));
console.log($("#id_cod_evento").val());
if($("#id_cod_evento").val()==""){
    const ce=localStorage.getItem("codigoevento");
  $("#id_cod_evento").val(ce);

  $("#id_nombre_evento").val(ce);

  $("#id_valor_evento").val(ce);

}

$("#id_cod_evento").prop("disabled",true);


$("#id_nombre_evento").prop("disabled",true);


$("#id_valor_evento").prop("disabled",true);


$(document).on('click', '#hack', function () {
    
    $("#id_cod_evento").prop("disabled",false);

    $("#id_nombre_evento").prop("disabled",false);

    $("#id_valor_evento").prop("disabled",false);
    const valmee=$("#id_valor_evento").val();
    $("#id_valor_evento").attr("type","number");
    $("#id_valor_evento").val(parseFloat(valmee.replace(/,/g,"")));
    $("#id_valor_evento").val(parseFloat($("#id_valor_evento").val()).toFixed(2));


    const val=$("#id_valor").val();
    $("#id_valor").attr("type","number");
    $("#id_valor").val(parseFloat(val.replace(/,/g,"")));
    $("#id_valor").val(parseFloat($("#id_valor").val()).toFixed(2));

  });