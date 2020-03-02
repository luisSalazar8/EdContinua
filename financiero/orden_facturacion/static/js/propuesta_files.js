

//Codigo para los archivos
        $(document).on('change', ".anexo", function (e) {
            e.preventDefault();
            console.log($(this).children([0]));
            const hijo=$(this).children([0]);
            console.log($(this).val());
            if($(this).val()==""){
                console.log("esta vacio");
                deleteForm('propuestafile_set', $(this));
            }else{
                console.log("esta lleno");
                cloneMore('.form-row:last', 'propuestafile_set');
                /*  cantInput=cantInput+1;
                const divp=$("<div>");
                divp.attr("id","div_anexos"+cantInput);
                divp.attr("class","form-group");
                const inputf=$("<input/>");
                inputf.attr("type","file");
                inputf.attr("id","id_archivo"+cantInput);
                inputf.attr("class","form-control anexo");
                inputf.attr("name","archivo"+cantInput);
                $("#div_anexos").append(inputf);
                cont+=1;*/
            }
        });
        
        function cloneMore(selector, prefix) {
            var newElement = $(selector).clone(true);
            var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
            
            newElement.find(':input:not([type=button]):not([type=submit]):not([type=reset])').each(function() {
                var name = $(this).attr('name').replace('-' + (total-1) + '-', '-' + total + '-');
                var id = 'id_' + name;
                $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
            });
            
            total++;
            $('#id_' + prefix + '-TOTAL_FORMS').val(total);
            $(selector).after(newElement);
        
        }
        
        function deleteForm(prefix, btn) {
            var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
            if (total > 1){
                $(btn).parent().parent().parent().parent().remove();
                var forms = $('.form-row');
                $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length-1);
                for (var i=1, formCount=forms.length; i<formCount; i++) {
                    console.log(forms[i]);
                    $(forms.get(i)).find(':input').each(function() {
                        updateElementIndex(this, prefix, i);
                    });
                }
            }
            return false;
        }
        
        function updateElementIndex(el, prefix, ndx) {
            var namep="form-"+(ndx-1)+"-file"
            console.log(namep);
            var id = 'id_' + namep;
            $(el).attr('name', namep);
            console.log($(el).attr('name'));
        }

    if($("[name=cod_propuesta]").val()!=""){
        $("td a + input").each(function() {
            $(this).remove();
          });
        
          $("td a + label").each(function() {
            $(this).remove();
        });
    }else{
        $("td input[type=checkbox]").each(function() {
            $(this).parent().remove();
            $(this).remove();
          });
        
          
    }
        console.log($("[name=cod_propuesta]").val())