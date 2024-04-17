package it.unical.demacs.informatica.gestorelibri.model;

public record Book(String isbn, String title, String author, String publisher, String year) {
    public Book{
        if(isbn == null || title == null || author == null || publisher == null || year == null)
            throw new IllegalArgumentException("Parameters cannot be null");
        if(isbn.isBlank() || title.isBlank() || author.isBlank() || publisher.isBlank() || year.isBlank())
            throw new IllegalArgumentException("Parameters cannot be null");
    }
    @Override
    public String toString(){
        return isbn + ";" + title + ";" + author + ";" + publisher + ";" + year;
    }
}
