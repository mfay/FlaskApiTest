from api import api, models, db, ma
from flask_restplus import Resource, Api, reqparse, inputs
from api.models import Employee


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class EmployeeSchema(ma.ModelSchema):
    class Meta:
        model = Employee

@api.route('/employees')
class EmployeeList(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', default='', help='Filter by email address')
        parser.add_argument('firstName', default='', help='Filter by first name')
        parser.add_argument('lastName', default='', help='Filter by last name')
        args = parser.parse_args()
        all_employees = (
            Employee.query
            .filter(Employee.email.contains(args.email))
            .filter(Employee.firstName.contains(args.firstName))
            .filter(Employee.lastName.contains(args.lastName))
            .all()
        )
        employee_schema = EmployeeSchema(many=True)
        return employee_schema.jsonify(all_employees)