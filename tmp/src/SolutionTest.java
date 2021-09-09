import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

import java.util.Map;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class SolutionTest {

    Solution solution;

    @BeforeEach
    void setUp() {
        solution = new Solution();
    }

    @Test
    void getPrimeRecordTableTest() throws Exception {

        String test = "9abcDe";
        StringBuffer newString = new StringBuffer();
        for (int i = 0; i < test.length(); i++) {
            newString.append(Character.toUpperCase(test.charAt(i)));
        }

        System.out.println(newString);
    }
}