#  문자열 다루기 1

- String [] 라는 문자열 배열

- class 내 외부에 모두 가능, 지역변수, 전역변수로 사용 가능

- 대신 외부에 두려면 static 이란걸 붙혀야함

- 입력받는데는 마찬가지로 Scanner를 사용하자.

### Lesson.java

```java
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Lesson {
	
//		지금은 지역변수로 사용, 함수 외부에 둬서 전역 변수처럼 사용할 수도 있음
//	대신 외부에 두려면 static 이란걸 붙혀야함
	static String [] names = new String [1000]; 
	static int [] numbers = new int[1000];
//	int [] numbers;
//	numbers = new int [1000];
	static int n=0;
	
	public static void main(String[] args) {
		
		Scanner sc;
		try {
			sc = new Scanner( new File("input.txt") );			
			
			while(sc.hasNext() ) {
				
				names[n] = sc.next(); 
				numbers[n] = sc.nextInt();
				n++;
			}
			
			sc.close();
			
		} catch (FileNotFoundException e) {	// 해당파일이 없으면 어쩔거냐 정하는 부분, 무조건 해야되는건아님.
			System.out.print("No file"); //내 맘대로 처리하면 됨.
			System.exit(1);
		}

		bubbleSort(n, names, numbers);
		
		for (int i=0; i<n; i++) {
			System.out.println(names[i] + "," +  numbers[i] );
			
		}
		

	}
	
	static public void bubbleSort(int n, String [] names, int [] numbers)// call-by-value
	{
		for (int i=n-1; i>0; i--) {
			for (int j=0; j<i; j++) {
				if ( names[j].compareTo(names[j+1] ) > 0 ) {  // ==0  str1.equals(str2) 문자열 같은지 비교하기 
					// swqp numbers [j] and numbers [j+1]
					int tmp = numbers[j];
					numbers[j] = numbers[j+1];
					numbers[j+1] = tmp;
							
					String tmpstr = names[j];
					names[j] = names[j+1];
					names[j+1] = tmpstr;
				} 			
				
			}
		}
	}
}
```



# 문자열 다루기2

- #### 인덱스 메이커

- 입력으로 하나의 텍스트 파일 일기
- 텍스트 파일에 등장하는 단어들의 목록 만들고, 단어가 텍스트 파일에 등장하는 횟수 세기
- 사용자가 요청하면 단어 목록을 하나의 파일로 저장
- 사용자가 단어 검색하면 단어가 텍스트 파일에 몇번 등장하는지 출력

- `java.lang.ArrayIndexOutOfBoundsException` 오류 => 배열의 인덱스를 벗어났다.

- `PrintWriter out`

```java
package Section3;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class Code22 {

	static String [] words = new String [100000];
	static int [] count = new int [100000];
	static int n= 0;
	
	public static void main(String[] args) {
		
		
		Scanner kb = new Scanner(System.in);
		
		while(true) {
			
			System.out.print("$ ");
			String command = kb.next();
			if (command.equals("read") ) {
				String fileName = kb.next();
				makeIndex( fileName );
			}
			else if (command.equals("find")) {
				String str = kb.next();
				int index = findWord(str);
				if (index > -1) {
					System.out.println("The word " + words[index] + " appears " + count[index] + " times.");
				}
				else
					System.out.println("The word" + str + " does not appear.");
			}
			else if (command.equals("saveas")) {
				String fileName = kb.next();
				saveAs( fileName );
			}
			else if (command.equals("exit")) {
				break;
			}
			
		}
		kb.close();
	}
		

	
	static void saveAs(String fileName) {
		
		PrintWriter outFile;
		try {
			outFile = new PrintWriter(new FileWriter(fileName));	// out 부분은 내가정하는 이름
			
			for (int i=0; i<n; i++)
				outFile.println(words[i] + " " + count[i]);
		
			
			outFile.close();
		} catch (IOException e) {
			System.out.println("Save failed");
		} 
		
		
		
		
	}
	
	
	static void makeIndex( String fileName) {
		
		try {
			Scanner inFile = new Scanner( new File(fileName));
			while(inFile.hasNext()) {
				String str = inFile.next();
				addWord(str);  // 목록에서 검사해서 상황에 따라 다르게하기
			}
			
			
			
			inFile.close();
		} catch (FileNotFoundException e) {
			System.out.println("no File");
			return;  //없다고 종료하기보단 다시 기회를 주자
		}		
	}

	static void addWord(String str) {
		int index = findWord( str );	// returns -1 if not found
		if (index != -1) {		// found words[index] == str
			count[index]++;
		}
		else {	// not found
			words[n] = str;
			count[n] = 1;
			n++;
		}
	}
	
	static int findWord(String str) {
		for (int i=0; i < n; i ++)
			if (words[i].equalsIgnoreCase((str)) )
				return i;
		return -1;
	}	
	
	
}

```



