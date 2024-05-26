lang="python"
x =lang.split("y")
print(x)
match lang:
    case "PHP":
        print("PHP")
    case  "JS":
        print("JS")
    case  "python":
        print("python")
    case _:
        print("No break")            

        # |   or     vertical bar
        