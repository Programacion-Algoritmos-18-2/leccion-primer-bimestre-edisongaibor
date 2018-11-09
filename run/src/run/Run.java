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
public class Run {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Empleado e = new Empleado();
        e.agregarNombre("Luis");
        e.agregarApellido("benitez");
        e.agregarCedula("110001");
        System.out.println(e);
        
    }
    
}
