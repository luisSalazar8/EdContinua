
$(document).ready(function () {
    initSelect2();
    load_data_descripcion();
});


$(document).on('change', '#id_centro_costos', function(e){
    load_data_descripcion();
});

$(document).on('change', '#id_codigo', function () {
    autocomplete($(this), 'id_partida');
});

$(document).on('change', '#id_partida', function () {
    autocomplete($(this), 'id_codigo');
});

$(document).on('click', "#div_id_partida span.selection", function (e) {
    load_data_descripcion();
});

$(document).on('click', "#div_id_codigo span.selection", function (e) {
    load_data_descripcion();
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
    console.log(tipo);
    
    if (tipo != "") {
        $.ajax({
            url: url,
            data: {
                'tipo': tipo
            },
            success: function (data) {
                $("#id_codigo").html(data.codigo).trigger('change.select2');
                $("#id_partida").html(data.partida).trigger('change.select2');
            }
        });
    }
    else{
        $('#id_codigo').val('').trigger('change.select2');
        $('#id_partida').val('').trigger('change.select2');
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
    $('#id_codigo').select2('close');
    $('#id_partida').select2('close');
}

