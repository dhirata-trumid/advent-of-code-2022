        IDENTIFICATION DIVISION.
        PROGRAM-ID. day1part1.

        ENVIRONMENT DIVISION.
           INPUT-OUTPUT SECTION.
              FILE-CONTROL.
              SELECT CALORIE ASSIGN TO 'sample/calorie_input.txt'
              ORGANIZATION IS LINE SEQUENTIAL.

        DATA DIVISION.
           FILE SECTION.
           FD CALORIE.
           01 CALORIE-FILE.
              05 AMOUNT PIC X(20).

        WORKING-STORAGE SECTION.
            01 WS-CALORIE.
                05 WS-AMOUNT PIC X(20).
            01 WS-EOF PIC A(1).
            01 MAX_CAL PIC 9(9) VALUE ZERO.
            01 TEMP_CAL PIC 9(9) VALUE ZERO.
            01 CUMULATIVE_CAL PIC 9(9) VALUE ZERO.
            01 MAX_CAL_FORMATTED PIC Z(9).

        PROCEDURE DIVISION.
            OPEN INPUT CALORIE.
                PERFORM UNTIL WS-EOF='Y'
                    READ CALORIE INTO WS-CALORIE
                        AT END MOVE 'Y' TO WS-EOF
                        NOT AT END
                            SET TEMP_CAL TO FUNCTION NUMVAL(WS-AMOUNT)
                            IF TEMP_CAL IS EQUAL TO 0
                                IF CUMULATIVE_CAL > MAX_CAL
                                    SET MAX_CAL TO CUMULATIVE_CAL
                                END-IF
                                SET CUMULATIVE_CAL TO 0
                            ELSE
                                ADD TEMP_CAL TO CUMULATIVE_CAL
                            END-IF
                    END-READ
                END-PERFORM.
            CLOSE CALORIE.
            MOVE MAX_CAL TO MAX_CAL_FORMATTED
            DISPLAY FUNCTION TRIM(MAX_CAL_FORMATTED)
        STOP RUN.
