/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package run;

/**
 *
 * @author edisongaibor
 */
public class EmpleadoFijo extends Empleado {
    private double sueldofijo;
    private double descuentofijo;
    private double operacion;
    private double descuentoseguro;
    


    public double obtenerSueldofijo() {
        return sueldofijo;
    }

    public double obtenerDescuentofijo() {
        return descuentofijo;
    }

    public double obtenerOperacion() {
        return operacion;
    }

    public double obtenerDescuentoseguro() {
        return descuentoseguro;
    }

    public void agregarSueldofijo(double sueldo) {
        sueldofijo = sueldo;
    }

    public void agregarDescuentofijo(double des) {
        descuentofijo = des;
    }

    public void agregarOperacion(double oper) {
        operacion = oper;
    }

    public void agregarDescuentoseguro(double desc) {
        descuentoseguro = desc;
    }
  
    
    
    
}
    

