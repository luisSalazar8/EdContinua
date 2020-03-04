/**
 * Funcion para calcular los valores de ingresos
 */
function CalcularIngresos() {
  var valor_u = $("#id_ingreso_individual_sin_desc").val();
  var n_participantes = $("#id_n_participantes").val();
  var sin_descuento_total = valor_u * n_participantes;
  var descuento_individual = $("#id_descuento_maximo").val() / 100 * valor_u;
  var descuento_total = descuento_individual * n_participantes;
  var egresos = $('#id_total_egresos').val();
  var ingreso_total = sin_descuento_total - descuento_total;
  var utilidad = ingreso_total - egresos
  $('#id_utilidad').val(utilidad.toFixed(2));
  $("#id_margen_contribucion").val((utilidad / ingreso_total).toFixed(2))
  $('#id_ingreso_total_sin_desc').val(sin_descuento_total.toFixed(2));
  $('#id_descuento_individual').val(descuento_individual.toFixed(2));
  $('#id_descuento_total').val(descuento_total.toFixed(2));
  $('#id_ingreso_neto_individual').val((valor_u - descuento_individual).toFixed(2)).trigger('change');
  $('#resumen_precio_evento').val((valor_u - descuento_individual).toFixed(2)).trigger('change');
  $('#id_ingreso_neto_total').val(ingreso_total.toFixed(2));
  $('#resumen_ingreso').val(ingreso_total.toFixed(2));

  CalcularHonorarios();
}


/**
 * Funcion que hace un requerimiento ajax al servidor para obtener los valores unitarios del tarifario y calcular
 * @param {*} modelo Representa el nombre de la fk en el modelo de PresupuestoEvento
 * @param {*} id Represeta la pk de la fk del cual el valor se va a buscar
 */
function CargarInfo(modelo, id) {
  var url = $('form').attr("data-info-url");
  $.ajax({
    url: url,
    data: {
      'modelo': modelo,
      'id': id,
    },
    success: function (data) {
      $('#id_' + modelo + '_unitario').val(+data.costo).trigger('change');
    }
  })
}

function CargarAportacion(modelo, id) {
  var url = $('form').attr("data-info-url");
  $.ajax({
    url: url,
    data: {
      'modelo': modelo,
      'id': id,
    },
    success: function (data) {
      $("#id_aportacion_espol_porcentaje").val(+data.costo.espol).trigger('change')
      $("#id_aportacion_espoltech_porcentaje").val(+data.costo.espoltech).trigger('change')
      $("#id_aportacion_ministerio_porcentaje").val(+data.costo.ministerio).trigger('change')
    }
  })
}


function CalcularValoresEgresos(valor, id_total, dependodnother, id_field) {
  var valo1 = valor

  if (valor < 0) valo1 = 0;

  var valor2 = 1;
  if (dependodnother == "True") {
    valor2 = $("#" + id_field).val();
  }
  var resultado = +valo1 * +valor2;
  $("#" + id_total).val(resultado.toFixed(2)).trigger('change');
}



function CalcularEgresos(clase) {
  var total = 0;
  $("." + clase).each(function (index) {
    if ($(this).val() !== "")
      total += +$(this).val();
  });
  return total;
}


function CalcularHonorarios() {
  const costo_total = $("#id_costo_instructores").val();
  $('#costo_total_instructores').val(costo_total);
  var resultado = costo_total * $("#id_n_horas").val();
  $("#id_honorario_total_evento").val(resultado.toFixed(2));
  var honorario = resultado / $("#id_ingreso_neto_total").val() * 100;
  $("#id_porcentaje_honorario_instructor").val(honorario.toFixed(0));
  if (honorario > 20 && honorario <= 100) {
    alert("Los honorarios superan el 20% del ingreso neto del evento.")
  }
}

function DependenciaCalculo(lista_id) {
  $.each(lista_id, function (index, value) {
    $('#' + value).trigger('change');
  })
}

$('.otros').change(function (e) {
  console.log($(this).val());
  if ($(this).val() == 100) {
    $('#' + e.target.dataset.label).attr('readonly', false);
  }
  else {
    $('#' + e.target.dataset.label).attr('readonly', true);
  }
});


$("#id_n_horas").change(function (e) {
  var depend = ['id_instalaciones_unitario'];
  DependenciaCalculo(depend);
});

$("#id_n_dias").change(function (e) {
  var depend = ['id_movilizacion_interna_unitario', 'n_dias_participantes'];
  DependenciaCalculo(depend);
});

