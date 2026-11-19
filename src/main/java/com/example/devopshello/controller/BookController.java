package com.example.devopshello.controller;

import com.example.devopshello.model.Book;
import com.example.devopshello.repository.BookRepository;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * REST controller exposing a JSON API for managing books.
 * Base path: /api/books
 */
@RestController
public class BookController {

    private final BookRepository bookRepository;

    public BookController(BookRepository bookRepository) {
        this.bookRepository = bookRepository;
    }

    @GetMapping("/api/books")
    public List<Book> list() {
        return bookRepository.findAll();
    }

    @GetMapping("/api/books/{id}")
    public ResponseEntity<Book> findById(@org.springframework.web.bind.annotation.PathVariable("id") Long id) {
        return bookRepository.findById(id)
                .map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    @PostMapping("/api/books")
    public ResponseEntity<Book> create(@RequestBody Book book) {
        return ResponseEntity.ok(bookRepository.save(book));
    }

    @PutMapping("/api/books/{id}")
    public ResponseEntity<Book> update(@org.springframework.web.bind.annotation.PathVariable("id") Long id,
                                       @RequestBody Book book) {
        return bookRepository.findById(id)
                .map(existing -> {
                    existing.setTitle(book.getTitle());
                    existing.setAuthor(book.getAuthor());
                    return ResponseEntity.ok(bookRepository.save(existing));
                })
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    @DeleteMapping("/api/books/{id}")
    public ResponseEntity<Void> delete(@org.springframework.web.bind.annotation.PathVariable("id") Long id) {
        return bookRepository.findById(id)
                .map(book -> {
                    bookRepository.delete(book);
                    return ResponseEntity.noContent().<Void>build();
                })
                .orElseGet(() -> ResponseEntity.notFound().build());
    }
}