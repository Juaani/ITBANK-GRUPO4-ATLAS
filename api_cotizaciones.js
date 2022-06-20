let ids = [
	"dolaroficial",
	"dolarblue",
	"dolarsoja",
	"dolarccl",
	"dolarbolsa",
    "bitcoin",
	"dolarturista",
    "dolar",
	"argentina",
];

function api_request(){
    fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
    .then(response=>response.json())
    .then(data=>{
        for(let i in ids){
            console.log(data[i].casa.nombre);
            let contenido= document.getElementById(ids[i]);            
            contenido.innerHTML=`${data[i].casa.nombre}<br>
            <p>Precio Compra: ${data[i].casa.compra}</p><br>
            <p>Precio Venta: ${data[i].casa.venta}</p>`;      
        }      
    })
    main();
}

function main(){
    setInterval(()=>{
        api_request();
    },50000)
}

//TODO: Ocultar el div de cotizaciones hasta que se aprete el botón, ahí hacerlo aparecer
//TODO: Podriamos poner que si se apreta el botón, el nombre cambie a Ocultar detalles, y si se presiona devuelta volver a ocultar el div de cotizaciones

// api_request();
// main();








</script>