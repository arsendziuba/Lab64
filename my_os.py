import os

def main():
    # Print computer name and processor architecture
    print("Computer Name:", os.environ['COMPUTERNAME'])
    print("Processor Architecture:", os.environ['PROCESSOR_ARCHITECTURE'])

    # Print current working directory
    print("Current Working Directory:", os.getcwd())

    # Change working directory to "C:"
    os.chdir("C:")
    print("Changed Working Directory to C:")

    # Print list of directories
    print("List of Directories in C:")
    for directory in os.listdir():
        if os.path.isdir(directory):
            print(directory)

    # Print list of files and check if they are links
    print("List of Files in C:")
    for file in os.listdir():
        if os.path.isfile(file):
            print(file)
            if os.path.islink(file):
                print(f"{file} is a symbolic link")

    # Back to initial working directory
    os.chdir(os.path.expanduser("~"))
    print("Changed Working Directory back to initial directory")

    # Create "Temp" folder
    os.mkdir("Temp")
    print("Created 'Temp' folder")

    # Delete "Temp" folder
    os.rmdir("Temp")
    print("Deleted 'Temp' folder")

if __name__ == "__main__":
    main()
