package ex1.model;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ExamTest {
	
	private List<Question> questions;
	
	public ExamTest() {
		questions = new ArrayList<Question>();
	}
	
	public void addQuestion(Question q) {
		questions.add(q);
	}
	
	public List<Question> getQuestions() {
		return Collections.unmodifiableList(questions);
	}
}
