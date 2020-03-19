
$(document).on('click', '#add', function () {
    var extra=$("#codigoe").val();
    localStorage.setItem("codigoevento",extra);
    
});

$(document).on('click', '#cancelar', function () {
  localStorage.removeItem("codigoevento");
  
});

$(document).on('click', '#guardar', function () {
  localStorage.removeItem("codigoevento");
  
});

if(localStorage.getItem("codigoevento")!=null){
  $("#codigoe").val(localStorage.getItem("codigoevento"));
}



  