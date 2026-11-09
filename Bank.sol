pragma solidity ^0.8.0;

 contract Bank {

     uint public balance;

     function deposit() public payable {
         balance += msg.value;
     }

     function withdraw(uint amount) public {
         require(amount <= balance, "Insufficient balance");
         balance -= amount;
         payable(msg.sender).transfer(amount);
     }

     function showBalance() public view returns(uint) {
         return balance;
     }
 }
