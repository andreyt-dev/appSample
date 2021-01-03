class person():
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
    def __str__(self):
        return f"Name:{self.name} |  phone:{self.phone}"

def main():
    a = person("andrey","054-777777")
    print(str(a))

if __name__ == "__main__":
    pass
        