//seccion de signo de dolar
var monto=$("#div_id_monto_propuesta");
var inp=$("#div_id_monto_propuesta input");
var hijos=monto.children();
const dnuevo=hijos[1];
dnuevo.remove();
const dollar=$("<div>");
dollar.attr("class","input-icon")
const icono=$("<i>");
icono.text("$");
dollar.append(inp);
dollar.append(icono);
monto.append(dollar);


var utilidad=$("#div_id_utilidad_esperada");
var inpu=$("#div_id_utilidad_esperada input");
var hijosu=utilidad.children();
const dnuevou=hijosu[1];
dnuevou.remove();
const dollaru=$("<div>");
dollaru.attr("class","input-icon")
const iconou=$("<i>");
iconou.text("$");
dollaru.append(inpu);
dollaru.append(iconou);
utilidad.append(dollaru);