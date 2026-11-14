package com.internship.hello;

/**
 * Phase 1 Hello World milestone in Java.
 */
public class Greeting {

    public String greet(String name) {
        return "Hello, " + name + "!";
    }

    public static void main(String[] args) {
        Greeting greeting = new Greeting();
        System.out.println(greeting.greet("World"));
        System.out.println(greeting.greet("Internship"));
    }
}
