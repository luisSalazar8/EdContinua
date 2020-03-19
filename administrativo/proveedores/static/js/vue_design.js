const app=new Vue({
    el:'#app',
    delimiters:["{","}"],
    data:{
        contactos:[],
        //recursos
        formActualizarContacto:false,
        indexUpdateContacto:null,

        ciContacto:"",
        nombreContacto:"",
        apellidosContacto:"",
        cargoContacto:"",
        contactoContacto:"",
        telefonoContacto:"",
        celularContacto:"",
        correoContacto:"",

        newciContacto:"",
        newnombreContacto:"",
        newapellidosContacto:"",
        newcargoContacto:"",
        newcontactoContacto:"",
        newtelefonoContacto:"",
        newcelularContacto:"",
        newcorreoContacto:"",
    },
    