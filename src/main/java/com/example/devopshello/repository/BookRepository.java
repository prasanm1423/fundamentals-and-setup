package com.example.devopshello.repository;

import com.example.devopshello.model.Book;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Data access layer for Book. Spring Data JPA auto-generates the
 * CRUD implementation at compile time — no manual SQL needed.
 */
@Repository
public interface BookRepository extends JpaRepository<Book, Long> {
}