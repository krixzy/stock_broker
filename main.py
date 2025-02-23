import argparse

def command():
    parser = argparse.ArgumentParser(description="This is a simple program that takes a string and returns the string in reverse")
    parser.add_argument("Command", help="Enter a string to reverse")
    args = parser.parse_args()
    return args


def model_test():
    


if __name__ == "__main__":
