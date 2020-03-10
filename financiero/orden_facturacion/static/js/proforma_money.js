//seccion de signo de dolar
var monto=$("#div_id_montoDesc");
var inp=$("#div_id_montoDesc input");
var hijos=monto.children();
var d=hijos[1];
d.remove();
var dollar=$("<div>");
dollar.attr("class","input-icon")
var icono=$("<i>");
icono.text("$");
dollar.append(inp);
dollar.append(icono);
monto.append(dollar);

//seccion de signo de dolar
var montou=$("#div_id_montoProforma");
var inpu=$("#div_id_montoProforma input");
var hijosu=montou.children();
var du=hijosu[1];
du.remove();
var dollaru=$("<div>");
dollaru.attr("class","input-icon")
var iconou=$("<i>");
iconou.text("$");
dollaru.append(inpu);
dollaru.append(iconou);
montou.append(dollaru);

//seccion de signo de dolar
var montoa=$("#div_id_montoAceptado");
var inpa=$("#div_id_montoAceptado input");
var hijosa=montoa.children();
var da=hijosa[1];
da.remove();
var dollara=$("<div>");
dollara.attr("class","input-icon")
var iconoa=$("<i>");
iconoa.text("$");
dollara.append(inpa);
dollara.append(iconoa);
montoa.append(dollara);

//seccion de signo de dolar
var montoe=$("#div_id_montoPorEjecutarse");
var inpe=$("#div_id_montoPorEjecutarse input");
var hijose=montoe.children();
var de=hijose[1];
de.remove();
var dollare=$("<div>");
dollare.attr("class","input-icon")
var iconoe=$("<i>");
iconoe.text("$");
dollare.append(inpe);
dollare.append(iconoe);
montoe.append(dollare);

//seccion de signo de dolar
var montoeo=$("#div_id_montoEjecutado");
var inpeo=$("#div_id_montoEjecutado input");
var hijoseo=montoeo.children();
var deo=hijoseo[1];
deo.remove();
var dollareo=$("<div>");
dollareo.attr("class","input-icon")
var iconoeo=$("<i>");
iconoeo.text("$");
dollareo.append(inpeo);
dollareo.append(iconoeo);
montoeo.append(dollareo);

//para poder controlar las versiones
const ver=parseInt($("#id_version").val());
if($("#ac").val()=="True"){
  $(document).on('change', "#id_version", function (e) {
    const veract=parseInt($("#id_version").val());
    if(veract>(ver+1)){
      $(this).val(ver+1)
    }else if(veract<ver){
      $(this).val(ver)
    }
  });
}else{
  $("#id_version").prop('disabled', true);
}