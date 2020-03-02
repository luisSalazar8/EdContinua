var p_url = "";
let form_count = Number($("[name=contacto_natural]").val());
$('.select2').select2({
  minimumInputLength: 2,
  language: {

    noResults: function () {
      $(".select2-results__options").append("<a id='pnuevo' class='btn btn-secondary btn-block btn-sm' href='" + p_url + "' target='_blank'>Agregar Nuevo</a>");
      return "No hay resultados";
    },
    searching: function () {

      return "Buscando...";
    },
    inputTooShort: function (e) {
      var t = e.minimum - e.input.length;
      return "Ingresa " + t + " caractéres para buscar";
    }
  }
});

function load_info() {
  var url = $('#form_test').attr("data-info-url");
  var per="";
  var id=0;
  if(flag){
    var id= $('#id_ruc_ci').val();
    if(id==null){
      id=$('#rc').val();
    }
    per="Natural";
    
  }
  else{
    var id= $('#id_ruc_ci').val();
    per="Natural";
    
  }
  $.ajax({
    url: url,
    data: {
      'id': id,
      'persona': "Natural",
    },
    success: function (data) {
      console.log(data)
      flag=false;
      //Para el contacto
      $("#telefono").val(data.telefono);
      $("#celular").val(data.celular);
      $("#email").val(data.email)
      $("#cargo").val(data.cargo)
    }
  })
}

function load_data() {
  var link = $('#form_test').attr("data-persona-url");
  var persona = "Natural";


  if (persona != "") {
    $.ajax({
      url: link,
      data: {
        'persona': persona
      },
      success: function (data) {

        console.log(link)
        $("#id_ruc_ci").html(data.ruc_ci)
        $("#id_razon_nombres").html(data.razon_nombre)
        $('#id_ruc_ci').val($('#rc').val());
        $('#id_razon_nombres').val($('#rn').val());
        $('#id_ruc_ci').trigger('change.select2')
        $('#id_razon_nombres').trigger('change.select2')
      }
    });
    $('#field-razon').show();
    $('#field-ruc-ci').show();


    if (persona == "Natural") {
       $('#ruc_ci').text('CI');
       $('#ra_nom').text('Nombre');
      p_url = $('#form_test').attr("data-natural-url");
    }
    else if (persona == "Jurídica") {
      $('#ruc_ci').text('RUC');
      $('#ra_nom').text('Razón Social');
      p_url = $('#form_test').attr("data-juridica-url");
    }
    $("#contacto").val("");
    $("#telefono").val("");
    $("#direccion").val("");
  }
  else {
    $('#field-razon').hide();
    $('#field-ruc-ci').hide();
  }
};

//Autocompleta de un select a otro usando el id
function autocomplete(from, to) {
  if (from.val() != "") {
    $('#' + to).val($('#' + to + " option[name='" + from.val() + "']").val());
    $('#select2-' + to + '-container').text($('#' + to).val());
  }
  else {
    $('#' + to).val("");
    $('#select2-' + to + '-container').text("---------");
  }
  load_info();
  $("#rc").val($("#id_ruc_ci").val());
  $("#rn").val($("#id_razon_nombres").val());
}



function Agregar_Contacto(){
    $('#agregar_contacto').click(function (e) {
      var valor_cedula = $("#id_ruc_ci").val();
      var valor_nombres = $("#id_razon_nombres").val();
      var telefono = $("#telefono").val();
      var celular = $("#celular").val();
      var email = $("#email").val();
      var cargo = $("#cargo").val();

      if(valor_cedula != null && valor_cedula != ""){
        partes = valor_nombres.split(" ")
        $("#id_ruc_ci").html("");
        $("#id_razon_nombres").html("");

        var nuevo_contacto = $("<tr></tr>")
        nuevo_contacto.addClass("text-center")

        var td_cedula = $("<td></td>").html(valor_cedula)
        var td_nombres = $("<td></td>").html(partes[0] +" " + partes[1])
        var td_apellidos = $("<td></td>").html(partes[2] +" " + partes[3])
        var td_cargo = $("<td></td>").html(cargo)
        var td_telefono= $("<td></td>").html(telefono)
        var td_celular = $("<td></td>").html(celular)
        var td_email = $("<td></td>").html(email)

        var icono = $("<i></i>")
        icono.addClass("fas fa-trash darkgreen-text text-center")
        
        var boton = $("<a></a>").html(icono)
        boton.attr({"boton":"eliminar_tabla"})
        boton.addClass("btn btn-light btn-sm btn-block waves-effect waves-light")
        var td_borrar = $("<td></td>").html(boton)
      
        td_cedula.addClass("td_cedula")
        
        td_cedula.attr("scope","row")
        td_nombres.attr("scope","row")
        td_apellidos.attr("scope","row")
        td_cargo.attr("scope","row")
        td_telefono.attr("scope","row")
        td_celular.attr("scope","row")
        td_email.attr("scope","row")

        td_borrar.attr("scope","row")
        
       

















        nuevo_contacto.append(td_cedula)
        nuevo_contacto.append(td_nombres)
        nuevo_contacto.append(td_apellidos)
        nuevo_contacto.append(td_cargo)
        nuevo_contacto.append(td_telefono)
        nuevo_contacto.append(td_celular)
        nuevo_contacto.append(td_email)
        nuevo_contacto.append(td_borrar)

        
       

       

        $("#dtBasicExample").append(nuevo_contacto)

        
        
        form_count ++;
        
        let element = $("<input type = 'hidden'/>");
        // element.attr('name', 'extra_field_' + form_count);
       
        element.attr('name', 'extra_field_'+ form_count);
        $(element).val(valor_cedula)
        $("#form_test").append(element);

        // build element and append it to our forms container
        
        
        // $("[name=extra_field_1]").val(valor_cedula);
        // increment form count so our view knows to populate 
        // that many fields for validation
     



      }
    });
}


