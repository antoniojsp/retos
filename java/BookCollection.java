import java.util.ArrayList;
import java.util.List;

public class BookCollection {

    // Private list to store the collection of books
    private List<Book> books;

    // Constructor initializes an empty collection
    public BookCollection() {
        this.books = new ArrayList<>();
    }

    // Method to add a new book to the collection
    public void addBook(Book book) {
        this.books.add(book);
    }

    // Method to remove a book from the collection
    public boolean removeBook(Book book) {
        return this.books.remove(book);
    }

    // Method to get the total number of books in the collection
    public int size() {
        return this.books.size();
    }

    // Method to check if the collection contains a specific book
    public boolean contains(Book book) {
        return this.books.contains(book);
    }

    // Method to retrieve a book at a specific index
    public Book getBook(int index) {
        if (index >= 0 && index < this.size()) {
            return this.books.get(index);
        } else {
            throw new IndexOutOfBoundsException("Invalid index");
        }
    }
}