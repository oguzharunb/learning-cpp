SRC = main.cpp

OBJ = $(SRC:.cpp=.o)

NAME = megaphone

all: $(NAME)

$(NAME): $(OBJ)
	g++ -o $(NAME) $(OBJ)

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all