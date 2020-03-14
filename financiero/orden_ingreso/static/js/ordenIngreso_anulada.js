function Ocultar(){
    var estado = $('input#id_estado');
    var boton_anulado = $('a#anular_orden_ingreso')

    var numero_tramite = $('input#id_n_tramite');
    var fecha_tramite = $('input#id_fecha_tramite');
    var fecha_pago = $('input#id_fechaPago');
    var anexo = $('input#id_anexo');

    var campos = [numero_tramite,fecha_tramite,fecha_pago];

    if ($(estado).val()=="ANLD"){
       campos.forEach(function(value,index){
          $(campos[index]).attr('readonly',"True");
       });

       //Para el anexo no funciona el readonly, es necesario usar disabled
       $(anexo).attr('disabled',"");
       $(boton_anulado).remove();
    }
    
  }
  $(document).ready(function () {
      Ocultar();
  });