let vacio = 0;  
let vacioList = [];
function Confirmar(){
    var vacioList=[]

$("input[type=radio]").each(function() {
    console.log($(this).attr("checked"));
    if($(this).attr("checked")!=undefined){
        console.log("si entra")
        if($(this).val()=="Primaria" || $(this).val()=="Secundaria"){
            console.log("entro primaria/secundaria");
            $("#id_ti_tercernivel").attr("class",$("#id_ti_tercernivel").attr("class")+" ignorar");
            $("#id_un_tercernivel").attr("class",$("#id_un_tercernivel").attr("class")+" ignorar");
            $("#id_pais_estudio").attr("class",$("#id_pais_estudio").attr("class")+" ignorar");
            $("#id_tercer_progreso").attr("class",$("#id_tercer_progreso").attr("class")+" ignorar");
            $("#id_ti_postgrado").attr("class",$("#id_ti_postgrado").attr("class")+" ignorar");
            $("#id_un_postgrado").attr("class",$("#id_un_postgrado").attr("class")+" ignorar");
        }else if($(this).val()=="Tercer Nivel"){
            console.log("entro tercer nivel");
            $("#id_ti_postgrado").attr("class",$("#id_ti_postgrado").attr("class")+" ignorar");
            $("#id_un_postgrado").attr("class",$("#id_un_postgrado").attr("class")+" ignorar");
            $("#id_institucion").attr("class",$("#id_institucion").attr("class")+" ignorar");
            $("#id_progreso").attr("class",$("#id_progreso").attr("class")+" ignorar");
        }else{
            console.log("entro posgrado")
            $("#id_ti_tercernivel").attr("class",$("#id_ti_tercernivel").attr("class")+" ignorar");
            $("#id_un_tercernivel").attr("class",$("#id_un_tercernivel").attr("class")+" ignorar");
            $("#id_institucion").attr("class",$("#id_institucion").attr("class")+" ignorar");
            $("#id_progreso").attr("class",$("#id_progreso").attr("class")+" ignorar");
        }
    }
    
    });

$("input").each(function() {
    var clases=$(this).attr("class");
    
    if($(this).val()=="" && !clases.includes("ignorar")){
        var label=$(this).parent().parent().children()[0];
        vacio =$(label).text();
        vacioList.push(vacio);
    }
    
});

$("select").each(function() {
    var clases=$(this).attr("class");
    if($(this).val()=="" && !clases.includes("ignorar")){
        var label=$(this).parent().parent().children()[0];
        vacio =$(label).text();
        vacioList.push(vacio);
    }
    
});

$("textarea").each(function() {
    var clases=$(this).attr("class");
    if($(this).val()=="" && !clases.includes("ignorar")){
        var label=$(this).parent().parent().children()[0];
        vacio =$(label).text();
        vacioList.push(vacio);
    }
    







      
    // $("a#confirmar").click(function (e) { 
    //     var campos = $("input[id]");
    //     var select = $("select[id]");
    //     var text_area = $("textarea[id]");
       
        
    //     campos.each(function (){

    //         if($(this).val()=="")
    //              vacios+=1;
    //              var l = $(this).parent().prev().text();
    //              labels.push(l);
            
    //     });
    //     select.each(function (){

    //         if($(this).val()=="")
    //              vacios+=1;
    //              var l = $(this).parent().prev().text();
    //              labels.push(l);
            
    //     });
    //     text_area.each(function (){

    //         if($(this).val()=="")
    //              vacios+=1;
    //              var l = $(this).parent().prev().text();
    //              labels.push(l);
            
    //     });



        // var select = $("select[id]");
        // console.log(campos.length);
        // vacios = 0;
        // campos_vacios =[];
        // for(i=0;i<campos.length;i++){
        //     console.log($(campos[i]).val());
        //     if($(campos[i]).val()==""){
        //         vacios+=1;
        //     }
        // }
        // var select = $("select[id]");
        // console.log(vacios);
    parrafo = $("<p></p>");
    console.log(vacios);
    parrafo.html("Hay " + String(vacios) + " campos vacíos");
    $("#modal-confirmacion").html("¿Está seguro que desea guardar los datos?");
    $("#modal-confirmacion").append(parrafo);
    vacioList.forEach(function(item,index){
        p = $("<p></p>");
        p.html(item);
        $("#modal-confirmacion").append(p);


    });
    vacios=0;
    vacioList = [];
    });
    
    
}
$(document).ready(function () {
    Confirmar();

    

  });