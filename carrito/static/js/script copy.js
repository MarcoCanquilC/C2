
/* Js para el menu hamburguesa*/ 
const nav = document.querySelector("#nav")
const abrir =document.querySelector("#abrir")
const cerrar =document.querySelector("#cerrar")

abrir.addEventListener("click", ()=>{
    nav.classList.add("visible")
})

cerrar.addEventListener("click", ()=>{
    nav.classList.remove("visible")
})


/* Js para alerta excluvo socios*/
const exclusivo = document.getElementById("exclusivo");

exclusivo.addEventListener("click", () => {
    alert("¡Proximamente Exclusivo Socios!");
});


/* Lista de subcategorias */
const subcategoria = {
    plastico: ["Botellas", "Envases", "Bolsas"],
    papel: ["Periódicos", "Cartón", "Papel de oficina"],
    vidrio: ["Botellas", "Frascos", "Cristalería"],
    metales: ["Latas", "Cables", "Electrodomésticos pequeños"],
    electronicos: ["Teléfonos móviles", "Baterías", "Componentes de computadoras"]
};

/*cambia segun la cateregoria elgida */
document.getElementById('principal').addEventListener('change', function() {
    
    const tipoResiduo = this.value;
    const subMenu = document.getElementById('subcategoria');
    subMenu.innerHTML = '<option value="selecciona">Selecciona</option>'; // Limpiar el menú anterior

    if (subcategoria[tipoResiduo]) {

        subcategoria[tipoResiduo].forEach(function(sub) {
            const option = document.createElement('option');
            
            option.value = sub.toLowerCase().replace(/\s+/g, '-'); //en caso de querer ocuparlo

            option.textContent = sub;
            subMenu.appendChild(option);
        });
    }

});

document.getElementById('boton_enviar').addEventListener("click", () => {
    
    let errores = [];

    // Obtener valores de los campos
    const tipoResiduo = document.getElementById('principal').value;
    const subcategoria = document.getElementById('subcategoria').value;
    const nombre = document.getElementById('nombre').value.trim();
    const correo = document.getElementById('correo').value.trim();
    const direccion = document.getElementById('direccion').value.trim();
    const errorDiv = document.getElementById('errorDiv');

    // Validar que todos los campos requeridos no este vacios
    if (tipoResiduo === 'selecciona') {
        errores.push('Seleccione un tipo de residuo.');
    }
    if (subcategoria === 'selecciona') {
        errores.push('Seleccione una subcategoría.');
    }
    if (nombre === '') {
        errores.push('El campo "Nombre" es obligatorio.');
    }
    if (!validarCorreo(correo)) {
        errores.push('Ingrese un correo electrónico válido.');
    }
    if (direccion === '') {
        errores.push('El campo "Dirección" es obligatorio.');
    }

    // Mostrar errores si existen
    if (errores.length > 0) {
        texto_error.style.display = 'block';
        texto_error.innerHTML = errores.join('<br>'); // Mostrar errores separados por línea

    } else {
        texto_error.style.display = 'none';
        alert('Formulario enviado correctamente.');
        // Aquí se puede enviar el formulario si pasa las validaciones
    }

    // Validar formato de correo electrónico
    function validarCorreo(correo) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(correo);
    }

});



    