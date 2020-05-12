import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Random;

// das hier ist die Aufgabe Java LCG
public class Main {

    private static int readInt() throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        return Integer.parseInt(input.readLine());
    }

    public static void main(String[] args) {
        Random rng = new Random();
        int i, rand, input;
        System.out.println("Welcome to the Java lottery!");
        for (i = 0; i < 10; i++) {
            // in jedem Versuch wird eine neue random number generiert; immer 9 Stueck bis neuer rng
            // Returns a pseudorandom, uniformly distributed int value between 0 (inclusive)
            // and the specified value (exclusive), drawn from this random number generator's sequence.
            // int.MAX_VALUE = 2147483647
            // die nummern sind auch nicht immer gleich lang, aber max. 32 bit lang
            rand = rng.nextInt(Integer.MAX_VALUE);
            System.out.println("What's the magic number?");
            try {
                input = readInt();
                if (input == rand) {
                    System.out.println("YOU WON!!!!");
                    System.out.println("flag{...}");
                    break;
                } else {
                    System.out.printf("WRONG! The magic number was: %d%n", rand);
                }
            } catch (IOException e) {
                System.out.println("DAFUQ ARE YOU DOING?!");
            }
        }

        // also man hat immer nur 9 Versuche bis eine neue instanz von Random generiert wird
        if (i == 9) {
            System.out.println("No more trials for you young lady!");
        }
    }
}
