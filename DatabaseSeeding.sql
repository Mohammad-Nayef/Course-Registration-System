INSERT INTO courses_schedules (days, start_time, end_time, room_no) VALUES
('Monday, Wednesday', '09:00:00', '10:00:00', 101),
('Sunday, Tuesday, Thursday', '10:00:00', '11:00:00', 102),
('Monday, Wednesday', '11:00:00', '12:00:00', 103),
('Sunday, Tuesday, Thursday', '12:00:00', '13:00:00', 104),
('Sunday, Tuesday, Thursday', '13:00:00', '14:00:00', 105);

INSERT INTO courses (code, name, description, prerequisite_id, instructor, capacity, schedule_id) VALUES
('CSE101', 'Introduction to Computer Science', 'An introduction to computer science concepts.', NULL, 'Dr. Smith', 50, 1),
('CSE201', 'Data Structures and Algorithms', 'Study of data structures and algorithms.', NULL, 'Prof. Johnson', 40, 2),
('CSE301', 'Database Management Systems', 'Introduction to database concepts and systems.', NULL, 'Dr. Williams', 30, 3),
('CSE401', 'Software Engineering', 'Principles and practices of software engineering.', 'CSE201', 'Prof. Brown', 35, 4),
('CSE501', 'Artificial Intelligence', 'Study of artificial intelligence techniques.', 'CSE301', 'Dr. Davis', 25, 5);

INSERT INTO enrollments (student_id, course_id) VALUES
(1, 'CSE101'),
(2, 'CSE101'),
(3, 'CSE301'),
(4, 'CSE401'),
(5, 'CSE501');