from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def main():
    '''print(get_files_info("calculator", ".") + "\n")
    print(get_files_info("calculator", "pkg") + "\n")
    print(get_files_info("calculator", "/bin") + "\n")
    print(get_files_info("calculator", "../"))'''

    print(get_file_content("calculator", "main.py") + "\n")
    print(get_file_content("calculator", "pkg/calculator.py") + "\n")
    print(get_file_content("calculator", "/bin/cat") + "\n")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))



if __name__ == "__main__":
    main()