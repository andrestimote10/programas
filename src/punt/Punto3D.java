package punt;

public class Punto3D extends Punto{
    public float z;
    public float calcularDistancia(Punto3D p){
        float distancia = 0;
        distancia = (float) Math.sqrt(Math.pow((this.x-p.x),2) + Math.pow((this.y - p.y), 2) + Math.pow((this.z - z), 2));
        return distancia;        
    }
    
    public float calcularDistancia(){
        float distancia = 0;
        distancia = (float) Math.sqrt(Math.pow((this.x),2) + Math.pow((this.y), 2) + Math.pow((this.z), 2));
        return distancia;        
    }

    public float getZ() {
        return z;
    }

    public void setZ(float z) {
        this.z = z;
    }
    
}