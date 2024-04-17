package Es1;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class FileManager {
    public void generaFile(String nomeFile) throws IOException {
        FileWriter out;
        BufferedWriter writer = null;
        try {
            out = new FileWriter(nomeFile+".txt", true);
            writer = new BufferedWriter(out);
            for(int i = 0; i<5; ++i){
                Random random = new Random();
                int chooseA = random.nextInt(3);
                switch(chooseA){
                    case 0:
                        for (int j = 0; j < 20; ++j) {
                            int chooseB = random.nextInt(2);
                            switch(chooseB){
                                case 0:
                                    String ch = Character.toString(random.nextInt(97, 122));
                                    writer.write(ch);
                                    break;
                                case 1:
                                    ch = Character.toString(random.nextInt(48, 57));
                                    writer.write(ch);
                                    break;
                            }
                        }
                        writer.newLine();
                    case 1:
                        for (int j = 0; j < 20; ++j) {
                            String ch = Character.toString(random.nextInt(97, 122));
                            writer.write(ch);
                        }
                        writer.newLine();
                        break;
                    case 2:
                        for (int j = 0; j < 20; ++j) {
                            String ch = Character.toString(random.nextInt(48, 57));
                            writer.write(ch);
                        }
                        writer.newLine();
                        break;
                }
            }

        } finally {
            if (writer != null) writer.close();
        }
    }

    List<String> leggiFile(String nomeFile) throws IOException{
        List<String> rows = new ArrayList<>();
        FileReader in = null;
        try{
            in = new FileReader(nomeFile+".txt");
            BufferedReader reader = new BufferedReader(in);
            while (reader.ready()) {
                rows.add(reader.readLine());
            }
            return rows;
        }
        finally {
            if(in!=null) in.close();
        }
    }

    public void stampaLineeNumeriche(String nomeFile) throws IOException{
        List<String> rows = leggiFile(nomeFile);
        for(String i:rows){
            boolean print = true;
            for(int j=0; j<i.length(); ++j){
                if(!Character.isDigit(i.charAt(j))){
                    print = false;
                }
            }
            if(print) System.out.println(i);
        }
        System.out.println();
    }

    public void stampaLineeConLetterePari(String nomeFile, char lettera) throws IOException {
        List<String> rows = leggiFile(nomeFile);
        for(String i:rows){
            int cont = 0;
            for(int j=0; j<i.length(); ++j){
                if(i.charAt(j)==lettera){
                    cont++;
                }
            }
            if(cont%2==0 && cont != 0) System.out.println(i);
        }
        System.out.println();
    }

    public void stampaLineeConNumeroUguale(String nomeFile, char lettera1, char lettera2) throws IOException {
        List<String> rows = leggiFile(nomeFile);
        for(String i:rows){
            int cont1 = 0, cont2 = 0;
            for(int j=0; j<i.length(); ++j){
                if(i.charAt(j)==lettera1){
                    cont1++;
                }
                if(i.charAt(j)==lettera2){
                    cont2++;
                }
            }
            if(cont1==cont2 && cont1 != 0) System.out.println(i);
        }
        System.out.println();
    }
}
