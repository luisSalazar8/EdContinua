$("tbody").children().each(function(){
    var ccant={};
    var codu=[];
    const cod=$(this).children()[5];
    $(cod).children().each(function(){
        if($(this).prop("tagName")!="BR"){
            if(codu.includes($(this).html())){
                ccant[$(this).html()]=ccant[$(this).html()]+1;
                $(this).next().remove();
                $(this).remove();
                
            }else{
                codu.push($(this).html());
                ccant[$(this).html()]=1;
            }
        }
        
    });
    console.log(ccant);
    console.log(codu);
    
    var nomu=[];
    const nom=$(this).children()[4];
    $(nom).children().each(function(){
        if($(this).prop("tagName")!="BR"){
            if(nomu.includes($(this).attr("class"))){
                $(this).next().remove();
                $(this).remove();
                
            }else{
                nomu.push($(this).attr("class"));
            }
        }
        
    });
    console.log(nomu);

    var valu=[];
    const val=$(this).children()[7];
    $(val).children().each(function(){
        if($(this).prop("tagName")!="BR"){
            if(valu.includes($(this).html())){
                $(this).next().remove();
                $(this).remove();
                
            }else{
                valu.push($(this).html());
            }
        }
        
    });
    console.log(valu);

    const part=$(this).children()[6];
    Object.keys(ccant).forEach(function(key){
        console.log(key);
        const span=$("<span>");
        span.html(ccant[key]);
        $(part).append(span);
        $(part).append($("<br>"));

    });

    var vtcant={};
    const vt=$(this).children()[9];
    $(vt).children().each(function(){
        if($(this).prop("tagName")!="BR"){
            if(vtcant[$(this).attr("class")]!=undefined){
                vtcant[$(this).attr("class")]=parseFloat($(this).html())+vtcant[$(this).attr("class")];
                $(this).next().remove();
                $(this).remove();
            }else{
                vtcant[$(this).attr("class")]=parseFloat($(this).html());
                $(this).next().remove();
                $(this).remove();
            }
        }
        
    });
    console.log(vtcant);
    Object.keys(vtcant).forEach(function(key){
        console.log(key);
        const span=$("<span>");
        span.html(vtcant[key]);
        $(vt).append(span);
        $(vt).append($("<br>"));

    });


    // var dcant={};
    // const desc=$(this).children()[8];
    // $(desc).children().each(function(){
    //     if($(this).prop("tagName")!="BR"){
    //         if(dcant[$(this).attr("class")]!=undefined){
    //             dcant[$(this).attr("class")]=parseFloat($(this).html())+dcant[$(this).attr("class")];
    //             $(this).next().remove();
    //             $(this).remove();
    //         }else{
    //             dcant[$(this).attr("class")]=parseFloat($(this).html());
    //             $(this).next().remove();
    //             $(this).remove();
    //         }
    //     }
        
    // });
    // console.log(dcant);
    // Object.keys(dcant).forEach(function(key){
    //     console.log(key);
    //     const span=$("<span>");
    //     span.html(dcant[key]/ccant[key]);
    //     $(desc).append(span);
    //     $(desc).append($("<br>"));

    // });


});