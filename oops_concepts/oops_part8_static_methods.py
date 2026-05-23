class StaticMethodsTesting:

    @staticmethod
    def is_valid_email(text):
        return "@" in text and "." in text

    @staticmethod
    def to_snake_case(text):
        return text.lower().replace(" ","_")

print(StaticMethodsTesting.is_valid_email("srini.k@gmail.com"))

print(StaticMethodsTesting.to_snake_case("This is a Snake Case"))