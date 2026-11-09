//bct 4th 
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {

    struct Student {
        uint rollNo;
        string name;
        uint marks;
    }

    Student[] public students;

    function addStudent(uint r, string memory n, uint m) public {
        students.push(Student(r, n, m));
    }

    function getStudent(uint i) public view returns (uint, string memory, uint) {
        Student memory s = students[i];
        return (s.rollNo, s.name, s.marks);
    }

    fallback() external payable {
    }
}
