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
public class Empleado {
    public String nombre;
    public String apellido;
    public String cedula;
    public double comisionfija;

    public String obtenerNombre() {
        return nombre;
    }

    public String obtenerApellido() {
        return apellido;
    }

    public String obtenerCedula() {
        return cedula;
    }

    public double obtenerComisionfija() {
        return comisionfija;
    }

    public void agregarNombre(String n) {
        nombre = n;
    }

    public void agregarApellido(String a) {
        apellido = a;
    }

    public void agregarCedula(String ced) {
        cedula = ced;
    }

    public void agregarComisionfija(double comi) {
        comisionfija = comi;
    }
    
    
 
    @Override
    public String toString(){
        return String.format("Informacion de %s %s\nCedula %s", 
                obtenerNombre(), obtenerApellido(), obtenerCedula());
    }
    
    
}