# 문자열 다루기 3

- code 22 개선하자!
- 소수점, 특수기호가 단어에 포함, 숫자 등이 단어에 포함, 대소문자는 맨밑에 수정해서 됬지만, 알파벳 순서대로 ㄱㄱ
- String 클래스 기본 메서드

![1](https://user-images.githubusercontent.com/45934115/58763366-af0c8c80-8594-11e9-96f3-83acc079320c.PNG)



- ex) "-?*he-llo+=() 면 he-llo 가 남게 하겠다!

### Code23 이 되어야하지만 Code 22에 쓴 친구

```java
package Section3;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class Code22 {

	static String [] words = new String [100000];
	static int [] count = new int [100000];
	static int n= 0;
	
	public static void main(String[] args) {
		
		
		Scanner kb = new Scanner(System.in);
		
		while(true) {
			
			System.out.print("$ ");
			String command = kb.next();
			if (command.equals("read") ) {
				String fileName = kb.next();
				makeIndex( fileName );
			}
			else if (command.equals("find")) {
				String str = kb.next();
				int index = findWord(str);
				if (index > -1) {
					System.out.println("The word " + words[index] + " appears " + count[index] + " times.");
				}
				else
					System.out.println("The word" + str + " does not appear.");
			}
			else if (command.equals("saveas")) {
				String fileName = kb.next();
				saveAs( fileName );
			}
			else if (command.equals("exit")) {
				break;
			}
			
		}
		kb.close();
	}
		

	
	static void saveAs(String fileName) {
		
		PrintWriter outFile;
		try {
			outFile = new PrintWriter(new FileWriter(fileName));	// out 부분은 내가정하는 이름
			
			for (int i=0; i<n; i++)
				outFile.println(words[i] + " " + count[i]);
		
			
			outFile.close();
		} catch (IOException e) {
			System.out.println("Save failed");
		} 
		
		
		
		
	}
	
	
	static void makeIndex( String fileName) {
		
		try {
			Scanner inFile = new Scanner( new File(fileName));
			while(inFile.hasNext()) {
				String str = inFile.next();
				
				
				String trimmed = trimming(str);
				
				if (trimmed != null) {
					String t = trimmed.toLowerCase();
					addWord( t );  // 목록에서 검사해서 상황에 따라 다르게하기
						
				}
			}
			
			
			inFile.close();
		} catch (FileNotFoundException e) {
			System.out.println("no File");
			return;  //없다고 종료하기보단 다시 기회를 주자
		}		
	}

	static String trimming(String str) {
		
		int i= 0, j= str.length()-1;
		while( i <= str.length()-1 && !Character.isLetter(str.charAt(i) ) ) //while i번째 character is not letter
			i++;
		
		while( j >=0 && !Character.isLetter(str.charAt(j) ) ) //while i번째 character is not letter
			j--;
		
		if (i > j)    // trimming을 했더니 남는게 없다면
			return null;
		
		return str.substring(i, j+1);	// [  ) 가 되어서 i부터 j까지 잘라낸 문자열을 반환하는 substring
		
										// i <= .... <= j
	}



	static void addWord(String str) {
		
		int index = findWord( str );	// returns -1 if not found
	
		if (index != -1) {		// found words[index] == str
			count[index]++;
		}
		else {	// not found
			
			int i = n-1;
			while (i >= 0 && words[i].compareTo(str) > 0) {
				words[i+1] = words[i];
				count[i+1] = count[i];
				i--;
			}
			words[i+1] = str;
			count[i+1] = 1;
			n++;
		}
	}
	
	
	static int findWord(String str) {
		for (int i=0; i < n; i ++)
			if (words[i].equalsIgnoreCase((str)) )
				return i;
		return -1;
	}	
	
	
}

```

