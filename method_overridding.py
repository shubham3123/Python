class Parent:
    def show(self):
        print("Parent Class")

        class Child(Parent):
            def show(self):
                print("Child Class")

super().show()  # This will call the Parent's show method