package datastructure.sequential;

import static org.assertj.core.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class StackTest {

    private Stack<Integer> stack;

    @BeforeEach
    void setUp() {
        stack = new Stack<>();
    }

    @Test
    void push() {

        int testData = 1;
        stack.push(testData);
        assertThat(stack.pop()).isEqualTo(testData);
    }
}