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