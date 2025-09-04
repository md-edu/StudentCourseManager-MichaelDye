# StudentCourseManager-MichaelDye

This is an app that manages students and their courses. It has the following features:
 - Add student
 - Remove student
 - Enroll student in courses
 - Remove a course from a student
 - Add grades for a course
 - Display student info
 - Display all students info
 - Save data as a JSON file
 - Load data from a JSON file

## Reflection: Agile vs Waterfall method
  Over the course of developing this project by using the Agile method, I had a couple of instances where I realized some of the advantages of the waterfall method. For starters, I didn't implement a display info feature in my app until the third sprint. Therefore, as I was working, I had to use the python debugger to verify that my students and courses were being added correctly to the course manager. However, you could argue that this is not necessarily a disadvantage of the agile method, but rather a failure in prioritizing base features in the first sprint. Additionally, midway through working on my project, I realized that it would've been more efficient to treat the courses as objects with properties for credits, name, and grades, but in order to pivot into this structure, it would take more time to rewrite what I had already done. With the waterfall method, I likely would've designed the course class from the beginning, knowing that specific properties were going to be needed of it down the line. One of these properties was the credits property. Originally, when creating courses, the only thing the user was prompted with was the course name, but later on when adding a GPA calculator, I needed to modify the code for creating courses to also link a credit number to each course.

  Clearly there are some ways in which waterfall would've made the code writing process more structured and follow a more holisitc design. However, the waterfall method would have introduced some more overhead in planning and designing the entire project, whereas with the agile method I was able to test out and expand the project modularly, allowing me to see the progress of a growing product in different stages. Additionally, the waterfall method sometimes is unrealistic as the expectations for a project might change midway through working on it. In the case of a coding assignment for a course, the requirements will stay the same, but that is not always the case. Therefore, I think a hybrid method is best, where some of the waterfall planning is mixed with the adaptability of the agile method.

