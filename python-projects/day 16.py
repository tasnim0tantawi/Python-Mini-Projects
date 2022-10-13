from turtle import Turtle, Screen
timmy = Turtle()
screen = Screen()
screen.bgcolor("black")
timmy.shape("turtle")
timmy.color("white", "coral")
timmy.forward(100)
# pypi is python package index that contains a lot of python packages
# a package is a collection of files (modules) that can be imported

screen.exitonclick()


class User:
    def __init__(self, id, name, email):
        # self is the instance of the class
        # __init__ is the constructor, it is called when you create a new object of the class
        self.id = id
        self.name = name
        self.email = email
        self.followers = 0
        self.following = 0
        print(f"User {self.name} with id {self.id} has been created.")

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def unfollow(self, user):
        if user.followers > 0:
            user.followers -= 1
            self.following -= 1



