function calcular_edad(){
    let a = prompt("Ingresa el año en que naciste (4 digitos):", "1980");
    let m = prompt("Ingresa el mes en que naciste (1-12):", "6");
    let d = prompt("Ingresa el día en que naciste (1-31):", "15");
    
    let fecha_nacimiento = new Date();
    fecha_nacimiento.setFullYear(parseInt(a), parseInt(m) - 1, parseInt(d));
    
    var edad = Math.floor( (Date.now() - fecha_nacimiento.getTime()) / (60 * 60 * 24 * 1000 * 365.25) );
    
    const month = fecha_nacimiento.toLocaleString('default', { month: 'long' });
    
    alert("Tu fecha de naciemiento es: " + d + " de " + month + " del año " + a);
    alert("Y tienes " + edad + " años.");
}

setTimeout(calcular_edad, 1500);