function Guardar(){
    $("#Boton_guardar").click(function (e){
    var CSRFtoken = $('input[name=csrfmiddlewaretoken]').val();
    var atributos_campos = {"nombre":"","ruc":"","direccion":"","telefono":"","celular":"","correo":"","representante":"","maximo_facturas":""};
    var atributos_selec = {"tipo_empresa":"","sector":'',"provincia":"","ciudad":"","forma_pago":""};
    var formulario_campos = $("input[id*='id']");
    var formulario_select = $("option[selected]");
    var indice = 0;
    for(var clave in atributos_campos){
        var valores = $(formulario_campos[indice]).val();
        atributos_campos[clave] = valores ;
        console.log(valores)
        indice+= 1;
    }
    var indice = 0;
    for(var clave in atributos_selec){
        var valores = $(formulario_select[indice]).val();
        atributos_campos[clave] = valores ;
        console.log(valores)
        indice+= 1;
    }
    atributos_campos["csrfmiddlewaretoken"]= CSRFtoken;
    
    
    var cedulas = []
    valores_cedulas = $(".td_cedula");
    
    if(valores_cedulas != " "){
      for(i=0;i<valores_cedulas.length;i++){
          ced = $(valores_cedulas[i]).text();
          cedulas.push(ced)
      }
      for(i=0; i<cedulas.length;i++){
          var c = "cedula "+ String(i);
          atributos_campos[c]=cedulas[i]
      }
    }
    else{
      console.log("vacio")
    }
    console.log(atributos_campos)

    var url = window.location.pathname;

    $.post(url, atributos_campos);
    });
    
}

function Eliminar(){
  //Para los contactos que ya estan guardados
  $("[boton~='eliminar']").click(function(){
    var argumento = $(this).attr("argumento");
    var link = $("#form_test").attr("eliminar-contacto-url");
    $.ajax({
			url: link,
			data: {"contacto": argumento },
			success: function (data) {
				$(".modal-content").html(data);
			}
    });
    
  });


 
}

function Eliminar_Fila_Tabla(){
  $('table').on('click', "[boton~='eliminar_tabla']", function(e){
    $(this).closest('tr').remove()
 })
 

}



  $(document).ready(function () {
    flag=true;
    load_data();
    load_info();
    
    Agregar_Contacto()
    // Guardar()
    Eliminar()
    Eliminar_Fila_Tabla()


  });



$(document).on('change', '#id_tipo_cliente', load_data)

$(document).on('change', '#id_razon_nombres', function () {
  autocomplete($(this), 'id_ruc_ci');
});

$(document).on('change', '#id_ruc_ci', function () {
  autocomplete($(this), 'id_razon_nombres');
});



$("#confirmar_guardar").click(function (e) {
  $.ajax({
    url: $('form_test').attr("data-confirmacion-url"),
    success: function (data) {
      $('.modal-body').html(data);
    },
  });
})

$(document).on('click', "#pnuevo", function () {
  $('#id_ruc_ci').select2('close');
  $('#id_razon_nombres').select2('close');
})

$(document).on('click', "#div_id_ruc_ci span.selection", function (e) {
  $("#rc").val("");
  $("#rn").val("");
  load_data();
});

$(document).on('click', "#div_id_razon_nombres span.selection", function (e) {
  $("#rc").val("");
  $("#rn").val("");
  load_data();
});