$("#id_ingreso_neto_individual").change(function (e) {
  var depend = ['id_aportacion_espol_porcentaje', 'id_aportacion_espoltech_porcentaje', 'id_aportacion_ministerio_porcentaje','id_aportacion_facultad_porcentaje_unitario'];
  DependenciaCalculo(depend);
});

$('#id_aportacion_facultad_total').change(function (e) {
  $('#resumen_aporte_facultad').val(e.target.value);
  $('#id_n_cursos').trigger('change');
})

$("#id_n_participantes").change(function (e) {
  var depend = ['id_ingreso_individual_sin_desc', 'id_certificados_unitario', 'id_carpeta_unitario', 'id_maletin_unitario', 'id_block_unitario', 'id_lapiz_unitario', 'id_pluma_unitario', 'n_dias_participantes',
    'id_credencial_plastico_unitario', 'id_credencial_pvc_unitario', 'id_pendrive_unitario', 'id_otros_materiales_unitario', 'ceremonia_participantes', 'id_break_evento_dias', 'id_almuerzo_evento_dias',
    'id_imprevisto_unitario', 'id_total_egresos'];
  $('#resumen_n_participantes').val($(this).val());
  DependenciaCalculo(depend);
});

$("#id_ingreso_individual_sin_desc").change(CalcularIngresos);

$("#ceremonia_participantes").change(function (event) {
  var n_participantes = $('#id_n_participantes').val();
  var valor = +(+n_participantes * 2) + 5;
  event.target.value = valor;
  CalcularValoresEgresos(valor, event.target.dataset.total, event.target.dataset.depend, event.target.dataset.field);
});

$("#n_dias_participantes").change(function (event) {
  var n_participantes = $('#id_n_participantes').val();
  var n_dias = $('#id_n_dias').val();

  var valor = n_participantes * n_dias
  event.target.value = valor;
  CalcularValoresEgresos(+valor, event.target.dataset.total, event.target.dataset.depend, event.target.dataset.field);
});

$('#n_dias_participantes').change();

$(".valor-total").change(function (event) {
  CalcularValoresEgresos(event.target.value, event.target.dataset.total, event.target.dataset.depend, event.target.dataset.field);
});

$(".valor-porcentaje").change(function (event) {
  if (event.target.value > +event.target.max) {
    event.target.value = +event.target.max
  }
  if (event.target.value < +event.target.min) {
    event.target.value = +event.target.min
  }
  CalcularValoresEgresos(+(event.target.value / 100), event.target.dataset.total, event.target.dataset.depend, event.target.dataset.field);
});

$(".punto").change(function (event) {
  var egreso_fijo = $('#id_total_egresos_fijos').val();
  var precio = $('#id_ingreso_neto_individual').val();
  var egreso_unit = $("#id_egreso_variable_unit").val();
  var resultado = +egreso_fijo / +(precio - egreso_unit);
  $("#id_punto_equilibrio").val(resultado.toFixed(0));
});

$(".egreso-fijo").change(function (e) {
  var total1 = CalcularEgresos('egreso-fijo');
  var total2 = CalcularEgresos('egreso-variable');
  var total = total1 + total2;
  var ingreso = $('#id_ingreso_neto_total').val();
  var utilidad = ingreso - total;
  console.log(ingreso+" "+total);
  $("#id_total_egresos_fijos").val(total1.toFixed(2));
  $("#id_total_egresos").val(total.toFixed(2)).trigger('change');
  $("#resumen_egreso").val(total.toFixed(2));
  $("#resumen_egreso_fijo").val(total1.toFixed(2));
  $('#id_utilidad').val(utilidad.toFixed(2));
  $("#id_margen_contribucion").val((utilidad / ingreso).toFixed(2))

});

$(".egreso-variable").change(function (e) {
  var total1 = CalcularEgresos('egreso-variable');
  var total2 = CalcularEgresos('egreso-fijo');
  var total = total1 + total2;
  var ingreso = $('#id_ingreso_neto_total').val();
  var resultado = ingreso - total;
  $("#id_total_egresos_variables").val(total1.toFixed(2));
  $("#id_total_egresos").val(total.toFixed(2)).trigger('change');
  $("#resumen_egreso").val(total.toFixed(2));
  $("#resumen_egreso_variable").val(total1.toFixed(2));
  $('#id_utilidad').val(resultado.toFixed(2));
  $("#id_margen_contribucion").val((resultado / ingreso).toFixed(2))
  var resultado2 = total1 / $("#id_n_participantes").val();
  $('#id_egreso_variable_unit').val(resultado2.toFixed(2)).trigger('change');
});
