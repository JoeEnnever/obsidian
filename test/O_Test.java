import java.util.*;

public class O_Test {
	public static void main(String[] args){
		System.out.println("Args: " + Arrays.asList(args));
                System.out.println("------------Env--------------\n" + System.getenv());	
		System.out.println("------------Props------------\n" + System.getProperties());
	}
}
