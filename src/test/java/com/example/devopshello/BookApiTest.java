package com.example.devopshello;

import com.example.devopshello.model.Book;
import com.example.devopshello.repository.BookRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;
import static org.hamcrest.CoreMatchers.hasItem;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.delete;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.put;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

/**
 * Integration tests for the Book REST API.
 * Uses MockMvc to exercise the full Spring MVC stack against an in-memory H2 database.
 */
@SpringBootTest
@AutoConfigureMockMvc
class BookApiTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private BookRepository bookRepository;

    @Test
    void shouldListBooks() throws Exception {
        bookRepository.save(new Book("978-0134853987", "Clean Code", "Robert C. Martin"));

        mockMvc.perform(get("/api/books"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$[*].title").value(hasItem("Clean Code")));
    }

    @Test
    void shouldCreateBook() throws Exception {
        String body = "{\"isbn\":\"978-0201616224\",\"title\":\"The Pragmatic Programmer\",\"author\":\"Andy Hunt\"}";

        mockMvc.perform(post("/api/books")
                        .contentType(org.springframework.http.MediaType.APPLICATION_JSON)
                        .content(body))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.title").value("The Pragmatic Programmer"));
    }

    @Test
    void shouldDeleteBook() throws Exception {
        Book saved = bookRepository.save(new Book("978-0134853987", "Clean Code", "Robert C. Martin"));

        mockMvc.perform(delete("/api/books/" + saved.getId()))
                .andExpect(status().isNoContent());

        mockMvc.perform(get("/api/books/" + saved.getId()))
                .andExpect(status().isNotFound());
    }

    @Test
    void shouldRejectBlankTitleOnUpdate() throws Exception {
        Book saved = bookRepository.save(new Book("978-0306406153", "Effective Java", "Joshua Bloch"));

        mockMvc.perform(put("/api/books/" + saved.getId())
                        .contentType(org.springframework.http.MediaType.APPLICATION_JSON)
                        .content("{\"isbn\":\"978-0134853987\",\"title\":\"\",\"author\":\"X\"}"))
                .andExpect(status().isBadRequest());
    }

    @Test
    void shouldRejectBlankIsbnOnCreate() throws Exception {
        mockMvc.perform(post("/api/books")
                        .contentType(org.springframework.http.MediaType.APPLICATION_JSON)
                        .content("{\"isbn\":\"\",\"title\":\"X\",\"author\":\"Y\"}"))
                .andExpect(status().isBadRequest());
    }
}
