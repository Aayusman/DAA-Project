README

## Code Environment
*   **Language:** Python 3.x
*   **Operating System:** OpenSUSE Tumbleweed; any Linux based OS would suffice
*   **Terminal Emulator:** Konsole; Any Linux based terminal would suffice
*   **External Dependencies:** None (standard built-in Python libraries: `sys`, `os` has been used)

## Input Format
The script accepts structural organization input either via standard input (`stdin`) or by passing a plain text file path as a command-line argument.

### Line Format
Each line defines a manager and their direct subordinates using the following syntax:
```text
ManagerName: Subordinate1, Subordinate2, Subordinate3
```

### Constraints & Rules
*   **Leaves:** For subordinates who do not manage anyone, leave the section after the colon empty (e.g., `Subordinate1:`).
*   **Separators:** Use a colon (`:`) to separate the manager from their subordinates, and commas (`,`) to separate individual subordinate names.
*   **Whitespace:** Leading and trailing whitespaces around names are automatically trimmed.

### Execution Methods
1.  **File Input:**
    ```bash
    python3 scriptname.py hierarchy.txt
    ```
2.  **Manual Terminal Input:**
    Run the script directly, paste or type the structure, and press `Ctrl+D` to send the EOF (End-of-File) signal to process:
    ```bash
    python3 scriptname.py
    ```

## Output Format
The program calculates the mathematically optimal Minimum Dominating Set for the provided tree hierarchy and prints the selected team members to the standard output.

### Output Syntax
The output prints a list representation of string identifiers corresponding to the selected managers/subordinates:
```text
Optimal Communications Team: ['Name1', 'Name2']
```
