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


let fechaEnMiliseg = Date.now()


function api_request(){
    fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
    .then(response=>response.json())
    .then(data=>{
        for(let i in ids){
            console.log(data[i].casa.nombre);
            let contenido= document.getElementById(ids[i]);
            let titulo= document.getElementById("titulocoti")  
            titulo.innerHTML= `Cotizaciones`    
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
