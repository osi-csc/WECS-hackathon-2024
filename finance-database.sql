CREATE TABLE IF NOT EXISTS Users (
  userID SERIAL PRIMARY KEY,
  username VARCHAR(40),
  userPassword VARCHAR(40),
  startDate DATE
);

CREATE TABLE IF NOT EXISTS TransactionTypes (
  transactionTypeID SERIAL PRIMARY KEY,
  transactionTypeName VARCHAR(70) UNIQUE
);

CREATE TABLE IF NOT EXISTS Categories (
  categoryID SERIAL PRIMARY KEY,
  categoryName VARCHAR(50) UNIQUE
);

CREATE TABLE IF NOT EXISTS Transactions (
  transactionID SERIAL PRIMARY KEY,
  transactionType VARCHAR(70) REFERENCES TransactionTypes(transactionTypeName),
  categoryID INTEGER REFERENCES Categories(categoryID),
  userID INTEGER REFERENCES Users(userID),
  amount DECIMAL(15, 2),
  transactionDate TIMESTAMP,
  transactionNote TEXT
);

CREATE TABLE IF NOT EXISTS Budgets (
  budgetID SERIAL PRIMARY KEY,
  userID INTEGER REFERENCES Users(userID),
  categoryID INTEGER REFERENCES Categories(categoryID),
  amount DECIMAL(15, 2),
  startDate DATE,
  endDate DATE
);

CREATE TABLE IF NOT EXISTS Goals (
  goalID SERIAL PRIMARY KEY,
  userID INTEGER REFERENCES Users(userID),
  goalName VARCHAR(70),
  targetAmount DECIMAL(15, 2),
  curentAmount DECIMAL(15, 2) DEFAULT 0,
  goalEndDate DATE  
  );

CREATE TABLE IF NOT EXISTS Bills (
  billID SERIAL PRIMARY KEY,
  userID INTEGER REFERENCES Users(userID),
  categoryID INTEGER REFERENCES Categories(categoryID),
  amount DECIMAL(15,2),
  interval VARCHAR(15) CHECK (interval IN ('daily', 'weekly', 'monthly', 'yearly')),
  intervalFrequency INTEGER,
  nextPayDay DATE
  );

CREATE TABLE IF NOT EXISTS Incomes (
  incomeID SERIAL PRIMARY KEY,
  userID INTEGER REFERENCES Users(userID),
  incomeSource VARCHAR(70),
  amount DECIMAL(15, 2),
  incomeDate TIMESTAMP,
  incomeNote TEXT
);

CREATE TABLE IF NOT EXISTS Debts (
  debtID SERIAL PRIMARY KEY,
  userID INTEGER REFERENCES Users(userID),
  debtAmount DECIMAL(15, 2),
  dueDate DATE,
  interestRate DECIMAL(5, 2),
  remainingBalance DECIMAL(15, 2)
);

