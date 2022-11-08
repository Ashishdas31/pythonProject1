while True:
    def email_slicer():
        print("Welcome to email slicer ")
        print("Enter S to stop")
        print("")

        email_input = input("Input your email address :- ")

        (Username, domain) = email_input.split("@")
        (domain, extension) = domain.split(".")

        print("Username :- ", Username)
        print("Domain :-", domain)
        print("Extension :- ", extension)

    email_slicer()
