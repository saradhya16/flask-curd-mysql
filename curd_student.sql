use mysql; 
CREATE TABLE student (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  age INT NOT NULL,
  location VARCHAR(255) NOT NULL
);

select * from student;
