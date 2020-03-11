//Cambiar el signo de dolar
var valor=$("#div_id_valor");
var inp=$("#div_id_valor input");
var hijos=valor.children();
const dnuevo=hijos[1];
console.log(dnuevo);
dnuevo.remove();
const dollar=$("<div>");
dollar.attr("class","input-icon")
const icono=$("<i>");
icono.text("$");
dollar.append(inp);
dollar.append(icono);
valor.append(dollar);

//Funcion para establecer Formato de Dinero
function transform(input){
    if($(input).val()!=""){
      $(input).val(parseFloat($(input).val()).toFixed(2));
    $(input).attr("type","text");
    console.log($(input).val())
    var numeroe=$(input).val().split(".")
    const long= numeroe[0].length;
    console.log(long)
    var newnum="";
    cont=0;
    for(var i=(long-1);i>=0;i--){
          if(cont%3==0 && cont!=0){
            newnum=numeroe[0].charAt(i)+","+newnum;
            console.log("coma");
            console.log(i);
            console.log(numeroe[0].charAt(i));
            cont+=1;
          }else{
            console.log("no coma");
            console.log(i);
            console.log(numeroe[0].charAt(i));
            newnum=numeroe[0].charAt(i)+newnum;
            cont+=1;
          }
    }
    console.log(newnum+"."+numeroe[1]);
    $(input).val(newnum+"."+numeroe[1]);
    }
    
  }



  //Una vez listo el documento
  $(document).ready(function () {
    var input = $("#id_valor");

    if($(input).val()!=""){
        transform($(input));
      }
      
      $(input).focusout(function() {
        transform($(this));
      })
      $(input).focus(function() {
      const val=$(this).val();
      $(this).attr("type","number");
      $(this).val(parseFloat(val.replace(/,/g,"")));
      $(this).val(parseFloat($(this).val()).toFixed(2));
      })
  });