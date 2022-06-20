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

  const d = new Date();
  let day = d.getDate();
  let month = d.getMonth();
  let hours = d.getHours();
  let minute= d.getMinutes();

function api_request(){
  
    fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
    .then(response=>response.json())
    .then(data=>{
        for(let i in ids){
            console.log(data[i].casa.nombre);
            let contenido= document.getElementById(ids[i]);
            let titulo= document.getElementById("titulocoti")  
            titulo.innerHTML= `Cotizaciones`    
            contenido.innerHTML= `<div id="infonueva" class="card bg-light mb-3" style="max-width: 18rem; background-color: #1d71b8"">
            <div class="card-header bg-secondary text-white">${data[i].casa.nombre}</div>
          <div class="row justify-content-md-center" style="display: flex;
          width: 100%;">
          <div class="col-6" style="font-size:80%">
            Precio Venta:
          </div>
          <div class="col-6" style="font-size:80%">
          Precio Compra:
          </div>
          </div>
          <div class="row justify-content-md-center">
          <div class="col-6">
           <h4> $${data[i].casa.venta}</h4>
          </div>
          <div class="col-6">
          <h4> $${data[i].casa.compra}</h4>
          </div>
          </div> 
    
          <div class="card-footer text-muted" style="font-size:60%">
          Última actualización: ${day}/${month} ${hours}:${minute} hs
        </div>

        </div>
          `;      
        }      
    })
}

function main(){
    setInterval(()=>{
        api_request();
    },50000)
}

//function FbotonOn() {
   // var uno = document.getElementById('botonOn');
    //if (uno.innerHTML == 'Ocultar Detalles') 
       // uno.innerHTML = 'Ver Detalles';
    //else uno.innerHTML = 'Ocultar Detalles'; 
  //}
  function toggleClock(aq) {
    var myClock = document.getElementById(aq);
    var displaySetting = myClock.style.display;
    var clockButton = document.getElementById('botonOn');
    if (displaySetting == 'block') {
      myClock.style.display = 'none';
      clockButton.innerHTML = 'Ver Detalles';
    }
    else {
      myClock.style.display = 'block';
      clockButton.innerHTML = 'Ocultar Detalles';
    }
  }

  function todos(){
    api_request();
    //FbotonOn();
    toggleClock("titulocoti");
    toggleClock("dolaroficial");
    toggleClock("dolarblue");
    toggleClock("dolarsoja");
    toggleClock("dolarccl");
    toggleClock("dolarbolsa");
    toggleClock("bitcoin");
    toggleClock("dolarturista");
}



//  api_request();
//  main();

//  verDivisas.onclick = function()
// {
//     console.log("Ver divisas...");
//     api_request();
//     main();
// }
