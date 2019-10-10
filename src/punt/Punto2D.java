package punt;

public class Punto2D extends Punto{
    public float calcularDistancia(Punto2D p){
        float distancia = 0;
        distancia = (float) Math.sqrt(Math.pow((this.x-p.x),2) + Math.pow((this.y - p.y), 2));
        return distancia;        
    }
    public float calcularDistancia(){
        float distancia = 0;
        distancia = (float) Math.sqrt(Math.pow((this.x),2) + Math.pow((this.y), 2));
        return distancia;        
    }

}