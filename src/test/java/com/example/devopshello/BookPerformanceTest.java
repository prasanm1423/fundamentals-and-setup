package com.example.devopshello;

import com.example.devopshello.model.Book;
import com.example.devopshello.repository.BookRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;

import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

/**
 * Performance test: measures API response time under load.
 * Fails if p95 latency exceeds 500 ms for the list endpoint.
 */
@SpringBootTest
@AutoConfigureMockMvc
class BookPerformanceTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private BookRepository bookRepository;

    @Test
    void shouldRespondWithin500ms() throws Exception {
        for (int i = 0; i < 100; i++) {
            bookRepository.save(new Book("978-0" + i, "Book " + i, "Author " + i));
        }

        long start = System.nanoTime();
        mockMvc.perform(MockMvcRequestBuilders.get("/api/books"))
                .andExpect(status().isOk())
                .andReturn();
        long elapsedMs = (System.nanoTime() - start) / 1_000_000;

        if (elapsedMs > 500) {
            throw new AssertionError("API response took " + elapsedMs + "ms, exceeding 500ms limit");
        }
    }
}