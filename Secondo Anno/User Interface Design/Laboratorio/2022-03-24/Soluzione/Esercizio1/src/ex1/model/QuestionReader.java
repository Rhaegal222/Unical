package ex1.model;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;

public class QuestionReader {
	
	public ExamTest readExam(File f) throws Exception {
		ExamTest examTest = new ExamTest();
		List<String> lines = Files.readAllLines(Path.of(f.toString()));
		for(int i = 0; i < lines.size(); i+=2) {
			String text = lines.get(i);
			String[] options = lines.get(i+1).split(";");
			examTest.addQuestion(new Question(text, Arrays.asList(options)));
		}
		return examTest;
	} 
}
