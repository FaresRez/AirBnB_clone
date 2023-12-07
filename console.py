import cmd

class Mycmd (cmd.Cmd):
    prompt = "(hbtn) "

    def __init__(self):
        super().__init__()

    def do_test (self, line):
        print(f"welcome to my cmd {line}")

    def do_exit (self, line):
        return True

    def default(self, line):
        print("unknown command")

    def do_help(self, line):
        super().do_help(line)
        
if __name__ == "__main__":
    Mycmd().cmdloop()