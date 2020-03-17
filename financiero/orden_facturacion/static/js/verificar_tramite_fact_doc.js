var has_anexo = false;
var has_n_tra = false;
var has_n_fact = false;
var has_f_tra = false;
var has_f_fact = false;
verificar();
function isInteger(str) {
    return /^\d*$/.test(str);
}

function change_state_btn() {
    if (has_anexo && has_n_tra && has_n_fact) {
        $("#id_estado").val("PNDP");
    }
    else {
        $("#id_estado").val("ACPF");
    }
}

function verificar() {
    $(".ordenfactf").each(function(){
            if($(this).val()!=""){
                has_anexo=true;
            }

    });

    has_f_tra = $("#id_fecha_tramite").val()!=undefined;

    has_f_tra = $("#id_fecha_factura").val()!=undefined;

    has_n_fact = isInteger($("#id_n_factura").val());

    has_n_tra = isInteger($("#id_n_tramite").val());

    change_state_btn()
}

$("#id_anexo_factura").change(function () {
    has_anexo = $(this).get(0).files.length !== 0;
    change_state_btn()
});

$("#id_n_factura").focusout(function () {
    has_n_fact = isInteger($(this).val());
    change_state_btn()
});

$("#id_n_tramite").focusout(function () {
    has_n_tra = isInteger($(this).val());
    change_state_btn()
});

$(document).on('click', "#guardar", function (e) {
    verificar();
});