
$(document).ready(function () {
    initSelect2();
    load_data_descripcion();
    load_data_producto();
});


$(document).on('change', '#id_centro_costos', function(e){
    load_data_descripcion();
});

$(document).on('change', '#codigo', function () {
    autocomplete($(this), 'partida');
    $("#id_egreso").val($(this).val());
});

$(document).on('change', '#partida', function () {
    autocomplete($(this), 'codigo');
    $("#id_egreso").val($('#codigo').val());
});

$(document).on('change', '#id_tipo_compra', function(e){
    load_data_producto();
});

$(document).on('change', '#producto', function () {
    $("#id_producto").val($(this).val());
    var prod=$(this).children('option[value="'+$(this).val()+'"]');
    $("#unidad_medida").val(prod.attr('data-unidad'));
    $("#costo_unitario").val(formatNumber(prod.attr('data-unitario')));
    $("#iva").val(prod.attr('data-iva'));
});


$(document).on('change',"#id_cantidad_anual",function(){
    var cant=+$(this).val();
    var unitario=unformatNumber($("#costo_unitario").val());
    var iva=unformatNumber($("#iva").val())*cant;
    var subtotal=cant*unitario;
    //Si iva es un check....
    //var iva=$("#iva").prop('checked') ? 1.12 : 1;
    //var total=subtotal*iva;
    var total= subtotal+iva;
    $("#id_subtotal").val(formatNumber(subtotal));
    $("#id_total").val(formatNumber(total));
});


function initSelect2() {
    $('.select2').select2({
        dropdownParent: $('#productoModalCenter'),
        dropdownAutoWidth: true,
        width: '100%',
        minimumInputLength: 2,
        language: {
            noResults: function () {
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
}

function load_data_descripcion() {
    var url = $('#form').attr("data-tipo-url");
    var tipo = $("#id_centro_costos").val();    
    if (tipo != "") {
        $.ajax({
            url: url,
            data: {
                'tipo': tipo
            },
            success: function (data) {
                $("#codigo").html(data.codigo);
                $("#codigo").val($("#id_egreso").val()).trigger('change.select2');
                $("#partida").html(data.partida);
                $("#partida").val($("#partida option[name='"+$("#id_egreso").val()+"']").val()).trigger('change.select2');
            }
        });
    }
    else{
        $('#codigo').val(null).trigger('change.select2');
        $('#partida').val(null).trigger('change.select2');
    }
};


function load_data_producto() {
    var url = $('#form').attr("data-producto-url");
    var tipo = $("#id_tipo_compra").val();
    
    if (tipo != "") {
        $.ajax({
            url: url,
            data: {
                'tipo': tipo
            },
            success: function (data) {
                $("#producto").html(data.producto);
                $("#producto").val($("#id_producto").val()).trigger('change');
            }
        });
    }
    else{
        $('#producto').val(null).trigger('change.select2');
    }
};

//Autocompleta de un select a otro usando el id
function autocomplete(from, to) {
    if (from.val() != "") {
        $('#' + to).val($('#' + to + " option[name='" + from.val() + "']").val()).trigger('change.select2');
    }
    else {
        $('#' + to).val(null).trigger('change.select2');
    }
}

function GetCurrentDate() {
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();

    today = yyyy + '-' + mm + '-' + dd;
    return today;
}