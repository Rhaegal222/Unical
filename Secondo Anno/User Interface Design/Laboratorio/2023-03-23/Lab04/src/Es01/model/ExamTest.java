package Es01.model;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ExamTest {
	private final List<Question> questions;
	public ExamTest() {
		questions = new ArrayList<>();
	}
	public void addQuestion(Question q) {
		questions.add(q);
	}
	public List<Question> getQuestions() {
		return Collections.unmodifiableList(questions);
	}
}
