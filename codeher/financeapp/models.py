from django.db import models

class User(models.Model):
    userID = models.AutoField(primary_key=True)  # Maps to SERIAL in PostgreSQL
    username = models.CharField(max_length=40)
    userPassword = models.CharField(max_length=40)
    startDate = models.DateField(auto_now_add=True )

class TransactionTypes(models.Model): 
    transactionTypeID = models.AutoField(primary_key=True)
    transactionTypeName = models.CharField(max_length=70, unique=True)
    
class Categories (models.Model):
    categoryID = model.AutoField(primary_key=true)
    categoryName = models.CharField(max_length=50, unique=True)
    
class Transactions(models.Model):
    transactionID =models.AutoField(primary_key=True)
    transactionType= models.ForeignKey(TransactionTypes, to_field='transactionTypeName',on_delete=models.CASCADE)#foriegn key to TransactionTypeName from TransactionTypes
    categoryID=models.ForeignKey(Categories, to_field='categoryID', on_delete=models.CASCADE)
    userID=models.ForeignKey(User,to_field='userID',on_delete=models.CASCADE)
    amount=models.DecimalFields(max_digits=15, decimal_places=2, null=True, blank=True, default=0.00)
    transactionDate=models.DataTimeField()#later come back to add null and blank default
    transactionNote=models.TextField(null=True,blank=True,default="n/a")

class Budgets(models.Model):
    budgetID= model.AutoField(primary_key=true)
    userID=models.ForeignKey(User, to_field= 'userID',on_delete=models.CASCADE)
    categoryID=models.ForeignKey(Categories, to_field='categoryID', on_delete=models.CASCADE)
    amount=models.DecimalFields(max_digits=15, decimal_places=2, null=True, blank=True, default=0.00)
    startDate=models.DateField()
    endDate=models.DateField()

class Goals(models.Model):
    goalID=models.AutoField(primary_key=true)
    userID=models.ForeignKey(User,to_field='userID',on_delete=models.CASCADE)
    goalName=models.CharField(max_length=70)
    targetAmount= models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0.00)
    currentAmount= models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0.00)
    goalEndDate = models.DateField()
    #add an add amount to goal

class Bills(models.Model):
    billID=models.AutoField(primary_key=true)
    userID=models.ForeignKey(User,to_field='userID',on_delete=models.CASCADE)
    categoryID=models.ForeignKey(Categories,to_field='categoryID',on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0.00)
    interval= models.CharField(max_length=15)
    intervalFrequency=models.IntegerField()
    NextPayDay=models.DateField()

class Incomes(models.Model):
    incomeID=models.AutoField(primary_key=true)
    userID=models.ForeignKey(User,to_field='userID', on_delete=models.CASCADE)
    incomeSource=models.CharField(max_length=70)
    amount= models.DecimalFielduserID=models.ForeignKey(User,on_delete=models.CASCADE)
    incomeDate= models.DateTimeField()
    incomeNote= models.TextField(null=True,blank=True,default="n/a")
    
class Debts(models.Model):
    debtID=models.AutoField(primary_key=true)
    userID=models.ForeignKey(User,to_field='userID',on_delete=models.CASCADE)
    debtAmount=models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0.00)
    dueDate=models.DateField()
    interestRate=models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    remainingBalance=models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0.00)

class   
    def __str__(self):
        return self.username
