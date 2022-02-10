# # import another_module
# #
# #
# #
# # print(another_module.another_variable)
#
#
# from turtle import Turtle, Screen
#
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
#
# print(timmy)
#
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Raichu", "Pichu"])
table.add_column("Type",["Electric","Electric","Electric"])

table.align = "l"

print(table)
