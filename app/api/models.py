# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, Integer, Numeric, SmallInteger, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql.types import MEDIUMBLOB
from sqlalchemy.ext.declarative import declarative_base
from api import db

class Customer(db.Model):
    __tablename__ = 'customers'

    customerNumber = db.Column(Integer, primary_key=True)
    customerName = db.Column(String(50), nullable=False)
    contactLastName = db.Column(String(50), nullable=False)
    contactFirstName = db.Column(String(50), nullable=False)
    phone = db.Column(String(50), nullable=False)
    addressLine1 = db.Column(String(50), nullable=False)
    addressLine2 = db.Column(String(50))
    city = db.Column(String(50), nullable=False)
    state = db.Column(String(50))
    postalCode = db.Column(String(15))
    country = db.Column(String(50), nullable=False)
    salesRepEmployeeNumber = db.Column(ForeignKey(u'employees.employeeNumber'), index=True)
    creditLimit = db.Column(Numeric(10, 2))

    employee = relationship(u'Employee')


class Employee(db.Model):
    __tablename__ = 'employees'

    employeeNumber = db.Column(Integer, primary_key=True)
    lastName = db.Column(String(50), nullable=False)
    firstName = db.Column(String(50), nullable=False)
    extension = db.Column(String(10), nullable=False)
    email = db.Column(String(100), nullable=False)
    officeCode = db.Column(ForeignKey(u'offices.officeCode'), nullable=False, index=True)
    reportsTo = db.Column(ForeignKey(u'employees.employeeNumber'), index=True)
    jobTitle = db.Column(String(50), nullable=False)

    office = relationship(u'Office')
    parent = relationship(u'Employee', remote_side=[employeeNumber])


class Office(db.Model):
    __tablename__ = 'offices'

    officeCode = db.Column(String(10), primary_key=True)
    city = db.Column(String(50), nullable=False)
    phone = db.Column(String(50), nullable=False)
    addressLine1 = db.Column(String(50), nullable=False)
    addressLine2 = db.Column(String(50))
    state = db.Column(String(50))
    country = db.Column(String(50), nullable=False)
    postalCode = db.Column(String(15), nullable=False)
    territory = db.Column(String(10), nullable=False)


class Orderdetail(db.Model):
    __tablename__ = 'orderdetails'

    orderNumber = db.Column(ForeignKey(u'orders.orderNumber'), primary_key=True, nullable=False)
    productCode = db.Column(ForeignKey(u'products.productCode'), primary_key=True, nullable=False, index=True)
    quantityOrdered = db.Column(Integer, nullable=False)
    priceEach = db.Column(Numeric(10, 2), nullable=False)
    orderLineNumber = db.Column(SmallInteger, nullable=False)

    order = relationship(u'Order')
    product = relationship(u'Product')


class Order(db.Model):
    __tablename__ = 'orders'

    orderNumber = db.Column(Integer, primary_key=True)
    orderDate = db.Column(Date, nullable=False)
    requiredDate = db.Column(Date, nullable=False)
    shippedDate = db.Column(Date)
    status = db.Column(String(15), nullable=False)
    comments = db.Column(Text)
    customerNumber = db.Column(ForeignKey(u'customers.customerNumber'), nullable=False, index=True)

    customer = relationship(u'Customer')


class Payment(db.Model):
    __tablename__ = 'payments'

    customerNumber = db.Column(ForeignKey(u'customers.customerNumber'), primary_key=True, nullable=False)
    checkNumber = db.Column(String(50), primary_key=True, nullable=False)
    paymentDate = db.Column(Date, nullable=False)
    amount = db.Column(Numeric(10, 2), nullable=False)

    customer = relationship(u'Customer')


class Productline(db.Model):
    __tablename__ = 'productlines'

    productLine = db.Column(String(50), primary_key=True)
    textDescription = db.Column(String(4000))
    htmlDescription = db.Column(String)
    image = db.Column(MEDIUMBLOB)


class Product(db.Model):
    __tablename__ = 'products'

    productCode = db.Column(String(15), primary_key=True)
    productName = db.Column(String(70), nullable=False)
    productLine = db.Column(ForeignKey(u'productlines.productLine'), nullable=False, index=True)
    productScale = db.Column(String(10), nullable=False)
    productVendor = db.Column(String(50), nullable=False)
    productDescription = db.Column(Text, nullable=False)
    quantityInStock = db.Column(SmallInteger, nullable=False)
    buyPrice = db.Column(Numeric(10, 2), nullable=False)
    MSRP = db.Column(Numeric(10, 2), nullable=False)

    productline = relationship(u'Productline')
