# Python More Classes
---
In this Project we fully developed a class in python to create and handle rectangles called Rectangle.
Each file added a new feature to said class.
---
0. Empty class
1. Added width and height attributes and getters and setters for them both
2. Defined two methods for returning the perimiter and area for the rectangle
3. Defined the \_\_str__ method to return a visual representation of the rectangle in #'s
4. Defined teh \_\_repr__ method to return a string representation of the rectangle that can be used by eval to make a new rectangle of same dimensions (Rectangle(n, n))
5. Defined \_\_del__ method to say "Bye rectangle..." when an instance of a rectangle was deleted
6. Added a class attribute to keep track of how many instances exist
7. Added a class attribute "print\_symbol" to define how you want the rectangle to be represented in the \_\_str__ method
8. Defined bigger\_or\_equal method to compare and return the greater of two rectangles
9. Defined a class method to return a new rectangle with width and height equal to each size  square(cls, size=0)
