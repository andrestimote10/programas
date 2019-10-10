package punt;

public class Principal {
    public static void main(String[] args){
        Punto2D p=new Punto2D();
        p.setX(1);
        p.setY(1);
        Punto2D a = new Punto2D();
        a.setX(5);
        a.setY(0);
        a.calcularDistancia(p);
        a.calcularDistancia();
        Punto3D c=new Punto3D();
        c.setX(1);
        c.setY(1);
        c.setZ(1);
        Punto3D b = new Punto3D();
        b.setX(5);
        b.setY(5);
        b.setZ(5);
        b.calcularDistancia(c);
        b.calcularDistancia();
        System.out.println(a.calcularDistancia(p) + "     "  + b.calcularDistancia(c) + "     " + a.calcularDistancia() + "     "  + b.calcularDistancia());
    }
}
