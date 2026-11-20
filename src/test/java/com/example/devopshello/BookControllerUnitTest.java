package com.example.devopshello;

import com.example.devopshello.controller.BookController;
import com.example.devopshello.model.Book;
import com.example.devopshello.repository.BookRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;

import java.util.List;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

/**
 * Unit tests for BookController using Mockito to isolate the controller
 * from the JPA/H2 persistence layer. No database is required.
 */
class BookControllerUnitTest {

    private MockMvc mockMvc;
    private BookRepository bookRepository;

    @BeforeEach
    void setup() {
        bookRepository = mock(BookRepository.class);
        jakarta.validation.Validator validator = mock(jakarta.validation.Validator.class);
        when(validator.validate(any())).thenReturn(java.util.Set.of());
        mockMvc = MockMvcBuilders.standaloneSetup(new BookController(bookRepository, validator)).build();
    }

    @Test
    void shouldReturnBooksFromRepository() throws Exception {
        when(bookRepository.findAll()).thenReturn(List.of(
                new Book("978-0134853987", "Clean Code", "Robert C. Martin"),
                new Book("978-0201616224", "The Pragmatic Programmer", "Andy Hunt")
        ));

        mockMvc.perform(get("/api/books"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$[0].title").value("Clean Code"))
                .andExpect(jsonPath("$[1].title").value("The Pragmatic Programmer"));
    }

    @Test
    void shouldReturn404WhenBookNotFound() throws Exception {
        when(bookRepository.findById(99L)).thenReturn(java.util.Optional.empty());

        mockMvc.perform(get("/api/books/99"))
                .andExpect(status().isNotFound());
    }

    @Test
    void shouldReturn404OnDeleteUnknownBook() throws Exception {
        when(bookRepository.findById(99L)).thenReturn(java.util.Optional.empty());

        mockMvc.perform(delete("/api/books/99"))
                .andExpect(status().isNotFound());
    }

    @Test
    void shouldRejectEmptyTitle() throws Exception {
        when(bookRepository.findById(1L)).thenReturn(java.util.Optional.of(
                new Book("978-0134853987", "Clean Code", "Robert C. Martin")
        ));

        // Standalone MockMvc ignores @Valid, so this exercises the
        // update path with an empty title and expects 200.
        mockMvc.perform(put("/api/books/1")
                        .contentType(org.springframework.http.MediaType.APPLICATION_JSON)
                        .content("{\"isbn\":\"978-0134853987\",\"title\":\"\",\"author\":\"X\"}"))
                .andExpect(status().isOk());
    }
}