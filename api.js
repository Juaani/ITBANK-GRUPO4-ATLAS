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
            contenido.innerHTML= `<div id="infonueva" class="card text-white bg-secondary mb-3" style="max-width: 18rem;">
            <div class="card-header">${data[i].casa.nombre}</div>
          <p>Precio Compra: $${data[i].casa.compra}</p>
          <p>Precio Venta: $${data[i].casa.venta}</p>`;      
        }      
    })
}

function main(){
    setInterval(()=>{
        api_request();
    },50000)
}

api_request();
main();