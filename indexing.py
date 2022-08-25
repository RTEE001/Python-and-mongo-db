from mongo_db import Visitor

def create_visitor(name, age,date, time ,assistant ,comments ):
    visitor = Visitor(visitor_name =name,visitor_age =age,
    date_of_visit =date, time_of_visit = time,
    assistant =assistant,comments =comments)
    visitor.save()

def list_visitors():
    visitors = []
    for visitor in Visitor.objects:
        visitors.append(visitor)
    return visitors

def delete_visitor(name):
    Visitor.objects(Visitor_name=name).delete()

update_visitor
visitor_details: Given a visitor’s id, return all information about that visitor.
delete_all