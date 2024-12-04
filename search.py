import re

def grep(pattern, file_name):
    try:
        with open(file_name, 'r') as fp:
            for line in fp:
                if re.search(pattern, line):
                    print(line.strip())
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error in grep: {e}")
    return 

def sed(old_pattern, new_pattern, file_name):
    try:
        with open(file_name, 'r') as fp:
            lines = fp.readlines()
        
        # Substitute the pattern in each line
        with open(file_name, 'w') as fp:
            for line in lines:
                new_line = re.sub(old_pattern, new_pattern, line)
                fp.write(new_line)
        
        print(f"Replaced '{old_pattern}' with '{new_pattern}' in file '{file_name}'.")
    except Exception as e:
        print(f"Error in sed: {e}")
    return 

def awk(n, file_name):
    try:
        with open(file_name, 'r') as fp:
            for line in fp:
                columns = line.strip().split()
                if n <= len(columns):  # Check if column exists
                    print(columns[n - 1])
                else:
                    print(f"Line has less than {n} columns: {line.strip()}")
    except ValueError:
        print("Invalid column number.")
    except Exception as e:
        print(f"Error in awk: {e}")
    return 

def main():
    file_name = input("Enter the file name")
    command  = input("Enter the command: grep, sed, awk")

    if command == 'grep':
        pattern = input("Enter the pattern")
        grep(pattern, file_name);
    elif command == 'sed':
        old_pattern = input("Enter old pattern")
        new_pattern = input("Enter new pattern")
        sed(old_pattern, new_pattern, file_name)
    elif command == 'awk':
        n = input("Enter the column number")
        num = int(n)
        awk(n, file_name)
    else:
        print("Comamnd is invalid")

if __name__ == "__main__":
    main()
