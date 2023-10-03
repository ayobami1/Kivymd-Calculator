# KivyMD Calculator App

## Description
This is a simple calculator app built using the KivyMD framework. It provides basic mathematical operations and a user-friendly interface for performing calculations.

## Features
- Addition, subtraction, multiplication, and division operations
- Clear button (C) to reset the calculator
- Delete button (Del) to remove the last character
- Error handling for invalid expressions
- Color customization

## Screenshots
![App Screenshot](https://github.com/ayobami1/Kivymd-Calculator/blob/main/Screenshot/Screen%20Shot%202023-10-04%20at%2012.02.06%20AM.png)
### You can use the Color Picker API to change color Directly
![change Color](https://github.com/ayobami1/Kivymd-Calculator/blob/main/Screenshot/Screen%20Shot%202023-10-04%20at%2012.08.17%20AM.png)

![App ScreenShot](https://github.com/ayobami1/Kivymd-Calculator/blob/main/Screenshot/Screen%20Shot%202023-10-04%20at%2012.08.08%20AM.png)

### From this Line you can change the button
```python
  for btn_txt in button:
                self.btn_lyt = MDFlatButton(
                    # text = btn_txt,
                    text =f"[b]{btn_txt}[/b]",
                    text_color = (0, 0, 0, 1),  # Dark yellow color
                    theme_text_color = "Primary",
                    on_press= lambda x, btn=btn_txt:self.button_press(btn, x)
                    # on_press= lambda btn_txt:self.button_press(btn_txt),
                    # on_press=partial(self.button_press, btn_txt)
```
![App ScreenShot](https://github.com/ayobami1/Kivymd-Calculator/blob/main/Screenshot/Screen%20Shot%202023-10-04%20at%2012.07.17%20AM.png)


## Prerequisites
- [Python](https://www.python.org/downloads/) installed on your system
- [KivyMD](https://github.com/kivymd/KivyMD) library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/kivymd-calculator.git
