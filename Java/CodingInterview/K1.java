import java.util.HashMap;
import java.util.Map;
import java.util.StringJoiner;

class Main {
    public static void main(String[] args) {
        String S = "John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker";
        String C = "Example";
        System.out.println(solution(S, C));
    }
    // S = "John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker"
    // return = "John Doe <jdoe@example.com>, Peter Parker <pparker@example.com>, Mary Jane Watson-Parker <mjwatsonpa@example.com>, James Doe <jdoe2@example.com>, John Elvis Doe <jedoe@example.com>, Jane Doe <jdoe3@example.com>, Penny Parker <pparker2@example.com>"
    public static String solution(String S, String C) {
        // write your code in Java SE 8
        String[] fullnames = S.split(", ");
        String[] nameAndEmail = new String[fullnames.length];
        HashMap<String, Integer> emailMap = new HashMap<>();
        for (int i = 0; i < fullnames.length; i++) {
            String fullName = fullnames[i];
            String[] fullNameInfos = fullName.split(" ");
            String name = "";
            String middle = "";
            String last = "";
            if (fullNameInfos.length == 2) {
                name = fullNameInfos[0];
                last = fullNameInfos[1];
            } else if (fullNameInfos.length == 3) {
                name = fullNameInfos[0];
                middle = fullNameInfos[1];
                last = fullNameInfos[2].replaceAll("-", "");
            }
            nameAndEmail[i] = fullName + " " + "<" + getEmail(name, middle, last, C, emailMap) + ">";
        }

        StringJoiner stringJoiner = new StringJoiner(", ");
        for (String s : nameAndEmail) {
            stringJoiner.add(s);
        }

        return stringJoiner.toString();
    }

    public static String getEmail(String name, String middle, String last, String company, Map<String, Integer> map) {
        name = name.toLowerCase();
        if (middle != "") {
            middle = middle.toLowerCase();
        }
        last = last.toLowerCase();
        company = company.toLowerCase();
        String email = "";
        String header = "";
        if (middle != "") {
            header = String.valueOf(name.charAt(0)) + String.valueOf(middle.charAt(0)) + last.substring(0, Math.min(8, last.length()));
        } else {
            header = String.valueOf(name.charAt(0)) + last.substring(0, Math.min(8, last.length()));
        }
        email = getEmail(header, company);

        if (map.containsKey(header)) {
            email = getEmail(header + String.valueOf(map.getOrDefault(header, 0) + 1), company);
        }
        map.put(header, map.getOrDefault(header, 0) + 1);
        return email;
    }

    public static String getEmail(String header, String company) {
        return header + "@" + company + ".com";
    }
}