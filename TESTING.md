
# Testing

The deployed project live link is [HERE](https://guess-colors-499273fe225a.herokuapp.com/) - ***Use Ctrl (Cmd) and click to open in a new window.*** 


The following tests were carried out to ensure the portal is working correctly

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Instructions | User is given typed out instructions | Intro screen presented | Works as expected |
| Information | User is given information | Information confirmed as true | Works as expected |
| 1, 2 or 3 option | User selects an answer | Correct information confirmed | Works as expected |
| "n" option  | User selects no to leav the game | Notice appears "Goodbye,see you soon" | Works as expected |
| "y" option  | User selects yes to continue the game | The new color combination apears | Works as expected |
| "invalid" option  | User selects an invalid option e.g. "z" | Notice appears "Invalid choice! Please enter 123 or "y" "n" | Works as expected |

## Testing Browsers
The portal was tested in the following browsers (based on my own testing and those of people who tested the portal):

- Chrome 
- Edge
- Firefox
- Safari 

It worked without issues in the above browsers except Safari. 

## Validation

PEP8 - Python style guide checker imported - [HERE](https://pypi.org/project/pep8/) [HERE](assets/images/Validation.png)
I used [Code Institute's validator](https://pep8ci.herokuapp.com/) to double-check my Python code. The project is without errors.
All code validated and where lines were showing as too long they were adjusted. Some line adjustments caused bugs in the code and it stopped working so I worked on it until the game worked again.



### [BACK TO README](README.md)

