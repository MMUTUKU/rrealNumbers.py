class Real_number:
  def __init__(self, num1, num2):
      self.num1 = num1
      self.num2 = num2

  def options(self):
      print("Which operation do you want to carry out? (1-6)")
      print("1. Addition")
      print("2. Subtraction")
      print("3. Multiplication")
      print("4. Division")
      print("5. Compare")
      print("6. Quit")

  def addition(self, num1, num2):
      return num1 + num2

  def subtraction(self, num1, num2):
      return num1 - num2

  def multiply(self, num1, num2):
      return num1 * num2

  def division(self, num1, num2):
      if num2 != 0:
          return num1 / num2
      else:
          return "Error! Division by zero."

  def compare(self, num1, num2):
      if num1 > num2:
          return f"{num1} is greater than {num2}"
      elif num1 < num2:
          return f"{num1} is less than {num2}"
      else:
          return f"{num1} is equal to {num2}"

def main():
  while True:
      num1 = input("Enter the first number: ")
      num2 = input("Enter the second number: ")

      if num1.isdigit() and num2.isdigit():
          num1 = int(num1)
          num2 = int(num2)
          real = Real_number(num1, num2)

          while True:
              real.options()
              choice = int(input("Enter your choice: "))

              if choice == 1:
                  print(real.addition(num1, num2))
              elif choice == 2:
                  print(real.subtraction(num1, num2))
              elif choice == 3:
                  print(real.multiply(num1, num2))
              elif choice == 4:
                  print(real.division(num1, num2))
              elif choice == 5:
                  print(real.compare(num1, num2))
              elif choice == 6:
                  print("Goodbye!")
                  return
              else:
                  print("Invalid choice. Please enter a number between 1 and 6.")
      else:
          print("Sorry, but you can only enter numbers. Try again.")

if __name__ == "__main__":
    main()
