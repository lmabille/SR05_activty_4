from tkinter import *
import sys
import select


class ExampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        toolbar = Frame(self)
        toolbar.pack(side="top", fill="x")
        b1 = Button(self, text="print to stdout", command=self.print_stdout)
        b2 = Button(self, text="print to stderr", command=self.print_stderr)
        b1.pack(in_=toolbar, side="left")
        b2.pack(in_=toolbar, side="left")
        Frame1 = Frame(self, borderwidth=2, relief=GROOVE, width=200, height=200)
        Frame1.pack(side=LEFT, padx=30, pady=30)
        Frame2 = Frame(self, borderwidth=2, relief=GROOVE, width=200, height=200)
        Frame2.pack(side=RIGHT, padx=30, pady=30)
        Label(Frame1, text="STDOUT").pack(padx=10, pady=10)
        Label(Frame2, text="STDERR").pack(padx=10, pady=10)
        self.text_1 = Text(Frame1, wrap="word")
        self.text_2 = Text(Frame2, wrap="word")
        self.text_1.pack(side="top", fill="both", expand=True)
        self.text_1.tag_configure("stderr", foreground="#b22222")
        self.text_2.pack(side="top", fill="both", expand=True)
        self.text_2.tag_configure("stderr", foreground="#b22222")
        sys.stdout = TextRedirector(self.text_1, "stdout")
        sys.stderr = TextRedirector(self.text_2, "stderr")
        self.after(1000, self.my_mainloop())

    def print_stdout(self):
        sys.stdout.write("Hello")

    def print_stderr(self):
        '''Illustrate that we can write directly to stderr'''
        mot = sys.stdin.readline()
        sys.stderr.write(f"reception de {mot}")

    def my_mainloop(self):
        print("Hello World!")
        if select.select([sys.stdin, ], [], [], 0.0)[0]:
            for line in sys.stdin:
                sys.stderr.write(f"reception de {line}")
                break
        self.after(1000, self.my_mainloop)


class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")


app = ExampleApp()
app.mainloop()
