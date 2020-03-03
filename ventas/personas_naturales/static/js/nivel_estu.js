function nivel_de_estudio(){
    if(document.getElementById("id_nivel_estudio_0").checked){

        document.getElementById("div_id_ti_tercernivel").style.display = "none";
        document.getElementById("div_id_un_tercernivel").style.display = "none";
        document.getElementById("div_id_pais_estudio").style.display = "none";
        document.getElementById("div_id_ti_postgrado").style.display = "none";
        document.getElementById("div_id_un_postgrado").style.display = "none";
        

        document.getElementById("div_id_institucion").style.display= 'block';
        document.getElementById("div_id_progreso").style.display= 'block';
        document.getElementById("div_id_profesion").style.visibility= 'visible';
    }

    if(document.getElementById("id_nivel_estudio_1").checked){
        document.getElementById("div_id_ti_tercernivel").style.display = "none";
        document.getElementById("div_id_un_tercernivel").style.display = "none";
        document.getElementById("div_id_pais_estudio").style.display = "none";
        document.getElementById("div_id_ti_postgrado").style.display = "none";
        document.getElementById("div_id_un_postgrado").style.display = "none";
        

        document.getElementById("div_id_institucion").style.display= 'block';
        document.getElementById("div_id_progreso").style.display= 'block';
        document.getElementById("div_id_profesion").style.visibility= 'visible';

    }

    if(document.getElementById("id_nivel_estudio_2").checked){

        
        document.getElementById("div_id_ti_postgrado").style.display = "none";
        document.getElementById("div_id_un_postgrado").style.display = "none";
        document.getElementById("div_id_institucion").style.display = "none";

        document.getElementById("id_ti_tercernivel").style.display = "block";
        document.getElementById("div_id_ti_tercernivel").style.display = "block";
        document.getElementById("id_un_tercernivel").style.display = "block";
        document.getElementById("div_id_un_tercernivel").style.display = "block";
        document.getElementById("id_pais_estudio").style.display = "block";
        document.getElementById("div_id_pais_estudio").style.display = "block";
        document.getElementById("id_progreso").style.visibility= 'block';
        document.getElementById("div_id_progreso").style.visibility= 'block';
        document.getElementById("id_profesion").style.visibility= 'visible';
        document.getElementById("div_id_profesion").style.visibility= 'visible';

    }

    if(document.getElementById("id_nivel_estudio_3").checked){
        document.getElementById("div_id_institucion").style.display = "none";

        document.getElementById("id_ti_tercernivel").style.display='inline';
        document.getElementById("div_id_ti_tercernivel").style.display='inline';
        document.getElementById("id_un_tercernivel").style.display = "inline";
        document.getElementById("div_id_un_tercernivel").style.display = "inline";
        document.getElementById("id_pais_estudio").style.display = "inline";
        document.getElementById("div_id_pais_estudio").style.display = "inline";
        document.getElementById("id_ti_postgrado").style.display = "block";
        document.getElementById("div_id_ti_postgrado").style.display = "block";
        document.getElementById("id_un_postgrado").style.display = "block";
        document.getElementById("div_id_un_postgrado").style.display = "block";
        document.getElementById("id_progreso").style.visibility= 'block';
        document.getElementById("div_id_progreso").style.visibility= 'block';
        document.getElementById("id_profesion").style.visibility= 'visible';
        document.getElementById("div_id_profesion").style.visibility= 'visible';

    }
}