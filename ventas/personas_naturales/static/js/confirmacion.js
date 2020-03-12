let vacioList = [];
function Confirmar(){
    
$("a#confirmar").click(function (e) { 
   

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
        

});






      
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
    parrafo.html("Hay " + String(vacioList.length) + " campos vacíos");
    $("#modal-confirmacion").html("¿Está seguro que desea guardar los datos?");
    $("#modal-confirmacion").append(parrafo);
    var cont=0;
    var padreactual= undefined;
    //const padre=$("<div>");
    //padre.attr("class","row");
    vacioList.forEach(function(item,index){
        if((cont%2)==0){
            p = $("<p></p>");
            p.attr("class","col-6 text-justify")
            p.html(item);
            //$("#modal-confirmacion").append(p);
            const padre=$("<div>");
            padre.attr("class","row");
            padre.append(p);
            $("#modal-confirmacion").append(padre);
            padreactual=padre;
            cont=cont+1;
        }else{
            console.log("momazo")
            p = $("<p></p>");
            p.attr("class","col-6 text-justify")
            p.html(item);
            //$("#modal-confirmacion").append(p);
            padreactual.append(p);
            cont=cont+1;
        }
        


    });
    vacioList = [];
    });
    
    
}
$(document).ready(function () {
    Confirmar();
});